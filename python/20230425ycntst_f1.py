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


# 86852248


def between_zeros(bz_result, begin_zero_index, end_zero_index):
    # print('begin_zero_index=', begin_zero_index)
    # print('end_zero_index=', end_zero_index)
    len_zero_index = end_zero_index-begin_zero_index
    if (len_zero_index <= 1):
        return
    if (len_zero_index <= 2):
        bz_result[begin_zero_index+1] = 1
        return

    count = 0
    while (True):
        x = begin_zero_index + count
        y = end_zero_index - count
        # print('while count=', count)
        # print('while x=', x)
        # print('while y=', y)
        bz_result[x] = count
        bz_result[y] = count
        if (y-x <= 1):
            return
        # if(y-x==1):
        #     return
        count += 1

    # count = 0
    # while(1):
    #     print('while count=', count)
    #     x=begin_zero_index+count
    #     y=end_zero_index-count
    #     print('while x=', x)
    #     print('while y=', y)
    #     bz_result[x]=count
    #     bz_result[y]=count
    #     if(y-x<=0):
    #         return
    #     if(y-x==1):
    #         return
    #     count+=1


def nearest_zero(house_numbers_list, len_street):
    result = list(house_numbers_list)
    # print(*result, sep=' ')

    zero_indexes_list = []
    for i in range(len_street):
        if house_numbers_list[i] == '0':
            zero_indexes_list.append(i)
    # print('zero_indexes_list=', zero_indexes_list)

    # count = zero_indexes_list[0]
    # for i in range(zero_indexes_list[0], 0, -1):
    #     result[i] = count
    #     count -= 1


    ll = list(range(zero_indexes_list[0], 0, -1))
    # print('ll=', ll)
    for i in range(zero_indexes_list[0]):
        result[i] = ll[i]


    # len_ll=len(zero_indexes_list)
    # print('len_ll=', len_ll)
    # print('len_street=', len_street)
    # print('zero_indexes_list[-1]=', zero_indexes_list[-1])

    # for i in range(0, len_ll-1, 1):
    for i in range(0, len(zero_indexes_list)-1, 1):
        between_zeros(result, zero_indexes_list[i], zero_indexes_list[i+1])
    
    count = 0
    for i in range(zero_indexes_list[-1], len_street, 1):
        result[i] = count
        count += 1
    return result


def main():
    file = open("input.txt", "r")
    # В первой строке дана длина улицы —– n (1 ≤ n ≤ 106)
    len_street = int(file.readline())
    # В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули)
    house_numbers_list = tuple(map(str, file.readline().split()))
    # house_numbers_list = tuple(map(int, file.readline().split()))
    file.close()
    result = nearest_zero(house_numbers_list, len_street)
    print(*result, sep=' ')


if __name__ == '__main__':
    main()





# def digits_waves(begin_list_index, dw_result, prev_list_index, next_list_index, dw_len_street):
#     dw_result[begin_list_index] = 0
#     index_left = begin_list_index - 1
#     len = 1

#     if (prev_list_index is not None):
#         while (index_left > prev_list_index):
#             if (dw_result[index_left] == len):
#                 break
#             dw_result[index_left] = len
#             if (dw_result[index_left-1] == len):
#                 break
#             len += 1
#             index_left -= 1
#     else:
#         while (index_left >= 0):
#                 dw_result[index_left] = len
#                 len += 1
#                 index_left -= 1

#     index_right = begin_list_index + 1
#     len = 1

#     if (next_list_index is not None):
#         while (index_right < next_list_index):
#             dw_result[index_right] = len
#             len += 1
#             index_right += 1
#     else:
#         while (index_right < dw_len_street):
#             dw_result[index_right] = len
#             len += 1
#             index_right += 1


# def main():

#     file = open("input.txt", "r")
#     # В первой строке дана длина улицы —– n (1 ≤ n ≤ 106)
#     len_street = int(file.readline())
#     # В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули)
#     house_numbers_list = tuple(map(str, file.readline().split()))
#     # house_numbers_list = tuple(map(int, file.readline().split()))

#     file.close()



#     # result = []
#     # for i in range(len_street):
#     #     result.append(house_numbers_list[i])

#     result = list(house_numbers_list)
#     print(*result, sep=' ')

#     zero_indexes_list = []
#     for i in range(len_street):
#         if house_numbers_list[i] == '0':
#             zero_indexes_list.append(i)
#     print('zero_indexes_list=', zero_indexes_list)

#     for i in range(len(zero_indexes_list)):

#         if i == 0:
#             prev_zero_index = None
#         else:
#             prev_zero_index = zero_indexes_list[i-1]

#         if i+1 == len(zero_indexes_list):
#             next_zero_index = None
#         else:
#             next_zero_index = zero_indexes_list[i+1]

#         digits_waves(
#             zero_indexes_list[i], result,
#             prev_zero_index, next_zero_index, len_street
#         )

#     # for i in range(len_street):
#     #     if house_numbers_list[i] == 0:
#     #         # print('i=',i)
#     #         digits_waves(i, result, len_street, first_wave)
#     #         first_wave = False
#     print(*result, sep=' ')


