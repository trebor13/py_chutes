__author__ = 'Robert'
min = 0
ladders = list(range(0,101))
chutes = list(range(0,101))


def init():
    for i in range(0,101):
        ladders[i] = chutes[i] = 0



def next_square (start, count, ll, lc):
    global min

    square = start
    c = 0

    if count > min: return

    while True:
        c += 1
        if c > 6 :
            count += 1
            if count >= min: break
            c = 1

        square += 1
        if square >= 100 :
            break

        x = ladders[square]
        if (x != 0) and (x != ll):
            if x == 100: break
            next_square(x, count+1, x, lc)
            continue

        x = chutes[square]
        if (x != 0) and (x != lc):
            next_square(x, count+1, 11, x)
            continue

    if count < min:
        min = count


t = int(input())
for ii in range(0,t):
    init()

    n = int(input())
    for i in range(0,n):
        a,b = input().split()
        a,b = int(a),int(b)
        ladders[a] = b

    n = int(input())
    for i in range(0,n):
        a,b = input().split()
        a,b = int(a),int(b)
        chutes[a] = b

    for i in range(1,101):
        x = ladders[i]
        if (x < 100): chutes[x] = 0

    min = -1
    for i in range(94,100):
        if (chutes[i] == 0):
            min = 99
            next_square(1,1,0,0)
            break

    print(min)



