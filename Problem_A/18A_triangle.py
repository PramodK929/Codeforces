# ip = input().split(' ')
# neigther = set(ip)
# print(neigther)
# if len(ip) == len(neigther):
#     print("NEITHER")
#
#










ipt = input().split()
u = set(ipt)
ref = []
for i in u:ref.append(ipt.count(i))
t = False
if ref[0] == ref[1] == ref[2] and ref[0]>1 : t = True
if 4 in ref or t == True:print("RIGHT")
elif 3 in ref:print("ALMOST")
else:print("NEITHER")