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


class DeckStack:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def __str__(self):
        return ' '.join(str(x) for x in self.queue)

    def is_empty(self):
        return self.size == 0

    def head_forward(self):
        if (self.head == self.max_n - 1):
            self.head = 0
        else:
            self.head += 1
        return

    def head_backward(self):
        if (self.head == 0):
            self.head = self.max_n - 1
        else:
            self.head -= 1
        return

    def tail_forward(self):
        if (self.tail == self.max_n - 1):
            self.tail = 0
        else:
            self.tail += 1
        return

    def tail_backward(self):
        if (self.tail == 0):
            self.tail = self.max_n - 1
        else:
            self.tail -= 1
        return

    def push_back(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            # print("1push_back self.tail=",self.tail)
            self.tail_forward()
            # self.tail = (self.tail + 1) % self.max_n
            # print("2push_back self.tail=",self.tail)
            self.size += 1
        else:
            return 'error'

    def push_front(self, x):
        if self.size != self.max_n:
            if (self.queue[self.head] is None):
                self.queue[self.head] = x
                self.tail = self.head
                self.tail_forward()
            else:
                self.head_backward()
                # print("2push_front self.head=",self.head)
                self.queue[self.head] = x
                # print("1push_front self.head=",self.head)
            # self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        if (self.size == 1):
            # print("1pop_front self.head=",self.head)
            # print("1pop_front self.tail=",self.tail)
            # print("1pop_front self.size=",self.size)
            self.tail = self.head
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.size -= 1
            # print("2pop_front self.head=",self.head)
            # print("2pop_front self.tail=",self.tail)
            # print("2pop_front self.size=",self.size)
            return x
        x = self.queue[self.head]
        self.queue[self.head] = None
        # print("1pop_front self.head=",self.head)
        # print("1pop_front self.tail=",self.tail)
        # print("1pop_front self.size=",self.size)
        self.head_forward()
        # self.head = (self.head + 1) % self.max_n
        self.size -= 1
        # print("2pop_front self.head=",self.head)
        # print("2pop_front self.tail=",self.tail)
        # print("2pop_front self.size=",self.size)
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        if (self.size == 1):
            # print("1pop_back self.tail=",self.tail)
            # print("1pop_back self.head=",self.head)
            self.tail = self.head
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.size -= 1
            # print("2pop_back self.head=",self.head)
            # print("2pop_back self.tail=",self.tail)
            return x
        # print("1pop_back self.tail=",self.tail)
        self.tail_backward()
        # print("2pop_back self.tail=",self.tail)
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return x


if __name__ == '__main__':
    # NUMBER_OF_PLAYERS = 2

    file = open("input.txt", "r")
    # В первой строке записано количество команд n — целое число, не превосходящее 100000.
    number_of_commands = int(file.readline())
    # Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000.
    deck_max_len = int(file.readline())
    # В следующих n строках записана одна из команд:

    # push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
    # push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
    # pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
    # pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
    # Value — целое число, по модулю не превосходящее 1000.

    commands_list = []
    for i in range(number_of_commands):
        commands_list.append(str(file.readline()).rstrip())
    # print('deck_max_len=', deck_max_len)
    # print('commands_list=', commands_list)

    new_stack = DeckStack(deck_max_len)

    for i in commands_list:
        command = i.split()
        # print(i)
        # print(command)
        # print("1new_stack=",new_stack)
        if 'push_' in command[0]:
            # comm_dict[command[0]](int(command[1]))
            # new_stack.comm_dict[command[0]](int(command[1]))
            result = getattr(new_stack, command[0])(int(command[1]))
            if (result == "error"):
                print(result)
        elif 'pop_' in command[0]:
            # comm_dict[command[0]]()
            # new_stack.comm_dict[command[0]](int(command[1]))
            # getattr(new_stack, command[0])()
            result = getattr(new_stack, command[0])()
            print(result)
        # print("2new_stack=",new_stack)
