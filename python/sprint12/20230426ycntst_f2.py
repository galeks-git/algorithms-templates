# https://contest.yandex.ru/contest/23390/problems/B/

# B. Ловкость рук
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9.

# В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

# Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

# Формат ввода
# В первой строке дано целое число k (1 ≤ k ≤ 5).

# В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой строке. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

# Формат вывода
# Выведите единственное число -— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.



# В начале каждого решения в комментарии укажите ID успешной посылки,
# чтобы ревьюер мог удостовериться, что решение рабочее.




# ID: 86518345

from collections import Counter

NUMBER_OF_PLAYERS = 2


def dexterity_hands(matrix_4_4, buttons_per_player):
    # matrix_dict = Counter()

    # for i in matrix_4_4:
    #     matrix_dict += Counter(i)
    #     print('i=', i)
    #     # f = Counter(i)
    #     # matrix_dict += f
    #     print('matrix_dict=', matrix_dict)
    
    matrix_dict = Counter(matrix_4_4)
    # print('matrix_dict=', matrix_dict)
    result = [
        x for x in matrix_dict
        if matrix_dict[x] <= NUMBER_OF_PLAYERS * buttons_per_player
    ]
    return len(result)


if __name__ == '__main__':
    # NUMBER_OF_PLAYERS = 2

    file = open("input.txt", "r")
    # В первой строке дано целое число k (1 ≤ k ≤ 5).
    buttons_per_player = int(file.readline())
    # В четырёх следующих строках задан вид тренажёра -— по 4 символа в строке.
    # Каждый символ – либо точка, либо цифра от 1 до 9.
    # Символы одной строки идут подряд и не разделены пробелами.
    matrix_4_4 = ''
    # matrix_4_4 = []
    for n_count in range(4):
        matrix_4_4 += "".join(filter(str.isdecimal, str(file.readline())))
    file.close()
    # print('matrix_4_4=', matrix_4_4)

    result = dexterity_hands(matrix_4_4, buttons_per_player)
    print(result)
