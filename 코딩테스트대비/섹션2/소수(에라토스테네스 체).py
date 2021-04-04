#입력
N = int(input())

# res = 0
# for i in range(2, N+1):
#     cnt = 0
#     for j in range(2, i+1):
#         if i % j == 0:
#             cnt += 1
#
#     if cnt == 1:
#         res += 1
# print(res)
ch=[0]*(N+1)
cnt = 0
for i in range(2, N+1):
    if ch[i] == 0:
        cnt+=1
        for j in range(i, N+1, i):
            ch[j] = 1
print(cnt)
