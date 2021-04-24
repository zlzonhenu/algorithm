import sys
sys.stdin = open("input.txt", "r")
a = [list(map(int, input().split())) for _ in range(7)]

cnt=0
for i in range(7):
    for j in range(3):
        b = []
        c = []
        for m in range(j, j + 5):
            #row
            b.append(a[i][m])
            #colum
            c.append(a[m][i])
        if b[0] == b[-1]:
            if b[1]==b[-2]:
                cnt += 1
        if c[0]==c[-1]:
            if c[1]==c[-2]:
                cnt += 1
print(cnt)
