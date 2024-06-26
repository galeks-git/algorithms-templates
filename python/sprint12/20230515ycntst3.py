# https://contest.yandex.ru/contest/23758/problems/D/

# D. Заботливая мама
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите функцию solution, определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке, если значение присутствует.
# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и искомый элемент, а возвращает целое число — индекс найденного элемента или -1.
# Используйте заготовки кода для данной задачи, расположенные по ссылкам:

# c++
# Java
# js
# Python
# C#
# go
# Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдет тесты.

# Формат ввода
# Функция на вход принимает голову односвязного списка и элемент, который нужно найти. Длина списка не превосходит 10000 элементов. Список не бывает пустым.
# Следуйте следующим правилам при отправке решений:

# По умолчанию выбран компилятор Make, выбор компилятора в данной задаче недоступен.
# Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
# Для Java файл должен называться Solution.java, для C# – Solution.cs
# Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
# Для Go укажите package main.
# Формат вывода
# Функция возвращает индекс первого вхождения искомого элемента в список(индексация начинается с нуля). Если элемент не найден, нужно вернуть -1.
# Примечания
# Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования. Нужно выбирать компилятор make.
# Для Java файл должен называться Solution.java
# Для остальных языков программирования это имя использовать нельзя (имя solution тоже).



# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

# LOCAL = False
LOCAL = True


if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, el):
    # Your code
    # ヽ(´▽`)/
    
    index=0

    cur_node=node
    next_node=node
    while(1):
        # print(cur_node.value)
        if cur_node.value == el:
            # print("return index=",index)
            return index
        if cur_node.next_item == None:
            return -1
        cur_node=cur_node.next_item
        index+=1


def nodes_print(node):
    # Your code
    # ヽ(´▽`)/
    cur_node=node
    next_node=node
    while(1):
        print(cur_node.value)
        if cur_node.next_item == None:
            return
        next_node=cur_node.next_item
        cur_node=next_node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    nodes_print(node0)
    res=solution(node0, "node1")
    print(res)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
    
