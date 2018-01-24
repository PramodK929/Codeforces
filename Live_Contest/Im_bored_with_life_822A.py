a, b = input().split(' ')
p = 1
for i in range(2, min(int(a), int(b))+1):p *= i
print(p)