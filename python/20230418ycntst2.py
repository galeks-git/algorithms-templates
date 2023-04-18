# https://contest.yandex.ru/contest/23389/problems/E/
# E. Самое длинное слово
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо оценить сложность статьи.

# Он придумал такой метод оценки: берётся случайное предложение из текста и в нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.

# Помогите Гоше справиться с этой задачей.

# Формат ввода
# В первой строке дана длина текста L (1 ≤ L ≤ 105).

# В следующей строке записан текст, состоящий из строчных латинских букв и пробелов. Слово —– последовательность букв, не разделённых пробелами. Пробелы могут стоять в самом начале строки и в самом её конце. Текст заканчивается переносом строки, этот символ не включается в число остальных L символов.

# Формат вывода
# В первой строке выведите самое длинное слово. Во второй строке выведите его длину. Если подходящих слов несколько, выведите то, которое встречается раньше.


file = open("input.txt", "r")
#  В первой строке дана длина текста L (1 ≤ L ≤ 105).
l = int(file.readline())
#  В следующей строке записан текст, состоящий из строчных латинских букв и пробелов. 
ll = list(map(str, file.readline().split()))
file.close()

res=''
rlen=0
for count in range(len(ll)):
    tmp = len(ll[count])
    if(tmp>rlen):
        rlen=tmp
        res=ll[count]
print(res)
print(rlen)

