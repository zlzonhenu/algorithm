n, k = map(int, input().split())
money = list(int(input()) for _ in range(n))

#최소 동전 개수 구하기
coin_num = 0

for i in range(1, n+1):
    #가장 큰 금액을 하나씩 가져오기
    coin = money[-i]

    if k >= coin:
        num = k//coin
        k -= coin*num
        coin_num += num

print(coin_num)
