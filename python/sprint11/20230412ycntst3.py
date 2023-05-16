# https://contest.yandex.ru/contest/26365/problems/C/
# C. Скользящее среднее

#  натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105
n = int(input())
#  n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103
q_list = list(map(int, input().split()))  
# натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
k = int(input())

result = []  # Пустой массив.
# Первый раз вычисляем значение честно и сохраняем результат.
current_sum = sum(q_list[0:k])
result.append(current_sum / k)
for i in range(0, len(q_list) - k):
    current_sum -= q_list[i]
    current_sum += q_list[i+k]
    current_avg = current_sum / k
    result.append(current_avg)

print(" ".join(list(map(str, result))))