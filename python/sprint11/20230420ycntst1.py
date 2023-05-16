# https://contest.yandex.ru/contest/23389/problems/H/
# H. Двоичная система
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

# Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.

# Формат вывода
# Одно число в двоичной системе счисления.


file = open("input.txt", "r")
#  На вход Два числа в двоичной системе счисления, 
# каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.
x = str(file.readline())
y = str(file.readline())
file.close()
# print(x)
# print(y)

def ff(x,y):
    lenx=len(x)-1
    leny=len(y)-1
    # print("lenx=",lenx)
    # print("leny=",leny)
    if(lenx>leny):
        for i in range(lenx-leny):
            y='0'+y
        
    if(leny>lenx):
        for i in range(leny-lenx):
            x='0'+x
    # print(x)
    # print(y)

    countx=len(x)-2
    county=len(y)-2
    res=''
    tmp=0
    while(countx+1 or county+1 or tmp):
        # print("while countx=",countx)
        # print("while x[countx]=", x[countx])
        # print("while county=",county)
        # print("while y[county]=", y[county])
        # print("while tmp=",tmp)
        if(tmp and countx<0 and county<0):
            res='1'+res
            break
        if(tmp):
            if(x[countx]=='0' and y[county]=='0'):
                res='1'+res
                tmp=0
            elif(x[countx]=='1' and y[county]=='1'):
                res='1'+res
                tmp=1
            else:
                res='0'+res
                tmp=1
        else:
            if(x[countx]=='0' and y[county]=='0'):
                res='0'+res
                tmp=0
            elif(x[countx]=='1' and y[county]=='1'):
                res='0'+res
                tmp=1
            else:
                # print("else while")
                res='1'+res
                tmp=0
        # print("while res=",res)
        county-=1
        countx-=1
        # print("end while tmp=",tmp)
        # print("end while county=",county)
        # print("end while countx=",countx)
    return res

if(x==0):
    print(y)
if(y==0):
    print(y)
res=ff(x,y)
print(res)
