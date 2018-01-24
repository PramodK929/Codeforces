hh, mm = input().split(':')
h, m = int(hh), int(mm)
x = int(m)
count = 0
count1 = 0
if h == 23 and m == 59:
    count = 1
else:
    while hh != mm[::-1]:
        if m > 59:
            h += 1
            count1 += 1
        elif m<60:
            m+=1
            count += 1
        else:
            count = 1
            break
        if int(hh)<10:hh = '0'+str(h)
        else:hh = str(h)
        if int(mm)<10:mm = '0'+str(m)
        else:mm = str(m)
# if count1 == 0:
#     print(count +  count1)
# else:
#     print((count-x) + count1)
print(count+(count1*60))