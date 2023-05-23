# https://contest.yandex.ru/contest/23759/problems/B/

# B. Калькулятор
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений. Еще её иногда называют постфиксной нотацией.

# В постфиксной нотации операнды расположены перед знаками операций.

# Пример 1:
# 3 4 +
# означает 3 + 4 и равно 7

# Пример 2:
# 12 5 /
# Так как деление целочисленное, то в результате получим 2.

# Пример 3:
# 10 2 4 * -
# означает 10 - 2 * 4 и равно 2

# Разберём последний пример подробнее:

# Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию, которую этот знак обозначает, то есть перемножить эти два числа. В результате получим 8.

# После этого выражение приобретёт вид:

# 10 8 -

# Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8. В итоге получаем 2.

# Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

# Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение слева направо и придерживаться следующих шагов:

# Обработка входного символа:
# Если на вход подан операнд, он помещается на вершину стека.
# Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений, взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
# Если входной набор символов обработан не полностью, перейти к шагу 1.
# После полной обработки входного набора символов результат вычисления выражения находится в вершине стека. Если в стеке осталось несколько чисел, то надо вывести только верхний элемент.
# Замечание про отрицательные числа и деление: в этой задаче под делением понимается математическое целочисленное деление. Это значит, что округление всегда происходит вниз. А именно: если a / b = c, то b ⋅ c — это наибольшее число, которое не превосходит a и одновременно делится без остатка на b.

# Например, -1 / 3 = -1. Будьте осторожны: в C++, Java и Go, например, деление чисел работает иначе.

# В текущей задаче гарантируется, что деления на отрицательное число нет.

# Формат ввода
# В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны через пробел.

# На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.

# Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

# Формат вывода
# Выведите единственное число — значение выражения.


# 87465081

import operator


class StackEmptyError(Exception):
    """Вызывается, когда Stack empty"""
    # print('Stack is empty')
    pass


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    def push(self, item):
        self.items.append(item)

    # def pop(self):
    #     return self.items.pop()
    # def peek(self):
    #     return self.items[-1]

    # def size(self):
    #     return len(self.items) 

    # def is_empty(self):
    #     return len(self.items) == 0

    def pop(self):
        if self.items:
            return self.items.pop()
        raise StackEmptyError


def polish_calc(expression):
    # print('polish_calc begin')
    # print("1 stack digits=",digits)
    # result = list(expression)
    # print(result)
    digits = Stack()
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }
    # result = 0
    for i in expression:
        # print("1 stack digits=",digits)
        # print("1 i =",i)
        if i not in operators:
            digits.push(int(i))
            # result = int(i)
        else:
            try:
                operand2 = digits.pop()
                operand1 = digits.pop()
            except StackEmptyError:
                print('Stack is empty. No operands for operation.')
            else:
                # print("     else operand2 =",operand2)
                # print("     else operand1 =",operand1)
                digits.push(operators[i](operand1, operand2))
                # print("     2else stack digits=",digits)
    try:
        result = digits.pop()
    except StackEmptyError:
        print('Stack is empty. No result of operation.')
    else:
        return result
    # return digits.pop()


if __name__ == '__main__':
    file = open("input.txt", "r")
    # В единственной строке дано выражение в обратной польской нотации.
    expression = tuple(file.readline().split())
    # exp_list = tuple(map(str, file.readline().split()))
    file.close()
    # print('begin')
    result = polish_calc(expression)
    print(result)
