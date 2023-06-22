# https://contest.yandex.ru/contest/24735/problems/B/

# B. Эффективная быстрая сортировка
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.5 секунд	17Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	2 секунды	64Mb
# Python 3.7.3	3 секунды	64Mb
# OpenJDK Java 11	3 секунды	64Mb
# C# (MS .NET 6.0 + ASP)	3 секунды	64Mb
# C# (MS .NET 5.0 + ASP)	3 секунды	64Mb
# Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель.

# Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

# Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

# Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").

# Как работает in-place quick sort
# Как и в случае обычной быстрой сортировки, которая использует дополнительную память, необходимо выбрать опорный элемент (англ. pivot), а затем переупорядочить массив. Сделаем так, чтобы сначала шли элементы, не превосходящие опорного, а затем —– большие опорного.

# Затем сортировка вызывается рекурсивно для двух полученных частей. Именно на этапе разделения элементов на группы в обычном алгоритме используется дополнительная память. Теперь разберёмся, как реализовать этот шаг in-place.

# Пусть мы как-то выбрали опорный элемент. Заведём два указателя left и right, которые изначально будут указывать на левый и правый концы отрезка соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он указывает на элемент, меньший опорного. Аналогично двигаем правый указатель влево, пока он стоит на элементе, превосходящем опорный. В итоге окажется, что что левее от left все элементы точно принадлежат первой группе, а правее от right — второй. Элементы, на которых стоят указатели, нарушают порядок. Поменяем их местами (в большинстве языков программирования используется функция swap()) и продвинем указатели на следующие элементы. Будем повторять это действие до тех пор, пока left и right не столкнутся.
# На рисунке представлен пример разделения при pivot=5. Указатель left — голубой, right — оранжевый.

# Формат ввода
# В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
# В каждой из следующих n строк задана информация про одного из участников.
# i-й участник описывается тремя параметрами:

# уникальным логином (строкой из маленьких латинских букв длиной не более 20)
# числом решённых задач Pi
# штрафом Fi
# Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
# Формат вывода
# Для отсортированного списка участников выведите по порядку их логины по одному в строке.


# # ------------------------------
# # 20230529 try1  2error tl
# # ------------------------------

# from operator import gt, eq, lt
# # import random

# def compare_pipl(pipl1,pipl2):
#     pipl1_tasks=int(pipl1[1])
#     pipl2_tasks=int(pipl2[1])
#     pipl1_fine=int(pipl1[2])
#     pipl2_fine=int(pipl2[2])
#     print('pipl1_name=',pipl1[0])
#     print('     pipl1_tasks=',pipl1_tasks)
#     print('         pipl1_fine=',pipl1_fine)
#     print('pipl2_name=',pipl2[0])
#     print('     pipl2_tasks=',pipl2_tasks)
#     print('         pipl2_fine=',pipl2_fine)
#     # if int(pipl1[1]) > int(pipl2[1]):
#     if gt(pipl1_tasks, pipl2_tasks):
#         print('ge(pipl1_tasks, pipl2_tasks)')
#         return True
#     # elif pipl1[1] == pipl2[1]:
#     elif eq(pipl1_tasks, pipl2_tasks):
#         print('eq(pipl1_tasks, pipl2_tasks)')
#         # if pipl1[2] > pipl2[2]:
#         if lt(pipl1_fine, pipl2_fine):
#             print('ge(pipl1_fine, pipl2_fine)')
#             return True
#         # elif pipl1[2] == pipl2[2]:
#         elif eq(pipl1_fine, pipl2_fine):
#             print('eq(pipl1_fine, pipl2_fine)')
#             # if pipl1[2] < pipl2[2]:
#             if lt(pipl1[0], pipl2[0]):
#                 print('lt(pipl1[0], pipl2[0])')
#                 return True
#     print('end false')
#     return False

# # функция partition(array, pivot):
# #     left = элементы array, меньшие pivot
# #     center = элементы array, равные pivot
# #     right = элементы array, большие pivot
# #     return left, center, right

# # функция quicksort(array):
# #     if length(array) < 2:  # базовый случай,
# #         return array       # массивы с 0 или 1 элементами фактически отсортированы
# #     else:  # рекурсивный случай
# #         pivot = случайный элемент из array
# #         left, center, right = partition(array, pivot)
# #         return quicksort(left) + center + quicksort(right)

# def partition(array, pivot):
#     # left = []
#     # # элементы array, меньшие pivot
#     # center =[]
#     # # элементы array, равные pivot
#     # right=[]
#     # # элементы array, большие pivot
#     # for i in array:
#     #     # print('pivot=',pivot)
#     #     # print('arrai[i]=',i)
#     #     if compare_pipl(i, pivot):
#     #     # if i < pivot:
#     #         # print('     left.append(i)')
#     #         left.append(i)
#     #     elif compare_pipl(pivot,i):
#     #     # elif i > pivot:
#     #         # print('     right.append(i)')
#     #         right.append(i)
#     #     else:
#     #     # elif i == pivot:
#     #         # print('     center.append(i)')
#     #         center.append(i)
#     # return left, center, right


#     left = []
#     # элементы array, меньшие pivot
#     center =[]
#     # элементы array, равные pivot
#     right=[]
#     left_index = 0
#     right_index=len(array)-1
#     print('pivot=',pivot)
#     while(left_index<=right_index):
#         print('left_index=',left_index)
#         print('     array[left_index]=',array[left_index])
#         print('right_index=',right_index)
#         print('     array[right_index]=',array[right_index])
#         if compare_pipl(array[left_index], pivot):
#         # if compare_pipl(pivot,array[left_index]):
#             print('     left.append(i)')
#             left.append(array[left_index])
#             left_index+=1
#             print('left=', left)
#         elif compare_pipl(pivot,array[right_index]):
#             print('     right.append(i)')
#             right.append(array[right_index])
#             right_index-=1
#             print('right=', right)
#         elif eq(pivot,array[right_index]):
#             print('     eq right')
#             center.append(pivot)
#             right_index-=1
#             print('center=', center)
#             print('right=', right)
#         elif eq(array[left_index], pivot):
#             print('     eq left')
#             center.append(pivot)
#             left_index+=1
#             print('center=', center)
#             print('left=', left)
#         else:
#             print('     swap')
#             print('left=', left)
#             print('center=', center)
#             print('right=', right)
#             print('left_index=',left_index)
#             print('     array[left_index]=',array[left_index])
#             print('right_index=',right_index)
#             print('     array[right_index]=',array[right_index])
#             left.append(array[right_index])
#             right.append(array[left_index])
#             left_index+=1
#             right_index-=1
#             print('left=', left)
#             print('center=', center)
#             print('right=', right)

#             # tmp=array[left_index]
#             # array[left_index]=array[right_index]
#             # array[right_index]=tmp
#             # # swap(array[left],array[right])
#             # left_index+=1
#             # right_index-=1
    
#     print('end left=', left)
#     print('end center=', center)
#     print('end right=', right)
#     return left, center, right


# def quicksort(array):
#     len_arr=len(array)
#     if  len_arr< 2:  # базовый случай,
#         return array       # массивы с 0 или 1 элементами фактически отсортированы
#     else:  # рекурсивный случай
#         # pivot = random(array)
#         pivot = array[len_arr//2]
#         left, center, right = partition(array, pivot)
#         return quicksort(left) + center + quicksort(right)

# def fast_sort(unsort_list, len_unsort_list):
#     # # result_list=[len_unsort_list]
#     # result_list=[]
#     # for i in range(len_unsort_list):
#     #     print('i=',i)
#     #     # result_list[i]=unsort_list[i]
#     #     result_list.append(unsort_list[i])
#     # return result_list

#     # result_list=[]
#     # for i in range(len_unsort_list):
#     #     # print('i=',i)
#     #     result_list.append(unsort_list[i])

#     #     item_to_insert = unsort_list[i]
#     #     j = i
#     #     while (j > 0 and compare_pipl(item_to_insert, unsort_list[j-1])):
#     #         unsort_list[j] = unsort_list[j-1]
#     #         j -= 1
#     #     unsort_list[j] = item_to_insert

#     # return unsort_list
#     result_list=quicksort(unsort_list)
#     print('result_list=',result_list)
#     return result_list



# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     pipl_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     pipl_list = []
#     for i in range(pipl_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         pipl_list.append(str(file.readline()).rstrip().split())
#     file.close()    

#     # print('begin')
#     # print('pipl_count=', pipl_count)
#     # print('pipl_list=', pipl_list)
#     pipl_sorted=fast_sort(pipl_list,pipl_count)
#     for i in pipl_sorted:
#         print(i[0])


# # ------------------------------
# # 20230529 try2
# # ------------------------------

# from operator import gt, eq, lt
# # import random

# def compare_pipl(pipl1,pipl2):
#     pipl1_tasks=int(pipl1[1])
#     pipl2_tasks=int(pipl2[1])
#     pipl1_fine=int(pipl1[2])
#     pipl2_fine=int(pipl2[2])
#     # print('pipl1_name=',pipl1[0])
#     # print('     pipl1_tasks=',pipl1_tasks)
#     # print('         pipl1_fine=',pipl1_fine)
#     # print('pipl2_name=',pipl2[0])
#     # print('     pipl2_tasks=',pipl2_tasks)
#     # print('         pipl2_fine=',pipl2_fine)
#     # if int(pipl1[1]) > int(pipl2[1]):
#     if gt(pipl1_tasks, pipl2_tasks):
#         # print('ge(pipl1_tasks, pipl2_tasks)')
#         return True
#     # elif pipl1[1] == pipl2[1]:
#     elif eq(pipl1_tasks, pipl2_tasks):
#         # print('eq(pipl1_tasks, pipl2_tasks)')
#         # if pipl1[2] > pipl2[2]:
#         if lt(pipl1_fine, pipl2_fine):
#             # print('ge(pipl1_fine, pipl2_fine)')
#             return True
#         # elif pipl1[2] == pipl2[2]:
#         elif eq(pipl1_fine, pipl2_fine):
#             # print('eq(pipl1_fine, pipl2_fine)')
#             # if pipl1[2] < pipl2[2]:
#             if lt(pipl1[0], pipl2[0]):
#                 # print('lt(pipl1[0], pipl2[0])')
#                 return True
#     # print('end false')
#     return False

# # функция partition(array, pivot):
# #     left = элементы array, меньшие pivot
# #     center = элементы array, равные pivot
# #     right = элементы array, большие pivot
# #     return left, center, right

# # функция quicksort(array):
# #     if length(array) < 2:  # базовый случай,
# #         return array       # массивы с 0 или 1 элементами фактически отсортированы
# #     else:  # рекурсивный случай
# #         pivot = случайный элемент из array
# #         left, center, right = partition(array, pivot)
# #         return quicksort(left) + center + quicksort(right)

# def partition(array, pivot_index,first_index, end_index):
#     print('partition')
#     # left = []
#     # # элементы array, меньшие pivot
#     # center =[]
#     # # элементы array, равные pivot
#     # right=[]
#     # # элементы array, большие pivot
#     # for i in array:
#     #     # print('pivot=',pivot)
#     #     # print('arrai[i]=',i)
#     #     if compare_pipl(i, pivot):
#     #     # if i < pivot:
#     #         # print('     left.append(i)')
#     #         left.append(i)
#     #     elif compare_pipl(pivot,i):
#     #     # elif i > pivot:
#     #         # print('     right.append(i)')
#     #         right.append(i)
#     #     else:
#     #     # elif i == pivot:
#     #         # print('     center.append(i)')
#     #         center.append(i)
#     # return left, center, right


#     # left = []
#     # # элементы array, меньшие pivot
#     # center =[]
#     # # элементы array, равные pivot
#     # right=[]
#     # left_index = 0
#     # right_index=len(array)-1
#     left_index = first_index
#     right_index=end_index
#     pivot=array[pivot_index]
#     print('pivot=',pivot)
#     print('first_index=',first_index)
#     print('end_index=',end_index)
#     print('array=',array)
#     # while(left_index<=right_index):
#     # while(left_index<pivot_index or pivot_index<right_index):
#     while(left_index!=right_index):
#         print('left_index=',left_index)
#         print('     array[left_index]=',array[left_index])
#         print('right_index=',right_index)
#         print('     array[right_index]=',array[right_index])
#         if compare_pipl(array[left_index], pivot):
#         # if compare_pipl(pivot,array[left_index]):
#             print('     left.append(i)')
#             # left.append(array[left_index])
#             left_index+=1
#             # print('left=', left)
#         elif compare_pipl(pivot,array[right_index]):
#             print('     right.append(i)')
#             # right.append(array[right_index])
#             right_index-=1
#             # print('right=', right)
#         elif eq(array[left_index], pivot):
#             print('     eq left')
#             # center.append(pivot)
#             # tmp=array[left_index]
#             array[left_index]=array[right_index]
#             array[right_index]=pivot
#             left_index+=1
#             pivot_index=right_index
#             # print('center=', center)
#             # print('left=', left)
#         elif eq(pivot,array[right_index]):
#             print('     eq right')
#             # center.append(pivot)
#             # tmp=array[left_index]
#             array[right_index]=array[left_index]
#             array[left_index]=pivot
#             right_index-=1
#             pivot_index=left_index
#             # print('center=', center)
#             # print('right=', right)
#         else:
#             print('     swap')
#             # print('left=', left)
#             # print('center=', center)
#             # print('right=', right)
#             print('left_index=',left_index)
#             print('     array[left_index]=',array[left_index])
#             print('right_index=',right_index)
#             print('     array[right_index]=',array[right_index])
#             # left.append(array[right_index])
#             # right.append(array[left_index])
#             # left_index+=1
#             # right_index-=1

#             tmp=array[left_index]
#             array[left_index]=array[right_index]
#             array[right_index]=tmp
#             # swap(array[left],array[right])
#             left_index+=1
#             right_index-=1
#             print('array=',array)
    
#     #         print('left=', left)
#     #         print('center=', center)
#     #         print('right=', right)

#     # print('end left=', left)
#     # print('end center=', center)
#     # print('end right=', right)
#     # return left, center, right
#     print('end part array=',array)
#     return pivot_index


# def quicksort(array,first_index,end_index):
#     print('quicksort')
#     print('first_index=',first_index)
#     print('end_index=',end_index)
#     print('array=',array)
#     # len_arr=len(array)
#     len_arr=end_index - first_index+1
#     half_len_arr=(len_arr//2)+first_index
#     print('half_len_arr=',half_len_arr)
#     if  len_arr< 2:  # базовый случай,
#         return array       # массивы с 0 или 1 элементами фактически отсортированы
#     else:  # рекурсивный случай
#         # pivot = random(array)
#         # pivot = array[half_len_arr]
#         pivot_index=partition(array, half_len_arr,first_index,end_index)
#         quicksort(array, first_index, pivot_index-1)
#         quicksort(array, pivot_index+1,end_index)
#         return
#         # left, center, right = 
#         # return quicksort(left) + center + quicksort(right)

# def fast_sort(unsort_list, len_unsort_list):
#     # result_list=quicksort(unsort_list,0,len_unsort_list-1)
#     # print('result_list=',result_list)
#     # return result_list

#     print('fast_sort')
#     print('unsort_list=',unsort_list)
#     quicksort(unsort_list,0,len_unsort_list-1)
#     print('end unsort_list=',unsort_list)
#     return



# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     pipl_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     pipl_list = []
#     for i in range(pipl_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         pipl_list.append(str(file.readline()).rstrip().split())
#     file.close()    

#     # print('begin')
#     # print('pipl_count=', pipl_count)
#     # print('pipl_list=', pipl_list)
#     # pipl_sorted=fast_sort(pipl_list,pipl_count)
#     # for i in pipl_sorted:
#     #     print(i[0])
#     fast_sort(pipl_list,pipl_count)
#     for i in pipl_list:
#         print(i[0])


# ------------------------------
# 20230529 try3
# ------------------------------

# from operator import gt, eq, lt
# # import random


# # def compare_pipl(pipl1,pipl2):
# #     pipl1_tasks=int(pipl1[1])
# #     pipl2_tasks=int(pipl2[1])
# #     pipl1_fine=int(pipl1[2])
# #     pipl2_fine=int(pipl2[2])
# #     # print('pipl1_name=',pipl1[0])
# #     # print('     pipl1_tasks=',pipl1_tasks)
# #     # print('         pipl1_fine=',pipl1_fine)
# #     # print('pipl2_name=',pipl2[0])
# #     # print('     pipl2_tasks=',pipl2_tasks)
# #     # print('         pipl2_fine=',pipl2_fine)
# #     # if int(pipl1[1]) > int(pipl2[1]):
# #     if gt(pipl1_tasks, pipl2_tasks):
# #         # print('ge(pipl1_tasks, pipl2_tasks)')
# #         return True
# #     # elif pipl1[1] == pipl2[1]:
# #     elif eq(pipl1_tasks, pipl2_tasks):
# #         # print('eq(pipl1_tasks, pipl2_tasks)')
# #         # if pipl1[2] > pipl2[2]:
# #         if lt(pipl1_fine, pipl2_fine):
# #             # print('ge(pipl1_fine, pipl2_fine)')
# #             return True
# #         # elif pipl1[2] == pipl2[2]:
# #         elif eq(pipl1_fine, pipl2_fine):
# #             # print('eq(pipl1_fine, pipl2_fine)')
# #             # if pipl1[2] < pipl2[2]:
# #             if lt(pipl1[0], pipl2[0]):
# #                 # print('lt(pipl1[0], pipl2[0])')
# #                 return True
# #     # print('end false')
# #     return False


# def compare_pipl(pipl1,pipl2):
#     pipl1_tasks=int(pipl1[1])
#     pipl2_tasks=int(pipl2[1])
#     pipl1_fine=int(pipl1[2])
#     pipl2_fine=int(pipl2[2])
#     # print('pipl1_name=',pipl1[0])
#     # print('     pipl1_tasks=',pipl1_tasks)
#     # print('         pipl1_fine=',pipl1_fine)
#     # print('pipl2_name=',pipl2[0])
#     # print('     pipl2_tasks=',pipl2_tasks)
#     # print('         pipl2_fine=',pipl2_fine)
#     # if int(pipl1[1]) > int(pipl2[1]):
#     # if gt(pipl1_tasks, pipl2_tasks):
#     if (pipl1_tasks > pipl2_tasks):
#         # print('ge(pipl1_tasks, pipl2_tasks)')
#         return True
#     # elif pipl1[1] == pipl2[1]:
#     # elif eq(pipl1_tasks, pipl2_tasks):
#     elif (pipl1_tasks == pipl2_tasks):
#         # print('eq(pipl1_tasks, pipl2_tasks)')
#         # if pipl1[2] > pipl2[2]:
#         # if lt(pipl1_fine, pipl2_fine):
#         if (pipl1_fine < pipl2_fine):
#             # print('ge(pipl1_fine, pipl2_fine)')
#             return True
#         # elif pipl1[2] == pipl2[2]:
#         # elif eq(pipl1_fine, pipl2_fine):
#         elif (pipl1_fine== pipl2_fine):
#             # print('eq(pipl1_fine, pipl2_fine)')
#             # if pipl1[2] < pipl2[2]:
#             # if lt(pipl1[0], pipl2[0]):
#             if (pipl1[0]< pipl2[0]):
#                 # print('lt(pipl1[0], pipl2[0])')
#                 return True
#     # print('end false')
#     return False


# # функция partition(array, pivot):
# #     left = элементы array, меньшие pivot
# #     center = элементы array, равные pivot
# #     right = элементы array, большие pivot
# #     return left, center, right

# # функция quicksort(array):
# #     if length(array) < 2:  # базовый случай,
# #         return array       # массивы с 0 или 1 элементами фактически отсортированы
# #     else:  # рекурсивный случай
# #         pivot = случайный элемент из array
# #         left, center, right = partition(array, pivot)
# #         return quicksort(left) + center + quicksort(right)


# # def swapList(arr, index1, index2):
# #     arr[index1], arr[index2] = arr[index2], arr[index1]
# #     return


# def partition(array, pivot_index,first_index, end_index):
#     print('partition')
#     # left = []
#     # # элементы array, меньшие pivot
#     # center =[]
#     # # элементы array, равные pivot
#     # right=[]
#     # # элементы array, большие pivot
#     # for i in array:
#     #     # print('pivot=',pivot)
#     #     # print('arrai[i]=',i)
#     #     if compare_pipl(i, pivot):
#     #     # if i < pivot:
#     #         # print('     left.append(i)')
#     #         left.append(i)
#     #     elif compare_pipl(pivot,i):
#     #     # elif i > pivot:
#     #         # print('     right.append(i)')
#     #         right.append(i)
#     #     else:
#     #     # elif i == pivot:
#     #         # print('     center.append(i)')
#     #         center.append(i)
#     # return left, center, right


#     # left = []
#     # # элементы array, меньшие pivot
#     # center =[]
#     # # элементы array, равные pivot
#     # right=[]
#     # left_index = 0
#     # right_index=len(array)-1
#     left_index = first_index
#     right_index=end_index
#     pivot=array[pivot_index]
#     print('pivot=',pivot)
#     print('first_index=',first_index)
#     print('end_index=',end_index)
#     print('array=',array)
#     # while(left_index<=right_index):
#     # while(left_index<pivot_index or pivot_index<right_index):
#     while(left_index!=right_index):
#         print('left_index=',left_index)
#         print('     array[left_index]=',array[left_index])
#         print('right_index=',right_index)
#         print('     array[right_index]=',array[right_index])
#         if compare_pipl(array[left_index], pivot):
#         # if compare_pipl(pivot,array[left_index]):
#             print('     left.append(i)')
#             # left.append(array[left_index])
#             left_index+=1
#             # print('left=', left)
#         elif compare_pipl(pivot,array[right_index]):
#             print('     right.append(i)')
#             # right.append(array[right_index])
#             right_index-=1
#             # print('right=', right)
#         elif eq(array[left_index], pivot):
#             print('     eq left')
#             # center.append(pivot)
#             # tmp=array[left_index]
#             # swapList(array, right_index, left_index):
#             array[left_index]=array[right_index]
#             array[right_index]=pivot
#             left_index+=1
#             pivot_index=right_index
#             # print('center=', center)
#             # print('left=', left)
#         elif eq(pivot,array[right_index]):
#             print('     eq right')
#             # center.append(pivot)
#             # tmp=array[left_index]
#             # swapList(array, right_index, left_index):
#             array[right_index]=array[left_index]
#             array[left_index]=pivot
#             right_index-=1
#             pivot_index=left_index
#             # print('center=', center)
#             # print('right=', right)
#         else:
#             print('     swap')
#             # print('left=', left)
#             # print('center=', center)
#             # print('right=', right)
#             print('left_index=',left_index)
#             print('     array[left_index]=',array[left_index])
#             print('right_index=',right_index)
#             print('     array[right_index]=',array[right_index])
#             # left.append(array[right_index])
#             # right.append(array[left_index])
#             # left_index+=1
#             # right_index-=1

#             # swapList(array, right_index, left_index):

#             tmp=array[left_index]
#             array[left_index]=array[right_index]
#             array[right_index]=tmp
#             # swap(array[left],array[right])
#             left_index+=1
#             right_index-=1
#             print('array=',array)
    
#     #         print('left=', left)
#     #         print('center=', center)
#     #         print('right=', right)

#     # print('end left=', left)
#     # print('end center=', center)
#     # print('end right=', right)
#     # return left, center, right
#     print('end part array=',array)
#     return pivot_index


# def quicksort(array,first_index,end_index):
#     print('quicksort')
#     print('first_index=',first_index)
#     print('end_index=',end_index)
#     print('array=',array)
#     # len_arr=len(array)
#     len_arr=end_index - first_index+1
#     half_len_arr=(len_arr//2)+first_index
#     print('half_len_arr=',half_len_arr)
#     if  len_arr< 2:  # базовый случай,
#         return array       # массивы с 0 или 1 элементами фактически отсортированы
#     else:  # рекурсивный случай
#         # pivot = random(array)
#         # pivot = array[half_len_arr]
#         pivot_index=partition(array, half_len_arr,first_index,end_index)
#         quicksort(array, first_index, pivot_index-1)
#         quicksort(array, pivot_index+1,end_index)
#         return
#         # left, center, right = 
#         # return quicksort(left) + center + quicksort(right)

# def fast_sort(unsort_list, len_unsort_list):
#     # result_list=quicksort(unsort_list,0,len_unsort_list-1)
#     # print('result_list=',result_list)
#     # return result_list

#     print('fast_sort')
#     print('unsort_list=',unsort_list)
#     quicksort(unsort_list,0,len_unsort_list-1)
#     print('end unsort_list=',unsort_list)
#     return



# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     pipl_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     pipl_list = []
#     for i in range(pipl_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         pipl_list.append(str(file.readline()).rstrip().split())
#     file.close()    

#     # print('begin')
#     # print('pipl_count=', pipl_count)
#     # print('pipl_list=', pipl_list)
#     # pipl_sorted=fast_sort(pipl_list,pipl_count)
#     # for i in pipl_sorted:
#     #     print(i[0])
#     fast_sort(pipl_list,pipl_count)
#     for i in pipl_list:
#         print(i[0])










#    def __init__(self, name: str, solved: str, penalty: str) -> None:
#         self.name: str = name
#         self.solved: int = int(solved)
#         self.penalty: int = int(penalty)



# from dataclasses import dataclass
# from typing import List


# # id = 87563686


# @dataclass
# class Competitor:
#     name: str
#     solved: int
#     penalties: int

#     def __str__(self) -> str:
#         return self.name

#     def __lt__(self, other):
#         return (
#             (-int(self.solved), int(self.penalties), self.name)
#             < (-int(other.solved), int(other.penalties), other.name)
#         )


# def effective_quick_sort(
#     competitors: List[Competitor], start: int = 0, end: int = None
# ) -> int:
#     if not end:
#         end = len(competitors) - 1
#     if start >= end:
#         return -1
#     left = start
#     right = end
#     pivot = competitors[(start + end) // 2]
#     while left <= right:
#         while competitors[left] < pivot:
#             left += 1
#         while competitors[right] > pivot:
#             right -= 1
#         if left <= right:
#             competitors[left], competitors[right] = competitors[right], competitors[left]
#             left += 1
#             right -= 1
#     effective_quick_sort(competitors, start, right)
#     effective_quick_sort(competitors, left, end)


# def read_input() -> List[Competitor]:
#     quantity = int(input())
#     users = [Competitor(*input().split()) for _ in range(quantity)]
#     return users


# def main():
#     users = read_input()
#     effective_quick_sort(users)
#     print(*users, sep='\n')


# if __name__ == '__main__':
#     main()







# # ------------------------------
# # 20230529 try4
# # ------------------------------

# from operator import gt, eq, lt

# def compare_pipl(pipl1,pipl2):
#     pipl1_tasks=int(pipl1[1])
#     pipl2_tasks=int(pipl2[1])
#     pipl1_fine=int(pipl1[2])
#     pipl2_fine=int(pipl2[2])
#     if (pipl1_tasks > pipl2_tasks):
#         return True
#     elif (pipl1_tasks == pipl2_tasks):
#         if (pipl1_fine < pipl2_fine):
#             return True
#         elif (pipl1_fine== pipl2_fine):
#             if (pipl1[0]< pipl2[0]):
#                 return True
#     return False

# def partition(array, pivot_index,first_index, end_index):
#     left_index = first_index
#     right_index=end_index
#     pivot=array[pivot_index]
#     while(left_index!=right_index):
#         if compare_pipl(array[left_index], pivot):
#             left_index+=1
#         elif compare_pipl(pivot,array[right_index]):
#             right_index-=1
#         elif eq(array[left_index], pivot):
#             array[left_index]=array[right_index]
#             array[right_index]=pivot
#             left_index+=1
#             pivot_index=right_index
#         elif eq(pivot,array[right_index]):
#             array[right_index]=array[left_index]
#             array[left_index]=pivot
#             right_index-=1
#             pivot_index=left_index
#         else:
#             tmp=array[left_index]
#             array[left_index]=array[right_index]
#             array[right_index]=tmp
#             left_index+=1
#             right_index-=1
#     return pivot_index


# def quicksort(array,first_index,end_index):
#     len_arr=end_index - first_index+1
#     half_len_arr=(len_arr//2)+first_index
#     if  len_arr< 2:  # базовый случай,
#         return array       # массивы с 0 или 1 элементами фактически отсортированы
#     else:  # рекурсивный случай
#         pivot_index=partition(array, half_len_arr,first_index,end_index)
#         quicksort(array, first_index, pivot_index-1)
#         quicksort(array, pivot_index+1,end_index)
#         return

# def fast_sort(unsort_list, len_unsort_list):
#     quicksort(unsort_list,0,len_unsort_list-1)
#     return



# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     pipl_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     pipl_list = []
#     for i in range(pipl_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         pipl_list.append(str(file.readline()).rstrip().split())
#     file.close()    
#     fast_sort(pipl_list,pipl_count)
#     for i in pipl_list:
#         print(i[0])




# ------------------------------
# 20230529 try5 ok
# ------------------------------

# from operator import gt, eq, lt


# class pipl:
#     def __init__(self, name: str, tasks: str, tickets: str) -> None:
#             self.name: str = name
#             self.tasks: int = int(tasks)
#             self.tickets: int = int(tickets)

#     def __str__(self):
#         # return ' '.join(str(x) for x in self.cells)
#         return self.name

# def compare_pipl(pipl1,pipl2):
#     # pipl1_tasks=int(pipl1[1])
#     # pipl2_tasks=int(pipl2[1])
#     # pipl1_fine=int(pipl1[2])
#     # pipl2_fine=int(pipl2[2])
#     pipl1_tasks=pipl1.tasks
#     pipl2_tasks=pipl2.tasks
#     pipl1_fine=pipl1.tickets
#     pipl2_fine=pipl2.tickets
#     if (pipl1_tasks > pipl2_tasks):
#         return True
#     elif (pipl1_tasks == pipl2_tasks):
#         if (pipl1_fine < pipl2_fine):
#             return True
#         elif (pipl1_fine== pipl2_fine):
#             if (pipl1.name< pipl2.name):
#                 return True
#     return False

# def partition(array, pivot_index,first_index, end_index):
#     left_index = first_index
#     right_index=end_index
#     pivot=array[pivot_index]
#     while(left_index!=right_index):
#         if compare_pipl(array[left_index], pivot):
#             left_index+=1
#         elif compare_pipl(pivot,array[right_index]):
#             right_index-=1
#         # elif eq(array[left_index], pivot):
#         elif array[left_index]== pivot:
#             array[left_index]=array[right_index]
#             array[right_index]=pivot
#             left_index+=1
#             pivot_index=right_index
#         # elif eq(pivot,array[right_index]):
#         elif array[right_index]==pivot:
#             array[right_index]=array[left_index]
#             array[left_index]=pivot
#             right_index-=1
#             pivot_index=left_index
#         else:
#             tmp=array[left_index]
#             array[left_index]=array[right_index]
#             array[right_index]=tmp
#             left_index+=1
#             right_index-=1
#     return pivot_index


# def quicksort(array,first_index,end_index):
#     len_arr=end_index - first_index+1
#     half_len_arr=(len_arr//2)+first_index
#     if  len_arr< 2:  # базовый случай,
#         return array       # массивы с 0 или 1 элементами фактически отсортированы
#     else:  # рекурсивный случай
#         pivot_index=partition(array, half_len_arr,first_index,end_index)
#         quicksort(array, first_index, pivot_index-1)
#         quicksort(array, pivot_index+1,end_index)
#         return

# def fast_sort(unsort_list, len_unsort_list):
#     quicksort(unsort_list,0,len_unsort_list-1)
#     return


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     pipl_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     pipl_list = []
#     for i in range(pipl_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         # tmp_input=str(file.readline()).rstrip().split()
#         # print('tmp_input=',tmp_input)
#         # pipl_list.append(pipl(tmp_input[0],tmp_input[1],tmp_input[2]))
#         pipl_list.append(pipl(*str(file.readline()).rstrip().split()))
#     file.close()
#     # print('pipl_list=',pipl_list)
#     # for i in pipl_list:
#     #     print(i)
#     #     # print(i.name)

#     fast_sort(pipl_list,pipl_count)
#     for i in pipl_list:
#         print(i)

# # # ------------------------------
# # # 20230531 work rev1
# # # ------------------------------

# # 87836688

# def compare_competitors(first, second):
#     first_tasks = first[1]
#     second_tasks = second[1]
#     first_fine = first[2]
#     second_fine = second[2]
#     if (first_tasks > second_tasks):
#         return True
#     elif (first_tasks == second_tasks):
#         if (first_fine < second_fine):
#             return True
#         elif (first_fine == second_fine):
#             if (first[0] < second[0]):
#                 return True
#     return False


# def partition(array, pivot_index, first_index, end_index):
#     left_index = first_index
#     right_index = end_index
#     pivot = array[pivot_index]
#     while left_index != right_index:
#         if compare_competitors(array[left_index], pivot):
#             left_index += 1
#         elif compare_competitors(pivot, array[right_index]):
#             right_index -= 1
#         elif array[left_index] == pivot:
#             array[left_index] = array[right_index]
#             array[right_index] = pivot
#             left_index += 1
#             pivot_index = right_index
#         elif array[right_index] == pivot:
#             array[right_index] = array[left_index]
#             array[left_index] = pivot
#             right_index -= 1
#             pivot_index = left_index
#         else:
#             tmp = array[left_index]
#             array[left_index] = array[right_index]
#             array[right_index] = tmp
#             left_index += 1
#             right_index -= 1
#     return pivot_index


# def quicksort(array, first_index, end_index):
#     len_indexes = end_index - first_index + 1
#     half_len_indexes = (len_indexes // 2) + first_index
#     if len_indexes < 2:
#         # базовый случай,
#         return array
#         # массивы с 0 или 1 элементами фактически отсортированы
#     else:
#         # рекурсивный случай
#         pivot_index = partition(
#             array, half_len_indexes, first_index, end_index
#         )
#         quicksort(array, first_index, pivot_index - 1)
#         quicksort(array, pivot_index + 1, end_index)
#         return

# # def fast_sort(unsort_list, len_unsort_list):
# #     quicksort(unsort_list,0,len_unsort_list-1)
# #     return

# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     competitors_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#     competitors_list = []
#     for i in range(competitors_count):
#         # pipl_list.append(str(file.readline()).rstrip())
#         tmp_input = str(file.readline()).rstrip().split()
#         # print('tmp_input=',tmp_input)
#         competitors_list.append(
#             [tmp_input[0], int(tmp_input[1]), int(tmp_input[2])]
#         )
#         # pipl_list.append()
#     file.close()
#     # print('pipl_list=',pipl_list)
#     quicksort(competitors_list, 0, competitors_count - 1)
#     for i in competitors_list:
#         print(i[0])


# # ------------------------------
# # 20230607 try5 ok
# # ------------------------------

# # from operator import gt, eq, lt

# # 87836858

# class Competitor:
#     def __init__(self, name: str, tasks: str, tickets: str) -> None:
#             self.name: str = name
#             self.tasks: int = int(tasks)
#             self.tickets: int = int(tickets)

#     def __str__(self):
#         # return ' '.join(str(x) for x in self.cells)
#         return self.name

#     # def __lt__(self, other):
#     #     first_tasks = self.tasks
#     #     second_tasks = other.tasks
#     #     first_fine = self.tickets
#     #     second_fine = other.tickets
#     #     if (first_tasks > second_tasks):
#     #         return True
#     #     elif (first_tasks == second_tasks):
#     #         if (first_fine < second_fine):
#     #             return True
#     #         elif (first_fine == second_fine):
#     #             if (self.name < other.name):
#     #                 return True
#     #     return False        


#     def __lt__(self, other):
#         # first_tasks = self.tasks
#         # second_tasks = other.tasks
#         # first_fine = self.tickets
#         # second_fine = other.tickets
#         if (self.tasks > other.tasks):
#             return True
#         elif (self.tasks == other.tasks):
#             if (self.tickets < other.tickets):
#                 return True
#             elif (self.tickets == other.tickets):
#                 if (self.name < other.name):
#                     return True
#         return False        

#     # def __lt__(self, other):
#     #     if not isinstance(other, (int, Clock)):
#     #         raise TypeError("Операнд справа должен иметь тип int или Clock")
 
#     #     sc = other if isinstance(other, int) else other.seconds
#     #     return self.seconds < sc

# # def compare_competitors(first, second):
# #     first_tasks = first[1]
# #     second_tasks = second[1]
# #     first_fine = first[2]
# #     second_fine = second[2]
# #     if (first_tasks > second_tasks):
# #         return True
# #     elif (first_tasks == second_tasks):
# #         if (first_fine < second_fine):
# #             return True
# #         elif (first_fine == second_fine):
# #             if (first[0] < second[0]):
# #                 return True
# #     return False


# # def partition(array, pivot_index, first_index, end_index):
# def partition(array, first_index, end_index):
#     len_indexes = end_index - first_index + 1
#     pivot_index = (len_indexes // 2) + first_index
#     left_index = first_index
#     right_index = end_index
#     pivot = array[pivot_index]
#     while left_index != right_index:
#         # if compare_competitors(array[left_index], pivot):
#         if array[left_index] < pivot:
#             left_index += 1
#         # elif compare_competitors(pivot, array[right_index]):
#         elif pivot < array[right_index]:
#             right_index -= 1
#         elif array[left_index] == pivot:
#             array[left_index] = array[right_index]
#             array[right_index] = pivot
#             left_index += 1
#             pivot_index = right_index
#         elif array[right_index] == pivot:
#             array[right_index] = array[left_index]
#             array[left_index] = pivot
#             right_index -= 1
#             pivot_index = left_index
#         else:
#             tmp = array[left_index]
#             array[left_index] = array[right_index]
#             array[right_index] = tmp
#             left_index += 1
#             right_index -= 1
#     return pivot_index


# def quicksort(array, first_index, end_index):
#     len_indexes = end_index - first_index + 1
#     # half_len_indexes = (len_indexes // 2) + first_index
#     if len_indexes < 2:
#         # базовый случай,
#         return array
#         # массивы с 0 или 1 элементами фактически отсортированы
#     else:
#         # рекурсивный случай
#         pivot_index = partition(
#             # array, half_len_indexes, first_index, end_index
#             array, first_index, end_index
#         )
#         quicksort(array, first_index, pivot_index - 1)
#         quicksort(array, pivot_index + 1, end_index)
#         return


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке задано число участников n
#     competitors_count = int(file.readline())
#     #  В каждой из следующих n строк задана информация про одного из участников.
#     # i-й участник описывается тремя параметрами:

#     # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
#     # числом решённых задач Pi
#     # штрафом Fi
#     # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
#     competitors_list = []
#     for i in range(competitors_count):
#         competitors_list.append(
#             Competitor(*str(file.readline()).rstrip().split())
#         )
#     file.close()
#     quicksort(competitors_list, 0, competitors_count - 1)
#     for i in competitors_list:
#         print(i)

# ------------------------------
# 20230622
# ------------------------------

# 87836858

class Competitor:
    def __init__(self, name: str, tasks: str, tickets: str) -> None:
        self.name: str = name
        self.tasks: int = int(tasks)
        self.tickets: int = int(tickets)

    def __str__(self):
        # return ' '.join(str(x) for x in self.cells)
        return self.name

    def __lt__(self, other):
        if (self.tasks > other.tasks):
            return True
        elif (self.tasks == other.tasks):
            if (self.tickets < other.tickets):
                return True
            elif (self.tickets == other.tickets):
                if (self.name < other.name):
                    return True
        return False


def partition(array, left_index, right_index):
    # print('begin partition')
    # print('1 left_index=', left_index)
    # print('1 right_index=', right_index)

    len_indexes = right_index - left_index + 1
    pivot_index = (len_indexes // 2) + left_index
    pivot = array[pivot_index]

    # pivot = array[(right_index - left_index) // 2]

    while left_index < right_index:
        # print('2    left_index=', left_index)
        # print('2    right_index=', right_index)
        # print('2    pivot=', pivot)
        # print('2    pivot_index=', pivot_index)
        while array[left_index] < pivot:
            # print('3   while array[left_index]     left_index=', left_index)
            # print('3   while array[left_index]     array[left_index]=', array[left_index])
            left_index += 1
        while pivot < array[right_index]:
            # print('3   while array[right_index]     right_index=', right_index)
            # print('3   while array[right_index]     array[right_index]=', array[right_index])
            right_index -= 1

        # print('4       left_index=', left_index)
        # print('4       array[left_index]=', array[left_index])
        # print('4       right_index=', right_index)
        # print('4       array[right_index]=', array[right_index])

        if left_index >= right_index:
            # print('6    return   right_index=', right_index)
            return right_index

        # print('5   swap     left_index=', left_index)
        # print('5   swap     array[left_index]=', array[left_index])
        # print('5   swap     right_index=', right_index)
        # print('5   swap    array[right_index]=', array[right_index])

        array[left_index], array[right_index] = (
            array[right_index], array[left_index]
        )
        # tmp = array[left_index]
        # array[left_index] = array[right_index]
        # array[right_index] = tmp




# def quicksort(array, first_index, end_index):
#     # print('0   quicksort     array=', array)
#     print('0   quicksort     first_index=', first_index)
#     print('0   quicksort     end_index=', end_index)
#     if first_index  >= end_index:
#         return
#     pivot_index = partition(
#         array, first_index, end_index
#     )
#     # quicksort(array, first_index, pivot_index)
#     quicksort(array, first_index, pivot_index - 1)
#     quicksort(array, pivot_index + 1, end_index)
#     return

# def quicksort(array, first_index, end_index):
#     pivot_index = partition(
#         array, first_index, end_index
#     )
#     quicksort(array, first_index, pivot_index-1)
#     # quicksort(array, first_index, pivot_index - 1)
#     quicksort(array, pivot_index + 1, end_index)
#     return

def quicksort(array, first_index, end_index):
    len_indexes = end_index - first_index + 1
    if len_indexes < 2:
        return
    else:
        pivot_index = partition(
            array, first_index, end_index
        )
        quicksort(array, first_index, pivot_index - 1)
        quicksort(array, pivot_index + 1, end_index)
        return


if __name__ == '__main__':
    file = open("input.txt", "r")
    # В первой строке задано число участников n
    competitors_count = int(file.readline())
    #  В каждой из следующих n строк задана информация про одного из участников.
    # i-й участник описывается тремя параметрами:

    # уникальным логином (строкой из маленьких латинских букв длиной не более 20)
    # числом решённых задач Pi
    # штрафом Fi
    # Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
    competitors_list = []
    for i in range(competitors_count):
        competitors_list.append(
            Competitor(*str(file.readline()).rstrip().split())
        )
    file.close()
    quicksort(competitors_list, 0, competitors_count - 1)
    for i in competitors_list:
        print(i)
