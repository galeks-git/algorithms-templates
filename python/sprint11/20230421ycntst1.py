# https://contest.yandex.ru/contest/23389/problems/J/
# J. Факторизация
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.052 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	0.4 секунды	64Mb
# Python 3.7.3	0.2 секунды	64Mb
# OpenJDK Java 11	0.4 секунды	64Mb
# C# (MS .NET 6.0 + ASP)	0.4 секунды	64Mb
# Kotlin 1.8.0 (JRE 11)	0.4 секунды	64Mb
# C# (MS .NET 5.0 + ASP)	0.4 секунды	64Mb
# Основная теорема арифметики говорит: любое число раскладывается на произведение простых множителей единственным образом, с точностью до их перестановки. Например:

# Число 8 можно представить как 2 × 2 × 2.
# Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.
# Разложение числа на простые множители называется факторизацией числа.

# Напишите программу, которая производит факторизацию переданного числа.

# Формат ввода
# В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

# Формат вывода
# Выведите в порядке неубывания простые множители, на которые раскладывается число n.


file = open("input.txt", "r")
# В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.
x = int(file.readline())
file.close()
# print(x)

def is_prime(n):
    # print('prime n=',n)
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True 


def ff(x):
    k=x
    j=2
    j_list=[]
    res=''
    while(k):
        if is_prime(j):
            k=x//j
            kk=x%j
        else:
            j+=1
            continue
        # print('j=',j)
        # print('k=',k)
        # print('kk=',kk)
        # print('j_list=',j_list)
        if(kk!=0):
            j+=1
        if(k!=0 and kk==0):
            res+=str(j)+' '
            if is_prime(k):
                return res+str(k)
            x=k
            # if j not in j_list:
            #     j_list.append(j)
        # print('res=',res)
    return res

if(x==0):
    print(0)
elif(x==1):
    print(1)
elif(is_prime(x)):
    print(x)
else:
    res=ff(x)
    print(res)
