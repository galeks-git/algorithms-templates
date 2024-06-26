# https://contest.yandex.ru/contest/24735/problems/

# A. Поиск в сломанном массиве
# Все языки	Make
# Ограничение времени	0.001 секунда	1.5 секунд
# Ограничение памяти	64Mb	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности. Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за 
# O
# (
# log
# n
# )
# .
# Можно предполагать, что в массиве только уникальные элементы.
# Задачу необходимо сдавать с компилятором Make, он выбран по умолчанию, других компиляторов в задаче нет. Решение отправляется файлом. Требуемые сигнатуры функций лежат в заготовках кода на диске.

# От вас требуется реализовать функцию, осуществляющую поиск в сломанном массиве. Файлы с заготовками кода, содержащими сигнатуры функций и базовый тест для поддерживаемых языков, находятся на Яндекс.Диске по ссылке. Обратите внимание, что считывать данные и выводить ответ не требуется.
# Расширение файла должно соответствовать языку, на котором вы пишете (.cpp, .java, .go, .js, .py). Если вы пишете на Java, назовите файл с решением Solution.java, для C# – Solution.cs. Для остальных языков название может быть любым, кроме solution.ext, где ext – разрешение для вашего языка.

# Формат ввода
# Функция принимает массив натуральных чисел и искомое число 
# k
# . Длина массива не превосходит 
# 1
# 0
# 0
# 0
# 0
# . Элементы массива и число 
# k
#  не превосходят по значению 
# 1
# 0
# 0
# 0
# 0
# .
# В примерах:
# В первой строке записано число 
# n
#  –— длина массива.
# Во второй строке записано положительное число 
# k
#  –— искомый элемент. 
# Далее в строку через пробел записано 
# n
#  натуральных чисел – элементы массива.

# Формат вывода
# Функция должна вернуть индекс элемента, равного 
# k
# , если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть 
# −
# 1
# .
# Изменять массив нельзя.
# Для отсечения неэффективных решений ваша функция будет запускаться от 
# 1
# 0
# 0
# 0
# 0
# 0
#  до 
# 1
# 0
# 0
# 0
# 0
# 0
# 0
#  раз.

# 87465081

# ------------------------------
# 20230526 try1
# ------------------------------

# def binarySearch(arr, x, left, right) -> int:
#     if right <= left: # промежуток пуст
#         return -1
#     # промежуток не пуст
#     mid = (left + right) // 2
#     if arr[mid] == x: # центральный элемент — искомый
#         return mid
#     elif x < arr[mid]: # искомый элемент меньше центрального
#                        # значит следует искать в левой половине
#         return binarySearch(arr, x, left, mid)
#     else: # иначе следует искать в правой половине
#         return binarySearch(arr, x, mid + 1, right)


# def find_broken(array, find_target) -> int:
#     print('begin find_broken')

#     if array[0]==find_target:
#         return 0
#     if array[-1]==find_target:
#         return len(array)-1

#     len_array= len(array)
#     half_len_array= len_array // 2
#     print("1 array=", array)
#     print("1 len_array=", len_array)
#     print("1 find_target=", find_target)
#     print("1 half_len_array=", half_len_array)
#     print("1 array[0]=", array[0])
#     print("1 array[half_len_array]=", array[half_len_array])
#     print("1 array[-1]=", array[-1])

#     if len_array in [1,2,3,4]:
#         print('len_array in [1,2,3,4]')
#         for i in range(len_array):
#             print("1234 find_target=", find_target)
#             print("1234 array[i]=", array[i])
#             print("1234 i=", i)
#             if array[i]==find_target:
#                 print("1234 if i=", i)
#                 return i
#         return -1


#     if array[0] < array[-1]:
#         if array[0] < find_target < array[-1]:
#             find_target_index = binarySearch(array, find_target, 0, len_array)
#             if find_target_index != -1:
#                 return find_target_index
#     #         # if array[half_len_array] < find_target:
#     #         #     find_target=find_broken(array[half_len_array : -1], find_target)
#     #         # else:
#     #         #     find_target=find_broken(array[0 : half_len_array], find_target)
#         else:
#             return -1
#     else:
#         find_target_index=find_broken(array[0 : half_len_array], find_target)
#         if find_target_index != -1:
#             return find_target_index
#         find_target_index=find_broken(array[half_len_array : len_array], find_target)
#         if find_target_index != -1:
#             find_target_index+=half_len_array
#             return find_target_index
#     return find_target_index

#         # if array[0] < array[-1]:
#         #     if array[0] < find_target < array[-1]:
#         #         if array[half_len_array] < find_target:
#         #             find_target=find_broken(array[half_len_array : -1], find_target)
#         #         else:
#         #             find_target=find_broken(array[0 : half_len_array], find_target)
#         #     else:
#         #         pass

#         # if array[0] < array[half_len_array]:
#         # xvxcvx



#     # if array[0] < find_target < array[len_array]:
#     #     if array[half_len_array] < find_target:
#     #         find_target=find_broken(array[half_len_array : len_array], find_target)
#     #     else:
#     #         find_target=find_broken(array[0 : half_len_array], find_target)
#     # else:
#     #     if array[0] < array[half_len_array]:
#     #     xvxcvx



#     # if array[half_len_array] < find_target:
#     #     find_broken(array[half_len_array : len_array], find_target)
#     # # if  len_array== 1:  # базовый случай рекурсии
#     # #     return array
    

#     # # запускаем сортировку рекурсивно на левой половине
#     # left = merge_sort(array[0 : len(array)/2])

#     # # запускаем сортировку рекурсивно на правой половине
#     # right = merge_sort(array[len(array)/2 : len(array)])



# def broken_search(nums, target) -> int:
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     print('begin broken_search')
#     print("1 nums=", nums)
#     print("1 target=", target)
#     # len_nums=len(nums)
#     target_index = find_broken(nums, target)
#     return target_index

#     # for i in range(len_nums):
#     #     if nums[i]==target:
#     #         return i
#     # return -1


# # def test():
# #     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
# #     assert broken_search(arr, 5) == 6


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     find_it = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     print('begin')
#     find_it_index = broken_search(input_array, find_it)
#     print(find_it_index)







# ------------------------------
# 20230526 try2
# ------------------------------

# def binarySearch(arr, x, left, right) -> int:
#     if right <= left: # промежуток пуст
#         return -1
#     # промежуток не пуст
#     mid = (left + right) // 2
#     if arr[mid] == x: # центральный элемент — искомый
#         return mid
#     elif x < arr[mid]: # искомый элемент меньше центрального
#                        # значит следует искать в левой половине
#         return binarySearch(arr, x, left, mid)
#     else: # иначе следует искать в правой половине
#         return binarySearch(arr, x, mid + 1, right)

# def broken_search(array, find_target) -> int:
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     # print('begin broken_search')
#     # print("1 nums=", nums)
#     # print("1 target=", target)
#     # # len_nums=len(nums)
#     # target_index = find_broken(nums, target)
#     # return target_index

# # def find_broken(array, find_target) -> int:
# #     print('begin find_broken')

#     if array[0]==find_target:
#         return 0
#     if array[-1]==find_target:
#         return len(array)-1

#     len_array= len(array)
#     half_len_array= len_array // 2
#     print("1 array=", array)
#     print("1 len_array=", len_array)
#     print("1 find_target=", find_target)
#     print("1 half_len_array=", half_len_array)
#     print("1 array[0]=", array[0])
#     print("1 array[half_len_array]=", array[half_len_array])
#     print("1 array[-1]=", array[-1])

#     if len_array in [1,2,3,4]:
#         print('len_array in [1,2,3,4]')
#         for i in range(len_array):
#             print("1234 find_target=", find_target)
#             print("1234 array[i]=", array[i])
#             print("1234 i=", i)
#             if array[i]==find_target:
#                 print("1234 if i=", i)
#                 return i
#         return -1


#     if array[0] < array[-1]:
#         if array[0] < find_target < array[-1]:
#             find_target_index = binarySearch(array, find_target, 0, len_array)
#             if find_target_index != -1:
#                 return find_target_index
#         else:
#             return -1
#     else:
#         find_target_index=broken_search(array[0 : half_len_array], find_target)
#         if find_target_index != -1:
#             return find_target_index
#         find_target_index=broken_search(array[half_len_array : len_array], find_target)
#         if find_target_index != -1:
#             find_target_index+=half_len_array
#             return find_target_index
#     return find_target_index



# # def test():
# #     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
# #     assert broken_search(arr, 5) == 6


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     find_it = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     print('begin')
#     find_it_index = broken_search(input_array, find_it)
#     print(find_it_index)


# # ------------------------------
# # 20230531
# # ------------------------------


# # def binarySearch(array, target, left_index, right_index) -> int:
# #     # print('begin binarySearch')
# #     if right_index <= left_index:
# #         # промежуток пуст
# #         return -1
# #     # промежуток не пуст
# #     middle_index = (left_index + right_index) // 2
# #     if array[middle_index] == target:
# #         # центральный элемент — искомый
# #         return middle_index
# #     if target < array[middle_index]:
# #         # искомый элемент меньше центрального
# #         # значит следует искать в левой половине
# #         return binarySearch(array, target, left_index, middle_index)
# #     return binarySearch(array, target, middle_index + 1, right_index)

# # 87785174

# def binarySearch(array, target, left_index, right_index) -> int:
#     # print('begin binarySearch')
#     while right_index > left_index:
#         middle_index = (left_index + right_index) // 2
#         if array[middle_index] == target:
#             # центральный элемент — искомый
#             return middle_index
#         if target < array[middle_index]:
#             # искомый элемент меньше центрального
#             # значит следует искать в левой половине
#             right_index = middle_index
#         else:
#             left_index = middle_index + 1
#     return -1


# # def find_broken(array, find_target) -> int:
# def brokenSearch(array, target, start_index, end_index) -> int:
#     # print('begin find_broken')

#     if array[start_index] == target:
#         return start_index
#     if array[end_index] == target:
#         return end_index

#     len_indexes = end_index-start_index + 1
#     if len_indexes < 3:
#         return -1
#     half_len_indexes = (len_indexes // 2) + start_index
#     # str_arr=[]
#     # for i in range(start_index, end_index+1):
#     #     str_arr.append(array[i])
#     # print("1 array=", str_arr)
#     # print("1 start_index=", start_index)
#     # print("1  end_index=", end_index)
#     # print("1        find_target=", find_target)
#     # print("1  half_len_array=", half_len_array)
#     # print("1   len_array=", len_array)
#     # print("1 array[start_index]=", array[start_index])
#     # print("1  array[half_len_array]=", array[half_len_array])
#     # print("1   array[end_index]=", array[end_index])

#     # if len_indexes < 5:
#     #     # print('len_array in [1,2,3,4]')
#     #     for i in range(start_index, end_index + 1):
#     #         # print("1234 find_target=", find_target)
#     #         # print("1234 array[i]=", array[i])
#     #         # print("1234 i=", i)
#     #         if array[i] == target:
#     #             # print("1234 if i=", i)
#     #             return i
#     #     return -1

#     if array[start_index] < array[end_index]:
#         # print('if array[start_index] < array[end_index]:')
#         if array[start_index] < target < array[end_index]:
#             # print('if array[start_index] << find_target <  array[end_index]:')
#             target_index = binarySearch(
#                 array, target, start_index, end_index
#             )
#             if target_index != -1:
#                 return target_index
#         else:
#             # print('else array[start_index] << find_target <  array[end_index]:')
#             return -1
#     else:
#         # print('2 left find_target_index begin')
#         # print("2 left    start_index=", start_index)
#         # print("2 left     half_len_array=", half_len_array)
#         target_index = brokenSearch(
#             array, target, start_index, half_len_indexes - 1
#         )
#         # print('2 left find_target_index=', find_target_index)

#         if target_index != -1:
#             # print('3  end left find_target_index=', find_target_index)
#             return target_index

#         # print('2 right find_target_index begin')
#         # print("2 r    half_len_array=", half_len_array)
#         # print("2 r     end_index=", end_index)
#         target_index = brokenSearch(
#             array, target, half_len_indexes, end_index - 1
#         )
#         # print('2 right find_target_index=', find_target_index)

#         if target_index != -1:
#             # print('3  end right find_target_index=', find_target_index)
#             return target_index

#     # print('4  end return find_target_index=', find_target_index)
#     return target_index


# def broken_search(nums, target) -> int:
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     # print('begin broken_search')
#     # print("1 nums=", nums)
#     # print("1 target=", target)
#     target_index = brokenSearch(nums, target, 0, len(nums)-1)
#     return target_index


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     input_array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     target = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     # print('begin')
#     target_index = broken_search(input_array, target)
#     print(target_index)

# # ------------------------------
# # 20230601
# # ------------------------------

# # 88012713

# def binary_search(array, target, left_index, right_index) -> int:
#     print('begin binarySearch')
#     while right_index > left_index:
#         middle_index = (left_index + right_index) // 2
#         if array[middle_index] == target:
#             # центральный элемент — искомый
#             return middle_index
#         if target < array[middle_index]:
#             # искомый элемент меньше центрального
#             # значит следует искать в левой половине
#             right_index = middle_index
#         else:
#             left_index = middle_index + 1
#     return -1


# # def find_broken(array, find_target) -> int:
# def broken_my_search(array, target, start_index, end_index) -> int:
#     print('begin broken_my_search')
#     print("1 array=", array)
#     print("1 target=", target)
#     print("1 start_index=", start_index)
#     print("1 end_index=", end_index)
#     # target_index = None
#     # while target_index is None:
#     # i=100
#     # while i:
#     #     i-=1
#     while True:
#         print("2while    start_index=", start_index)
#         print("2while    end_index=", end_index)
#         if array[start_index] == target:
#             return start_index
#         if array[end_index] == target:
#             return end_index

#         len_indexes = end_index-start_index + 1
#         print("2while    len_indexes=", len_indexes)
#         if len_indexes < 3:
#             return -1
#         half_len_indexes = (len_indexes // 2) + start_index
#         print("2while    half_len_indexes=", half_len_indexes)

#         if array[start_index] < array[end_index]:
#             print('if array[start_index] < array[end_index]:')
#             print("3if    array[start_index]=", array[start_index])
#             print("3if    array[end_index]=", array[end_index])
#             if array[start_index] < target < array[end_index]:
#                 print('if array[start_index] << find_target <  array[end_index]:')
#                 return binary_search(
#                     array, target, start_index, end_index
#                 )
#                 # target_index = binary_search(
#                 #     array, target, start_index, end_index
#                 # )
#                 # if target_index != -1:
#                 #     return target_index
#             else:
#                 print('else array[start_index] << find_target <  array[end_index]:')
#                 return -1
#         else:
#             print('else if array[start_index] < array[end_index]:')
#             print("3if    array[start_index]=", array[start_index])
#             print("3if    array[end_index]=", array[end_index])
#             if array[start_index] < array[half_len_indexes - 1]:
#                 print('if array[start_index] < array[half_len_indexes - 1]:')
#                 print("3if    array[start_index]=", array[start_index])
#                 print("3if    array[half_len_indexes - 1]=", array[half_len_indexes - 1])
#                 if array[start_index] < target < array[half_len_indexes - 1]:
#                     end_index = half_len_indexes - 1
#                     continue
#                 else:
#                     start_index = half_len_indexes
#                 # continue

#             if array[half_len_indexes] < array[end_index - 1]:
#                 print('if array[half_len_indexes] < array[end_index - 1]')
#                 print("3if    array[half_len_indexes]=", array[half_len_indexes])
#                 print("3if    array[end_index-1]=", array[end_index-1])
#                 if array[half_len_indexes] < target < array[end_index - 1]:
#                     start_index = half_len_indexes
#                     # continue
#                 else:
#                     end_index = half_len_indexes
#                     # continue

#             # if array[start_index] < array[half_len_indexes - 1]:
#             #     # print('if array[start_index] < array[end_index]:')
#             #     if array[start_index] < target < array[half_len_indexes - 1]:
#             #         end_index = half_len_indexes - 1
#             # elif array[half_len_indexes] < array[end_index - 1]:
#             #     # print('if array[start_index] < array[end_index]:')
#             #     if array[half_len_indexes] < target < array[end_index - 1]:
#             #         start_index = half_len_indexes
#             # else:





# def broken_search(nums, target) -> int:
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     print('begin broken_search')
#     print("1 nums=", nums)
#     print("1 target=", target)
#     target_index = broken_my_search(nums, target, 0, len(nums)-1)
#     return target_index


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     input_array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     target = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     # print('begin')
#     target_index = broken_search(input_array, target)
#     print(target_index)


# # ------------------------------
# # 20230621
# # ------------------------------

# # 88012713

# # def binary_search(array, target, left_index, right_index) -> int:
# #     print('begin binarySearch')
# #     while right_index > left_index:
# #         middle_index = (left_index + right_index) // 2
# #         if array[middle_index] == target:
# #             # центральный элемент — искомый
# #             return middle_index
# #         if target < array[middle_index]:
# #             # искомый элемент меньше центрального
# #             # значит следует искать в левой половине
# #             right_index = middle_index
# #         else:
# #             left_index = middle_index + 1
# #     return -1


# def broken_my_search(array, target, start_index, end_index) -> int:
#     # print('begin broken_my_search')
#     # print("1 array=", array)
#     # print("1 target=", target)
#     # print("1 start_index=", start_index)
#     # print("1 end_index=", end_index)

#     while True:
#         if array[start_index] == target:
#             return start_index
#         if array[end_index] == target:
#             return end_index

#         len_indexes = end_index-start_index + 1
#         if len_indexes < 3:
#             return -1
#         half_len_indexes = (len_indexes // 2) + start_index

#         # print("2 start_index=", start_index)
#         # print("2 end_index=", end_index)
#         # print("2 len_indexes=", len_indexes)
#         # print("2 half_len_indexes=", half_len_indexes)
#         # print("2        target=", target)
#         # print("2    array[start_index]=", array[start_index])
#         # print("2    array[half_len_indexes]=", array[half_len_indexes])
#         # print("2    array[end_index]=", array[end_index])        

#         # if array[start_index] < array[end_index]:

#         #     if array[start_index] < target < array[end_index]:

#         #         return binary_search(
#         #             array, target, start_index, end_index
#         #         )

#         if array[half_len_indexes] == target:
#             return half_len_indexes

#         if array[start_index] < array[half_len_indexes]:
#             if array[start_index] < target < array[half_len_indexes]:
#                 end_index = half_len_indexes
#                 continue
#             else:
#                 start_index = half_len_indexes + 1
#                 continue
#         else:
#             if array[half_len_indexes] < target and array[end_index] > target:
#                 start_index = half_len_indexes + 1
#                 continue
#             end_index = half_len_indexes


# def broken_search(nums, target) -> int:
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     # print('begin broken_search')
#     # print("1 nums=", nums)
#     # print("1 target=", target)
#     target_index = broken_my_search(nums, target, 0, len(nums)-1)
#     return target_index


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     input_array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     target = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     # print('begin')
#     target_index = broken_search(input_array, target)
#     print(target_index)

# ------------------------------
# 20230627
# ------------------------------

# # 88012713

# def broken_search(array, target) -> int:
# # def broken_my_search(array, target, start_index, end_index) -> int:
#     # print('begin broken_my_search')
#     # print("1 array=", array)
#     # print("1 target=", target)
#     # print("1 start_index=", start_index)
#     # print("1 end_index=", end_index)
#     start_index = 0
#     end_index = len(array) - 1
#     while True:
#         if array[start_index] == target:
#             return start_index
#         if array[end_index] == target:
#             return end_index

#         len_indexes = end_index-start_index + 1
#         if len_indexes < 3:
#             return -1
#         half_len_indexes = (len_indexes // 2) + start_index

#         # print("2 start_index=", start_index)
#         # print("2 end_index=", end_index)
#         # print("2 len_indexes=", len_indexes)
#         # print("2 half_len_indexes=", half_len_indexes)
#         # print("2        target=", target)
#         # print("2    array[start_index]=", array[start_index])
#         # print("2    array[half_len_indexes]=", array[half_len_indexes])
#         # print("2    array[end_index]=", array[end_index])

#         if array[half_len_indexes] == target:
#             return half_len_indexes

#         if array[start_index] < array[half_len_indexes]:
#             if array[start_index] < target < array[half_len_indexes]:
#                 end_index = half_len_indexes
#                 # continue
#             else:
#                 start_index = half_len_indexes + 1
#                 # continue
#         else:
#             if array[half_len_indexes] < target and array[end_index] > target:
#                 start_index = half_len_indexes + 1
#                 continue
#             # return -1
#             end_index = half_len_indexes


# if __name__ == '__main__':
#     file = open("input.txt", "r")
#     # В первой строке записано число n –— длина массива.
#     input_array_len = int(file.readline())
#     # Во второй строке записано положительное число k –— искомый элемент. 
#     target = int(file.readline())
#     # Далее в строку через пробел записано n натуральных чисел – элементы массива.
#     input_array = tuple(map(int, file.readline().split()))
#     file.close()
#     # print('begin')
#     target_index = broken_search(input_array, target)
#     print(target_index)


# ------------------------------
# 20230628
# ------------------------------

# 88012713

def broken_search(array, target) -> int:
# def broken_my_search(array, target, start_index, end_index) -> int:
    # print('begin broken_my_search')
    # print("1 array=", array)
    # print("1 target=", target)
    # print("1 start_index=", start_index)
    # print("1 end_index=", end_index)
    start_index = 0
    end_index = len(array) - 1
    # while True:
    while start_index <= end_index:
        if array[start_index] == target:
            return start_index
        if array[end_index] == target:
            return end_index

        len_indexes = end_index-start_index + 1
        # if len_indexes < 3:
        #     return -1
        half_len_indexes = (len_indexes // 2) + start_index

        # print("2 start_index=", start_index)
        # print("2 end_index=", end_index)
        # print("2 len_indexes=", len_indexes)
        # print("2 half_len_indexes=", half_len_indexes)
        # print("2        target=", target)
        # print("2    array[start_index]=", array[start_index])
        # print("2    array[half_len_indexes]=", array[half_len_indexes])
        # print("2    array[end_index]=", array[end_index])

        if array[half_len_indexes] == target:
            return half_len_indexes

        if array[start_index] < array[half_len_indexes]:
            if array[start_index] < target < array[half_len_indexes]:
                end_index = half_len_indexes - 1
                # continue
            else:
                start_index = half_len_indexes + 1
                # continue
        else:
            if array[half_len_indexes] < target and array[end_index] > target:
                start_index = half_len_indexes + 1
                # continue
            # return -1
            else:
                end_index = half_len_indexes - 1
    return -1

if __name__ == '__main__':
    file = open("input.txt", "r")
    # В первой строке записано число n –— длина массива.
    input_array_len = int(file.readline())
    # Во второй строке записано положительное число k –— искомый элемент. 
    target = int(file.readline())
    # Далее в строку через пробел записано n натуральных чисел – элементы массива.
    input_array = tuple(map(int, file.readline().split()))
    file.close()
    # print('begin')
    target_index = broken_search(input_array, target)
    print(target_index)
