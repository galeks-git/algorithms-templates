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


file = open("input.txt", "r")
# В первой строке дано целое число k (1 ≤ k ≤ 5).
k = int(file.readline())
# В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой строке. 
# Каждый символ – либо точка, либо цифра от 1 до 9.
# Символы одной строки идут подряд и не разделены пробелами.

k_list_list = []
for n_count in range(4):
    ll = str(file.readline())
    # ll = map(str, file.readline().split())
    # ll = list(map(str, file.readline().split()))
    k_list_list.append(ll)

file.close()


print('k=',k)
print('k_list_list=',k_list_list)

# def ff(i,res,n,first):
#     # print('ff i=',i)
#     res[i]=0

#     if(i<n):
#         x=i+1
#         len=1
#         while(x<n and res[x]):
#             # print('x=',x)
#             res[x]=len
#             # if (res[x+1]==len):
#             #     break
#             len+=1
#             x+=1
#         # print('res=',res)

#     if(i>0):
#         y=i-1
#         len=1
#         # print('first=',first)
#         if(first):
#             while(y>=0 and res[y]):
#                 # print('y=',y)
#                 res[y]=len
#                 len+=1
#                 y-=1
#             # print('res=',res)
#         else:
#             while(y>=0 and res[y]):
#                 # print('y=',y)
#                 if (res[y]==len):
#                     break
#                 res[y]=len
#                 if (res[y-1]==len):
#                     break
#                 len+=1
#                 y-=1
#             # print('res=',res)



# res=[]
# first=True
# for i in range(n):
#     res.append(nn[i])
# for i in range(n):
#     if nn[i]==0:
#         # print('i=',i)
#         ff(i,res,n,first)
#         first=False
# print(*res, sep=' ')
