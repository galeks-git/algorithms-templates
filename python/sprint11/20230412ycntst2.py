# https://contest.yandex.ru/contest/26365/problems/B/
# Застёжка-молния
# from sys import stdin

n = int(input())                       # Считывание первой строки ввода
arr = list(map(int, input().split()))  # Считывание второй строки ввода
arr2 = list(map(int, input().split()))  # Считывание второй строки ввода
farr = []
for i in range(n):
    farr.append(arr[i])
    farr.append(arr2[i])
print(" ".join(list(map(str, farr))))