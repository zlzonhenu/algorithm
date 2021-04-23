#input
n = int(input())
z = [0 for _ in range(n+2)]
a = [z]
for m in range(n):
    x = list(map(int, input().split()))
    x.insert(0, 0)
    x.append(0)
    a.append(x)
a.append(z)



cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j] > a[i + 1][j]:
            if a[i][j] > a[i - 1][j]:
                if a[i][j] > a[i][j - 1]:
                    if a[i][j] > a[i][j + 1]:
                        cnt += 1
print(cnt)

#다른풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split()))]
a.insert(0, [0]*n)
a.append([0*n])
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)