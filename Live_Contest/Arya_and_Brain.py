n, k = map(int, input().split(' '))
arr = [int(i) for i in input().split(' ')]
c = 0
rem = 0
result = False
days = 0
for i in arr:
    if i + rem <= 8:
        c+=i+rem
        rem = 0
    else:
        c+=8
        rem = i+rem-8
    # print(c, rem, k, days)
    if c >= k:
        result = True
        break
    else:
        days+=1
if result == True:
    print(days+1)
else:
    print(-1)