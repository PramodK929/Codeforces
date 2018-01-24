n, d = map(int, input().split())
arr = [int(i) for i in input().split()]
ans = 0
for i in range(1, n):
    if arr[i]<=arr[i-1]:
        diff = abs(arr[i]-arr[i-1])
        ans += (diff//d)+1
        arr[i]+=d*((diff//d)+1)
print(ans)
            