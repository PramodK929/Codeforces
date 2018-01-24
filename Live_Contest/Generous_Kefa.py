n, k = map(int, input().split())
s = input()
result = False
for i in s:
    if s.count(i)<=k:result = True
    else:result = False;break
print("YES" if result is True else "NO")
