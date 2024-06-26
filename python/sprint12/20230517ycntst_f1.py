# https://contest.yandex.ru/contest/23759/problems/

# A. Дек
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.3 секунды	39Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	1 секунда	64Mb
# Python 3.7.3	2 секунды	64Mb
# OpenJDK Java 11	1 секунда	128Mb
# C# (MS .NET 6.0 + ASP)	1 секунда	64Mb
# C# (MS .NET 5.0 + ASP)	1 секунда	64Mb
# Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

# Внимание: при реализации используйте кольцевой буфер.

# Формат ввода
# В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:

# push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
# push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
# pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
# pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
# Value — целое число, по модулю не превосходящее 1000.
# Формат вывода
# Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.


# 87465081

class DequeFullError(Exception):
    """Вызывается, когда DequeStack full"""
    pass


class DequeEmptyError(Exception):
    """Вызывается, когда DequeStack empty"""
    pass


class Deque:
    def __init__(self, len_cells):
        self.cells = [None] * len_cells
        self.len_cells = len_cells
        self.head = 0
        self.tail = 0
        # self.tail = 1
        self.size = 0

    def __str__(self):
        return ' '.join(str(x) for x in self.cells)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.len_cells

    def push_back(self, value):
        if self.is_full():
            raise DequeFullError
        # if self.is_empty():
        #     self.tail = self.head
        self.cells[self.tail] = value
        # print("1push_back self.tail=",self.tail)
        self.tail = (self.tail + 1) % self.len_cells
        # print("2push_back self.tail=",self.tail)
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise DequeFullError
        # if self.is_empty():
        #     self.tail = self.head
            # self.tail = (self.head + 1) % self.len_cells
        self.head = (self.head - 1) % self.len_cells
        self.cells[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeEmptyError
        tmp_cell = self.cells[self.head]
        self.cells[self.head] = None
        # print("1pop_front self.head=",self.head)
        # print("1pop_front self.tail=",self.tail)
        # print("1pop_front self.size=",self.size)
        self.head = (self.head + 1) % self.len_cells
        self.size -= 1
        # print("2pop_front self.head=",self.head)
        # print("2pop_front self.tail=",self.tail)
        # print("2pop_front self.size=",self.size)
        return tmp_cell

    def pop_back(self):
        if self.is_empty():
            raise DequeEmptyError
        # print("1pop_back self.tail=",self.tail)
        self.tail = (self.tail - 1) % self.len_cells
        # print("2pop_back self.tail=",self.tail)
        tmp_cell = self.cells[self.tail]
        self.cells[self.tail] = None
        self.size -= 1
        return tmp_cell


if __name__ == '__main__':
    file = open("input.txt", "r")
    # В первой строке записано количество команд
    number_of_commands = int(file.readline())
    # Во второй строке записано число m — максимальный размер дека.
    deck_max_len = int(file.readline())
    # В следующих n строках записана одна из команд:
    # push_back(value) – добавить элемент в конец дека.
    # Если в деке уже находится максимальное число элементов, вывести «error».
    # push_front(value) – добавить элемент в начало дека.
    # Если в деке уже находится максимальное число элементов, вывести «error».
    # pop_front() – вывести первый элемент дека и удалить его.
    # Если дек был пуст, то вывести «error».
    # pop_back() – вывести последний элемент дека и удалить его.
    # Если дек был пуст, то вывести «error».
    # Value — целое число, по модулю не превосходящее 1000.

    commands_list = []
    for i in range(number_of_commands):
        commands_list.append(str(file.readline()).rstrip())
    # print('deck_max_len=', deck_max_len)
    # print('commands_list=', commands_list)
    file.close()

    new_stack = Deque(deck_max_len)

    for i in commands_list:
        a, *b = i.split()
        # print("1 a=",a)
        # print("1 b=",b)
        try:
            result = getattr(new_stack, a)(*b)
        except (DequeEmptyError, DequeFullError):
            print('error')
        else:
            if result:
                print(result)
        # print("1new_stack=",new_stack)
