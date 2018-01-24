n = input()
sum1 =0
sum2 = 0
for i in n[0:3]:sum1 += int(i)
for j in n[3:]:sum2 += int(j)
if sum1 == sum2:print(0)
elif sum1 < sum2:
    digit = sum1 - sum2
    if digit > 18:print(3)
    elif digit < 9:print(2)
    else:print(1)
else:
    if sum1 > 18:
        ad = sum1 - sum2
