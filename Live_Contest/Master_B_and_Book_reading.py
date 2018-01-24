c, v0, v1, a , l  = map(int, input().split(' '))
result = False
i = 1
sum = 0
while result!= True:
    if a == 0 and l == 0:
        i = c + 1
        break
    if (i-1) * a >= v1:
        z = v1
    else:
        z = (i-1) * a
    if(i==1):
        sum += (v0 + z)
    else:
        sum += (z - l)
    if(sum >= c):
        result = True
    i += 1
print(i-1)
