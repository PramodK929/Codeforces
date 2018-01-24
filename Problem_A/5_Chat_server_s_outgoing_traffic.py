import sys
c = t = 0
for l in sys.stdin:
    if l!=exit():
        c += l[0] == '+'
        c -= l[0] == '-'
        if ':' in l: t += c * (len(l) - l.find(':') - 2)
print(t)