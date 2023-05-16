# https://contest.yandex.ru/contest/23758/problems/G/

# G. Стек - MaxEffective
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.2 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	1.5 секунд	64Mb
# Python 3.7.3	1.5 секунд	64Mb
# OpenJDK Java 11	1.5 секунд	64Mb
# C# (MS .NET 6.0 + ASP)	1.5 секунд	64Mb
# Golang 1.20.1	0.5 секунд	64Mb
# C# (MS .NET 5.0 + ASP)	1.5 секунд	64Mb
# Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке. Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop() также должны выполняться за константное время.

# Формат ввода
# В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в строке. Команды могут быть следующих видов:

# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;
# Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».
# Формат вывода
# Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return 'error'

    def get_max(self):
        if self.items:
            return max(self.items)
        else:
            return None

    # def peek(self):
    #     return self.items[-1]

    # def size(self):
    #     return len(self.items) 


if __name__ == '__main__':
    # NUMBER_OF_PLAYERS = 2

    file = open("input.txt", "r")
    # В первой строке записано одно число n — количество команд, которое не превосходит 10000.
    n = int(file.readline())
    # В следующих n строках идут команды. Команды могут быть следующих видов:
    # push(x) — добавить число x в стек;
    # pop() — удалить число с вершины стека;
    # get_max() — напечатать максимальное число в стеке;
    # Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

    commands_list=[]
    for i in range(n):
        commands_list.append(str(file.readline()).rstrip())
    # print('commands_list=', commands_list)


    new_stack=StackMax()

    # comm_dict={
    #     # 'push': push,
    #     # 'pop': pop,
    #     # 'get_max': get_max,
    #     'push': new_stack.push,
    #     'pop': new_stack.pop,
    #     'get_max': new_stack.get_max,
    # }

    for i in commands_list:
        # print(i)
        command=i.split()
        # print(command)
        # print(new_stack.i())
        if command[0]=='push':
            # comm_dict[command[0]](int(command[1]))
            # new_stack.comm_dict[command[0]](int(command[1]))
            getattr(new_stack, command[0])(int(command[1]))
        elif command[0]=='pop':
            # comm_dict[command[0]]()
            # new_stack.comm_dict[command[0]](int(command[1]))
            # getattr(new_stack, command[0])()
            k=getattr(new_stack, command[0])()
            if (k=="error"):
                print(k)
        elif command[0]=='get_max':
            # k=comm_dict[command[0]]()
            # k=new_stack.comm_dict[command[0]]()
            k=getattr(new_stack, command[0])()
            print(k)
        # else:
        #     k=comm_dict[command[0]]()
        #     # k=new_stack.comm_dict[command[0]]()
        #     # k=getattr(new_stack, command[0])()
        #     # print(k)

