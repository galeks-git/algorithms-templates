# https://contest.yandex.ru/contest/23389/problems/I/
# I. Степень четырёх
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

# Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.

# Формат ввода
# На вход подаётся целое число в диапазоне от 1 до 10000.

# Формат вывода
# Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.


file = open("input.txt", "r")
# На вход подаётся целое число в диапазоне от 1 до 10000.
x = int(file.readline())
file.close()
# print(x)

def ff(x):
    k=x
    r=x
    while(k):
        # print('r=',r)
        # print('x=',x)
        k=x//4
        print('k=',k)
        if(k!=0):
            r=x%(4*k)
            if(k==1):
                return True
            if(r!=0 or k<4):
                return False
        x=k
        print('end r=',r)
    # return True

    # if (r==0):
    #     return True
    # else:
    #     return False

if(x==0):
    print('False')
elif(x==1):
    print('True')
else:
    res=ff(x)
    print(res)
