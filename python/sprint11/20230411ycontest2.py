# from sys import stdin
file = open("input.txt", "r")
a,b=map(int,file.read().split())
file.close()
f = open("output.txt", "w")
f.write(str(a+b))
f.close()
