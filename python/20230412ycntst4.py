# https://contest.yandex.ru/contest/26365/problems/D/
# D. Две фишки

#  В первой строке записано количество фишек n
n = int(input())
#  Во второй строке записано n целых чисел —– очки на фишках
q_list = list(map(int, input().split()))  
# В третьей строке —– загаданное Гошей целое число k
k = int(input())

result = []  # Пустой массив.


def ff():
    for i in range(0, n):
        for j in range(i+1, n):
            if q_list[i] + q_list[j] == k:
                result.append(q_list[i])
                result.append(q_list[j])
                return


ff()
if result:
    print(result[0], result[1])
else:
    print('None')
