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


# ------------------------------
# 20230527 try1
# ------------------------------

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
#         pipl_list.append(str(file.readline()).rstrip())
#         # pipl_list.append(str(file.readline()).rstrip().split())
#     print('pipl_count=', pipl_count)
#     print('pipl_list=', pipl_list)
#     file.close()    

#     print('begin')


# ------------------------------
# 20230527 try1 pachka
# https://app.pachca.com/chats/3834079?thread_id=1102945
# ------------------------------

# from dataclasses import dataclass
# from typing import List, Tuple


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
#             (self.solved, other.penalties, self.name)
#             < (other.solved, self.penalties, other.name)
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


# # def data_sort(competitor: Competitor) -> List[Tuple[int, int, str]]:
# #     parsing_result = Competitor(*competitor)
# #     return [
# #         -int(parsing_result.solved),
# #         int(parsing_result.penalties),
# #         str(parsing_result.name)
# #     ]


# # def read_input() -> List[Competitor]:
# #     quantity = int(input())
# #     users = [Competitor(*input().split()) for _ in range(quantity)]
# #     return users

# def read_input() -> List[Competitor]:
#     file = open("input.txt", "r")
#     quantity = int(file.readline())
#     users = [Competitor(*file.readline().split()) for _ in range(quantity)]
#     print('quantity=', quantity)
#     print('users=', users)
#     return users


# def main():
#     users = read_input()
#     effective_quick_sort(users)
#     print(*users, sep='\n')


# if __name__ == '__main__':
#     main()








# ------------------------------
# 20230527 try2 pachka
# https://app.pachca.com/chats/3834079?thread_id=1121911
# ------------------------------
import random


class Competitor:
    def __init__(self, name, problems_solved, fine):
        self.name = name
        self.problems_solved = int(problems_solved)
        self.fine = int(fine)

    def __str__(self):
        return f'{self.name}'

    def __lt__(self, other):
        if self.problems_solved > other.problems_solved:
            return True
        if self.problems_solved == other.problems_solved:
            if self.fine < other.fine:
                return True
            if self.fine == other.fine:
                if self.name < other.name:
                    return True
        return False


def in_place_partition(array, pivot):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] > pivot and (pivot > array[right] or pivot == array[right]):
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        elif array[left] > pivot and (array[right] > pivot or array[right] == pivot):
            right -= 1
        elif (array[left] < pivot or array[left] == pivot) and array[right] < pivot:
            left += 1
        else:
            right -= 1
            left += 1
    return array, left


def optimised_quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        partition_result = in_place_partition(array, pivot)
        left_part_end = partition_result[1]
        left = partition_result[0][:left_part_end]
        right = partition_result[0][left_part_end:]
        return optimised_quick_sort(left) + optimised_quick_sort(right)


if __name__ == '__main__':
    file = open("input.txt", "r")
    competitors = []
    number_of_candidates = int(file.readline())
    for _ in range(number_of_candidates):
        competitors.append(Competitor(*file.readline().split()))
    file.close()
    # print('number_of_candidates=', number_of_candidates)
    # print('competitors=', competitors)
    for i in optimised_quick_sort(competitors):
        print(i)
