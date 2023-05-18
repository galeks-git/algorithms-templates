# https://contest.yandex.ru/contest/23758/problems/H/

# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов. Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.

# Дана скобочная последовательность. Нужно определить, правильная ли она.

# Будем придерживаться такого определения:

# пустая строка —– правильная скобочная последовательность;
# правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
# правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью —– тоже правильная.
# На вход подаётся последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True, если последовательность правильная, а иначе False.

# Формат ввода
# На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.

# Формат вывода
# Выведите «True» или «False».

class StackMax:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join(str(x) for x in self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return 'error'

    # def get_max(self):
    #     if self.items:
    #         return max(self.items)
    #     else:
    #         return None

    # def peek(self):
    #     return self.items[-1]

    # def size(self):
    #     return len(self.items) 


if __name__ == '__main__':

    file = open("input.txt", "r")
    #  На вход подаётся одна строка, содержащая скобочную последовательность.
    # Скобки записаны подряд, без пробелов.
    l = str(file.readline())
    file.close()

    ll="".join(c for c in l)
    # ll="".join(c.lower() for c in l if c.isalnum())

    print(l)
    print(ll)

    ldict={
        '(':")",
        '[':"]",
        '{':"}",
    }

    new_stack=StackMax()

    for i in ll:
        x = new_stack.pop()
        print("i=",i)
        print("x=",x)
        if(i == x):
            continue
        else:
            new_stack.push(x)
            new_stack.push(i)
        print("new_stack=",new_stack)


    # lenl=len(ll)
    # res='True'
    # rlen=0
    # count_lenl=lenl-1
    # for count in range(int(lenl/2)):
    #     if(ll[count]!=ll[count_lenl]):
    #         res='False'
    #         break
    #     count_lenl-=1
    # print(res)


    # for i in commands_list:
    #     # print(i)
    #     command=i.split()
    #     # print(command)
    #     # print(new_stack.i())
    #     if command[0]=='push':
    #         # comm_dict[command[0]](int(command[1]))
    #         # new_stack.comm_dict[command[0]](int(command[1]))
    #         getattr(new_stack, command[0])(int(command[1]))
    #     elif command[0]=='pop':
    #         # comm_dict[command[0]]()
    #         # new_stack.comm_dict[command[0]](int(command[1]))
    #         # getattr(new_stack, command[0])()
    #         k=getattr(new_stack, command[0])()
    #         if (k=="error"):
    #             print(k)
    #     elif command[0]=='get_max':
    #         # k=comm_dict[command[0]]()
    #         # k=new_stack.comm_dict[command[0]]()
    #         k=getattr(new_stack, command[0])()
    #         print(k)
    #     # else:
    #     #     k=comm_dict[command[0]]()
    #     #     # k=new_stack.comm_dict[command[0]]()
    #     #     # k=getattr(new_stack, command[0])()
    #     #     # print(k)

