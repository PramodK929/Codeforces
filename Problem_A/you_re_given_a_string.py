s = input()
reference_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = []
final = []
d = set(s)
if s.count(s[0]) == len(s) or len(d) == 1:
    print(len(s)-1)
elif len(d) == len(s):
    print(0)
else:
    k = 2
    for i in range(2, len(s)):
        for j in range(0, len(s)-1):
            final.append(s[j:k])
        k+=1
    print(final)
    d = set(final)
    print(d)
    innond=[]
    for i in d:
        innond.append(final.count(i))
    print((innond))
