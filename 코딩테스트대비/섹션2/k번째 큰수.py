#입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
#set()은 중복자동제거 리스트
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
