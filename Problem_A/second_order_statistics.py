n = int(input())
arr = [int(i) for i in input().split(' ')]
arr.sort()
if arr.count(min(arr)) == len(arr):print("NO")
else:print(arr[arr.count(min(arr))])