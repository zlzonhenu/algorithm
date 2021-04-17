n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]


for i in range(m):
    src = a[b[i][0]-1] + a[b[i][0]-1]
    #왼쪽
    if b[i][1] == 0:
        a[b[i][0]-1] = src[b[i][2]:b[i][2]+n]
    else:
        a[b[i][0]-1] = src[-b[i][2]-n:-b[i][2]]

tot = 0
for j in range(n):
    if j <= int(n//2):
        for x in a[j][j:n-j]:
            tot += x
    else:
        for x in a[j][-j-1:j+1]:
            tot += x

print(tot)

#또 다른 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)