ipt = [int(i) for i in input().split(' ')]
ipt.sort()
if ipt[0]+ipt[1]>ipt[2] or ipt[1]+ipt[2]>ipt[3]:print("TRIANGLE")
elif ipt[0]+ipt[1] == ipt[2] or ipt[1]+ipt[2] == ipt[3] or ipt[0]+ipt[2] == ipt[3] or ipt[0]+ipt[2] == ipt[1]:print("SEGMENT")
else:print("IMPOSSIBLE")