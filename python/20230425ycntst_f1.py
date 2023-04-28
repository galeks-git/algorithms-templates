# https://contest.yandex.ru/contest/23390/problems/?nc=yyZUtgKt

# A. Ближайший ноль
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	3 секунды	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	1.6 секунд	256Mb
# OpenJDK Java 11	1.6 секунд	400Mb
# C# (MS .NET 6.0 + ASP)	1.6 секунд	400Mb
# Golang 1.20.1	0.8 секунд	64Mb
# Kotlin 1.8.0 (JRE 11)	2.5 секунд	256Mb
# GNU c++17 7.3	0.8 секунд	64Mb
# C# (MS .NET 5.0 + ASP)	1.6 секунд	400Mb
# Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

# Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

# Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

# Формат вывода
# Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.







# В начале каждого решения в комментарии укажите ID успешной посылки,
# чтобы ревьюер мог удостовериться, что решение рабочее.
# ID: 86518345
 

file = open("input.txt", "r")
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106)
len_street = int(file.readline())
# В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули)
house_numbers_list = tuple(map(int, file.readline().split()))
# nn = tuple(map(int, file.readline().split()))
file.close()


# print('n=',n)
# print('nn=',nn)

# def ff(i,res,n,first):
 
def digits_waves(begin_list_index, dw_result, dw_len_street, dw_first_wave):
    # print('ff i=',i)
    dw_result[begin_list_index] = 0

    if (begin_list_index < dw_len_street):
        index_right = begin_list_index + 1
        len = 1
        while (index_right < dw_len_street and dw_result[index_right]):
            # print('x=',x)
            dw_result[index_right] = len
            # if (res[x+1]==len):
            #     break
            len += 1
            index_right += 1
        # print('res=',res)

    if (begin_list_index > 0):
        index_left = begin_list_index - 1
        len = 1
        # print('first=',first)
        if (dw_first_wave):
            while (index_left >= 0 and dw_result[index_left]):
                # print('y=',y)
                dw_result[index_left] = len
                len += 1
                index_left -= 1
            # print('res=',res)
        else:
            while (index_left >= 0 and dw_result[index_left]):
                # print('y=',y)
                if (dw_result[index_left] == len):
                    break
                dw_result[index_left] = len
                if (dw_result[index_left-1] == len):
                    break
                len += 1
                index_left -= 1
            # print('res=',res)


def main():
    # result = []
    first_wave = True
    result = list(house_numbers_list)
    # for i in range(len_street):
    #     result.append(house_numbers_list[i])
    for i in range(len_street):
        if house_numbers_list[i] == 0:
            # print('i=',i)
            digits_waves(i, result, len_street, first_wave)
            first_wave = False
    print(*result, sep=' ')


if __name__ == '__main__':
    main()
