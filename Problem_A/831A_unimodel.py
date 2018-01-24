n = int(input())
arr = [int(i) for i in input().split(' ')]
i = 1
if len(arr) == 1:print("YES")
else:
    while i<n and arr[i-1]<arr[i]:i+=1
    while i<n and arr[i-1] == arr[i]:i+=1
    while i<n and arr[i-1]>arr[i]:i+=1
    print("YES" if i == n else "NO")