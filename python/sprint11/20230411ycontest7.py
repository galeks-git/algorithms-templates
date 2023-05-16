# from sys import stdin
s=()
s=map(str,input())
j=()
j=map(str,input())
count = 0
k=j
for ss in s:
    print("ss=",ss)
    for jj in k:
        print("jj=",jj)
        if ss == jj:
            print("ss=jj count=",count)
            count += 1
            print("ss=jj count+=",count)
        else:
            continue
print(count)