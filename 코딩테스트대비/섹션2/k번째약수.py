#입력
N, k = map(int, input().split())

# 내 방법
S = []
for i in range(1, N+1):
    s = N % i
    if s == 0:
        S.append(i)

if len(S) < k:
    print(-1)
else:
    print(S[k-1])
# 다른 방법
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

