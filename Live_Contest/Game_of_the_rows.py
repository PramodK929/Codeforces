n, k = map(int, input().split(' '))
g = [int(i) for i in input().split(' ')]
seats = ['two1', 'four', 'two2']
for i in range(n):

remaining_seats = 0
advanced_seats = 0
for i in g:
    if i + remaining_seats<=2:
        seats[0] = 'full'
    elif i + remaining_seats<=6:
        seats[0] = 'full'
        seats[1] = 'full'
    elif i + remaining_seats <= 8:
        seats[0] = 'full'
        seats[1] = 'full'
        seats[2] = 'full'
    else:
        remaining_seats = i // 8
    seats = []
