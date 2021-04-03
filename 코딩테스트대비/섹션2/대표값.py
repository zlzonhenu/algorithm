#입력
n = int(input())
p = list(map(int, input().split()))

ave = round(sum(p)/n)
min = 2147000000
for idx, x in enumerate(p):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)

