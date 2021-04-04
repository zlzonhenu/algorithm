# n = int(input())
# A = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     A.append(a)
# max = 0
# for p in A:
#     uiq_p = set(p)
#     if len(list(uiq_p)) == 1:
#         res = 10000+list(uiq_p)[0]*1000
#     elif len(list(uiq_p)) == 2:
#         res = 1000+[x for x in p if x in list(uiq_p)][0]*100
#     elif len(list(uiq_p)) == 3:
#         res = sorted(list(uiq_p))[-1]*100
#     if res > max:
#         max = res
#
# print(max)
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = c*100
    if money > res:
        res = money
print(res)