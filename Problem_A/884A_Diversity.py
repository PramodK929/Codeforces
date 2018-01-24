str = input()
k = int(input())
if len(set(str)) == len(str) and len(str)>=k: print(0)
elif k<= len(str):
    if len(set(str))>= k:print(0)
    else:print(abs(k - len(set(str))))
else: print("impossible")
