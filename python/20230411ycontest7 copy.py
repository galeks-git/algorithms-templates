# from sys import stdin
file = open("input7.txt", "r")
# a,b=map(int,file.read().split())
s=()
j=()
s,j=map(str,file.input().split('\n'))
# j=map(str,file.input())
file.close()
count = 0
for ss in s:
    print("ss=",ss)
    for jj in j:
        print("jj=",jj)
        if ss == jj:
            print("ss=jj count=",count)
            count += 1
            print("ss=jj count+=",count)
print(count)