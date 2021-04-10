n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# for i in sorted(a+b):
#     print(i, end=' ')
i = 0
j = 0
res = []
while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
if i < n:
    res = res+a[i:]
if j < m:
    res = res+b[j:]

for r in res:
    print(r, end=' ')



