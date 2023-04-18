# https://contest.yandex.ru/contest/23389/problems/D/
# D. Хаотичность погоды
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.2 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# OpenJDK Java 11	0.5 секунд	64Mb
# C# (MS .NET 6.0 + ASP)	0.5 секунд	64Mb
# Kotlin 1.8.0 (JRE 11)	0.6 секунд	64Mb
# C# (MS .NET 5.0 + ASP)	0.5 секунд	64Mb
# Метеорологическая служба вашего города решила исследовать погоду новым способом.

# Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
# Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше, чем в день до (если такой существует) и в день после текущего (если такой существует). Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
# Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

# Заметим, что если число показаний n=1, то единственный день будет хаотичным.

# Формат ввода
# В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. Во второй строке даны n целых чисел –— значения температуры в каждый из n дней. Значения температуры не превосходят 273 по модулю.

# Формат вывода
# Выведите единственное число — хаотичность за данный период.



file = open("input.txt", "r")
#  В первой строке дано число n –— длина периода измерений в днях
n = int(file.readline())
#  Во второй строке даны n целых чисел –— значения температуры в каждый из n дней
ll = list(map(int, file.readline().split()))
file.close()

# print("n=",n)
# print("range=",range(n))
# print("m=",m)
# print("n_pos=",n_pos)
# print("m_pos=",m_pos)
# print(ll)
# # print(k_list_list[1])
# # print(k_list_list[1][2])
# print(k_list_list[n_pos][m_pos+1])

res=0
for count in range(n):
    if(n==1):
        res=1
    if(count==0 and n!=1):
        if(ll[count]>ll[count+1]):
            res+=1
    elif(count==n-1):
        if(ll[count]>ll[count-1]):
            res+=1
    else:
        if(ll[count-1] < ll[count] > ll[count+1]):
            res+=1
    
print(res)


# result=[]
# if (n_pos==0 and n!=1):
#     result.append(k_list_list[n_pos+1][m_pos])
# elif (0<n_pos<n-1 and n!=1):
#     result.append(k_list_list[n_pos-1][m_pos])
#     result.append(k_list_list[n_pos+1][m_pos])
# elif (n_pos==n-1 and n!=1):
#     result.append(k_list_list[n_pos-1][m_pos])

# if (m_pos==0 and m!=1):
#     result.append(k_list_list[n_pos][m_pos+1])
# elif (0<m_pos<m-1 and m!=1):
#     result.append(k_list_list[n_pos][m_pos+1])
#     result.append(k_list_list[n_pos][m_pos-1])
# elif (m_pos==m-1 and m!=1):
#     result.append(k_list_list[n_pos][m_pos-1])

# result.sort()
# # print(result)
# print(" ".join(map(str, result)))

