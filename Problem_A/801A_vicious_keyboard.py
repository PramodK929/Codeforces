str = input()
count , p1, p2= str.count("VK"), 'VV', 'KK'
print(count+1 if p1 in str or p2 in str else count)
