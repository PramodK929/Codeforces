n = int(input())
a = input().split()
team_a = []
team_b = []
arr = sorted(a)
#print(arr)
for i in range(0, len(a)//2):team_b.append(arr[i])
for i in range(len(a)//2, len(a)):team_a.append(arr[i])
# print(team_a, team_b)
# print(team_a[0] , team_b[-1])
if(arr[len(arr)//2] > arr[len(arr)//2-1]):
    print("YES")
else:
    print("NO")