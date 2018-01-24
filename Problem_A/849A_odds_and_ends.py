n = int(input())
arr = [int(i) for i in input().split()]
flag = True
if  arr[0]%2==0 or arr[-1]%2==0:
    flag = False
elif arr[0]%2!=0 and arr[-1]%2!=0 and len(arr)%2!=0:
    flag = True
else:
    for i in range(n-1, 0, -1):
        if i%2==0:
            if arr[i]%2==0:
                flag = False
                break
        elif (n-i)%2==0 and flag == False:
            flag = False
            break
if flag == True and n%2!=0:
    print("Yes")
else:print("No")
    
