N, M = map(int, input().split())

cnt = [0 for _ in range(N+M+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1
max = 0
for x in range(N+M+1):
    if cnt[x] > max:
        max = cnt[x]

for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=" ")