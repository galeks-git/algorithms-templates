# https://contest.yandex.ru/contest/23389/problems/L/
# L. Лишняя буква
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

# Формат ввода
# На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

# Формат вывода
# Выведите лишнюю букву.


file = open("input.txt", "r")
# На вход подаются строки s и t, разделённые переносом строки.
# s = str(file.readline())
# t = str(file.readline())
ss = str(file.readline())
# ss = list(map(str, file.readline()))
tt = list(map(str, file.readline()))
# ll = list(map(str, file.readline().split()))


file.close()
# print(x)


# print('lenll=',lenll)
# print('ll=',ll)
print('ss=',ss)
print('tt=',tt)

res=''
for i in tt:
    # print('tt[i]=',tt[i])
    if(i not in ss):
        res=i
    if(i in ss):
        ss = ss.replace(i, '',1)
    # print('ss=',ss)
print(res)
# break