# https://contest.yandex.ru/contest/23758/problems/C/

# C. Нелюбимое дело
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася размышляет, что ему можно не делать из того списка дел, который он составил. Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову обновлённого списка.
# Используйте заготовки кода для данной задачи, расположенные по ссылкам:

# c++
# Java
# js
# Python
# C#
# go
# Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдет тесты.

# Формат ввода
# Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). Список содержит не более 
# 5
# 0
# 0
# 0
#  элементов. Список не бывает пустым.
# Следуйте следующим правилам при отправке решений:

# По умолчанию выбран компилятор Make, выбор компилятора в данной задаче недоступен.
# Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
# Для Java файл должен называться Solution.java, для C# – Solution.cs
# Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
# Для Go укажите package main.
# Формат вывода
# Верните голову списка, в котором удален нужный элемент.




# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

# LOCAL = False
LOCAL = True


if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, index):
    # Your code
    # ヽ(´▽`)/
    if (index==0):
        return node.next_item
    
    head=node
    
    prev_node=node
    cur_node=node.next_item
    next_node=cur_node.next_item

    for i in range(1, index):
        # print("for i=",i)
        prev_node=cur_node
        if cur_node.next_item == None:
            prev_node.next_item=None
            return head
        cur_node=cur_node.next_item
        next_node=cur_node.next_item

    prev_node.next_item=next_node
    return head

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
    node00=solution(node0, 4)
    nodes_print(node00)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
    
