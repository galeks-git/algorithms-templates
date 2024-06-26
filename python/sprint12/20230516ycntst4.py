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

LOCAL = True

if LOCAL:
    class DoubleConnectedNode:  
        def __init__(self, value, next=None, prev=None):  
            self.value = value  
            self.next = next  
            self.prev = prev


def solution(node):
    # Your code
    # ヽ(´▽`)/
    
    # print("solution")

    node_last=DoubleConnectedNode(node.value)
    node_last.next=None
    node_last.prev=node.next    
    node=node.next 

    # print('node_last.value=',node_last.value)
    # print('node_last.prev_item=',node_last.prev.value)
    # print('node.value=',node.value)

    while(1):
        # print('while node.value=',node.value)
        new_node=DoubleConnectedNode(node.value)
        new_node.next=node_last
        new_node.prev=node.next
        # print('while new_node.value=',new_node.value)
        if node.next == None:
            return new_node
        node_last=new_node
        node=node.next    


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1 
    assert node2.prev is node3
    assert node1.next is node0 
    assert node1.prev is node2
    assert node0.prev is node1

if __name__ == '__main__':
    test()



