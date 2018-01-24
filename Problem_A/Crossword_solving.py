n, m = input().split()
s = input()
t =input()
final_min = 0
final_list = []
min = len(s)
for i in range(len(t)):
    final_list = []
    count = 0
    idx = []
    for j in range(len(s)):
        if s[j] != t[i]:
            count += 1
            if j not in idx:
                idx.append(j)
    if count<min:
        final_min = count
        final_list = idx
print(final_min)
print(final_list)

