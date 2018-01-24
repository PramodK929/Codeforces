n = int(input())
s = input().split()
num = []
c = 0
for i in s:
    c = 0
    for j in i:
        if ord(j)>64 and ord(j)<=90:
            c+=1
    num.append(c)
print(max(num))
