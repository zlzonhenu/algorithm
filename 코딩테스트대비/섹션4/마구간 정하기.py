n, m = map(int, input().split())
locs = []
for _ in range(n):
    loc = int(input())
    locs.append(loc)
locs.sort()
lt = 1
rt = locs[-1]
res = 0
while lt <= rt:
    cnt = 1
    mid = (lt+rt) // 2
    for i in range(1, n):
        dif = locs[i] - locs[0]
        if mid <= dif:
            cnt += 1
    if cnt < m:
        rt = mid - 1
    else:
        res = max(mid, res)
        lt = mid + 1

print(res)
