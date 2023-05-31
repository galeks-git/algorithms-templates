# https://contest.yandex.ru/contest/24734/problems/L/

# L. Два велосипеда
# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления Вася не вынимает деньги из копилки.

# У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

# Ваша задача — по заданной стоимости велосипеда определить

# первый день, в которой Вася смог бы купить один велосипед,
# и первый день, в который Вася смог бы купить два велосипеда.
# Подсказка: решение должно работать за O(log n).

# Формат ввода
# В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

# В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

# В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

# Формат вывода
# Нужно вывести два числа — номера дней по условию задачи.

# Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.


def binarySearch(arr, x, left, right) -> int:
    # print('begin binarySearch')
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        while(arr[mid] == x):
            mid-=1
        return mid+1
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


def VeloSearch(digits_array, x, n_days):
    velo_price=x

    print('begin VeloSearch')
    print('n_days=',n_days)
    print('digits_array=',digits_array)
    print('velo_price=',velo_price)

    if(velo_price>digits_array[-1]):
        return -1
    while(velo_price<=digits_array[-1]):
        print('1velo_price=',velo_price)
        a=binarySearch(digits_array,velo_price,0,n_days)
        print('a=',a)
        if a!=-1:
            return a+1
        velo_price+=1
        print('2velo_price=',velo_price)
    if a==-1:
        return -1


if __name__ == '__main__':

    file = open("input.txt", "r")
    # В В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями
    n_days = int(file.readline())
    # В следующей строке записаны n целых неотрицательных чисел. 
    # Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.
    digits_array = tuple(map(int, file.readline().split()))
    # В третьей строке записано целое положительное число s — стоимость велосипеда.
    #  Это число не превосходит 106.
    velo_price_begin = int(file.readline())
    file.close()

    print('begin')
    print('n_days=',n_days)
    print('digits_array=',digits_array)
    print('velo_price_begin=',velo_price_begin)

    res=[]
    res.append(VeloSearch(digits_array, velo_price_begin,n_days))
    res.append(VeloSearch(digits_array, 2*velo_price_begin,n_days))
   
    print(' '.join(str(x) for x in res))

