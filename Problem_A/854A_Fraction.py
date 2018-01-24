import math
n = int(input())
half = 0
if n % 2 == 0: half = n//2-1
else: half = n//2
r = True
while half > 1:
    r = False
    if math.gcd(half, n-half) == 1 and r == False:
        print(half, n-half)
        break
    else: r = True
    half -= 1
if r == True: print(half, n-half)