n = int(input())
arr = [int(i) for i in input().split()]
ref = []
for i in arr:
    if i%2 == 0: ref.append(0)
    else:ref.append(1)
print(ref.index(ref.count(max(ref)) < ref.count(min(ref)))+1)