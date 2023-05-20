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


# 87465081


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
            return None


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
        ')':"(",
        ']':"[",
        '}':"{",
        '(':None,
        '[':None,
        '{':None,
        # '(':")",
        # '[':"]",
        # '{':"}",
    }

    new_stack=StackMax()

    res = True

    for i in ll:
        if i not in ldict:
            print("i not in ldict:")
            print("     new_stack=",new_stack)
            x = new_stack.pop()
            if x is not None:
                print("     if x is None")
                res = False
                print("         res=",res)
            continue
        x = new_stack.pop()
        if x is None:
            print("if x is None")
            print("     i=",i)
            new_stack.push(i)
            print("     new_stack=",new_stack)
            continue
        print("i=",i)
        print("x=",x)
        if ldict[i] == x:
            res = True
            print("ldict[i] == x")
            print("     new_stack=",new_stack)
            print("     res=",res)
            continue
        # if(i == x):
        #     continue
        else:
            res = False
            print("else")
            print("     res=",res)
            new_stack.push(x)
            new_stack.push(i)
        print("new_stack=",new_stack)
    print(res)

