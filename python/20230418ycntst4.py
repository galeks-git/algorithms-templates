# https://contest.yandex.ru/contest/23389/problems/G/
# G. Работа из дома
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. Но, кажется, она получилась не очень оптимальной.

# Попробуйте написать более эффективную программу.

# Не используйте встроенные средства языка по переводу чисел в бинарное представление.

# Формат ввода
# На вход подаётся целое число в диапазоне от 0 до 10000.

# Формат вывода
# Выведите двоичное представление этого числа.


file = open("input.txt", "r")
#  На вход подаётся целое число в диапазоне от 0 до 10000.
x = int(file.readline())
file.close()
# print(x)
if(x==0):
    print('0')
else:
    ll=''
    k=x
    while(x):
        k=x%2
        # k=x//2
        x=x//2
        c=str(k)
        # print("while k=",k)
        # print("while chr k=",c)
        # ll+='1'
        ll=str(k)+ll
        # ll.insert(0,(str(k)))
        # print(ll)
    print(ll)