# https://contest.yandex.ru/contest/23389/problems/C/
# C. Соседи
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

# Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.



# Формат ввода
# В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

# Формат вывода
# Напечатайте нужные числа в возрастающем порядке через пробел.



file = open("input.txt", "r")
#  В первой строке задано n — количество строк матрицы
n = int(file.readline())
#  Во второй — количество столбцов m
m = int(file.readline())

k_list_list = []
for n_count in range(n):
    ll = list(map(int, file.readline().split()))
    k_list_list.append(ll)

# В последних двух строках записаны координаты элемента, соседей которого нужно найти. 
# Индексация начинается с нуля.
n_pos = int(file.readline())
#  Во второй — количество столбцов m
m_pos = int(file.readline())
file.close()

# print("n=",n)
# print("m=",m)
# print("n_pos=",n_pos)
# print("m_pos=",m_pos)
# print(k_list_list)
# # print(k_list_list[1])
# # print(k_list_list[1][2])
# print(k_list_list[n_pos][m_pos+1])

result=[]
if (n_pos==0 and n!=1):
    result.append(k_list_list[n_pos+1][m_pos])
elif (0<n_pos<n-1 and n!=1):
    result.append(k_list_list[n_pos-1][m_pos])
    result.append(k_list_list[n_pos+1][m_pos])
elif (n_pos==n-1 and n!=1):
    result.append(k_list_list[n_pos-1][m_pos])

if (m_pos==0 and m!=1):
    result.append(k_list_list[n_pos][m_pos+1])
elif (0<m_pos<m-1 and m!=1):
    result.append(k_list_list[n_pos][m_pos+1])
    result.append(k_list_list[n_pos][m_pos-1])
elif (m_pos==m-1 and m!=1):
    result.append(k_list_list[n_pos][m_pos-1])

result.sort()
# print(result)
print(" ".join(map(str, result)))

