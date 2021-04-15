n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

tot=0
for i in range(n):
    if i <= int(n//2):
        k = i
    else:
        k = n-i-1
    for j in range(int(n//2)-k, int(n//2)+k+1):
        tot += a[i][j]

print(tot)


#또 다른 방법
res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)