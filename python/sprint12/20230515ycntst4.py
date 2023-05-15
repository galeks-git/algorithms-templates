# https://contest.yandex.ru/contest/23758/problems/E/

# E. Всё наоборот
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася решил запутать маму —– делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке. Напишите функцию, которая вернёт список в обратном порядке.
# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову двусвязного списка и возвращает голову перевёрнутого списка. Ниже дано описание структуры, которая задаёт вершину списка.
# Используйте заготовки кода для данной задачи, расположенные по ссылкам:

# c++
# Java
# js
# Python
# C#
# go
# Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдёт тесты.

# Формат ввода
# Функция принимает на вход единственный аргумент — голову двусвязного списка.
# Длина списка не превосходит 1000 элементов. Список не бывает пустым.
# Следуйте следующим правилам при отправке решений:

# По умолчанию выбран компилятор Make, выбор компилятора в данной задаче недоступен.
# Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
# Для Java файл должен называться Solution.java, для C# – Solution.cs
# Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
# Для Go укажите package main.
# Формат вывода
# Функция должна вернуть голову развернутого списка.


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

# LOCAL = False
LOCAL = True


if LOCAL:
    class Node:
        def __init__(self, value, next_item=None, prev_item=None):
            self.value = value
            self.next_item = next_item
            self.prev_item = prev_item


def solution(node):
    # Your code
    # ヽ(´▽`)/
    
    # cur_node=node
    # next_node=node.next_item
    # prev_node=None

    print("solution")

    cur_node=node
    node_last=node
    node_last.next_item=None
    # node_last.prev_item=node.next_item    
    # cur_node=node.next_item
    print('node_last.value=',node_last.value)
    print('cur_node.value=',cur_node.value)


    # node.next_item=None
    # node.prev_item=tmp_node.next_item

    while(1):
        print(cur_node.value)
        tmp_node=cur_node
        if cur_node.next_item == None:
            tmp_node.next_item=node_last
            node_last.prev_item=None
            return tmp_node
        tmp_node.next_item=node_last
        node_last.prev_item=tmp_node
        cur_node=cur_node.next_item

        # tmp_node.next_item=tmp_node.prev_item
        # cur_node=tmp_node.next_item


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
    node3 = Node("node3", None, None)
    node2 = Node("node3", None, None)
    node1 = Node("node3", None, None)
    node0 = Node("node3", None, None)
    node3 = Node("node3", None, node2)
    node2 = Node("node2", node3, node1)
    node1 = Node("node1", node2, node0)
    node0 = Node("node0", node1, None)
    nodes_print(node0)
    new_head=solution(node0)
    print("result")
    nodes_print(new_head)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
    
