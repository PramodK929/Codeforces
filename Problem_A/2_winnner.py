# t = int(input())
# name = []
# score = []
# top_score = 0
# for i in range(t):
#     ip = input().split(' ')
#     name.append(ip[0])
#     score.append(ip[1])
# unique_names = list(set(name))
# unique_reference = []
# sum = []
# for i in range(len(unique_names)):
#     s = 0
#     for j in range(len(name)):
#         if unique_names[i] == name[j]:
#             s += int(score[j])
#     sum.append(s)
# mx_score = max(sum)
# final_names = []
# for i in range(len(sum)):
#     if sum[i]>=mx_score:
#         final_names.append(unique_names[i])
# for i in range(len(name)):
#     f_sum = dic(name[i]);
#     if name[i] in final_names:
p, r, n = [], {}, int(input())
for i in range(n):
    a, b = input().split()
    b = int(b)
    r[a] = r.get(a, 0) + b
    p.append([r[a], a])
    m = max(r.values())
for n, a in p:
    if n >= m and r[a] >= m:
        print(a)
        break