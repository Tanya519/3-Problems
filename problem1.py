n=int(input())
a=[]
for i in range (n):
    a.append(int(input()))
s=int(input())
for i in range (n):
    for j in range (n):
        if i!=j and a[i]+a[j]==s:
                print(i, ' ',j)
    break





