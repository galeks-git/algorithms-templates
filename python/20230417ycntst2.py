# https://contest.yandex.ru/contest/23389/problems/B/
# B. Чётные и нечётные числа
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа. Если все три числа оказываются одной чётности, игрок выигрывает.

# Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

# Формат ввода
# В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.

# Формат вывода
# Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.


file = open("input.txt", "r")
a,b,c=map(int,file.readline().split())
file.close()

y = (a%2)+(b%2)+(c%2)
# print("y=",y)
if(y==0 or y==3):
    print("WIN")
else:
    print("FAIL")
