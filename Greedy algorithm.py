#큰수의 법칙
#p92
N, M, K = map(int, input().split())
number = list(map(int, input().split()))

#제일 큰수, 두번째로 큰수 정하기
number.sort()
first = number[-1]
second = number[-2]

sum = 0
while True:
    for i in range(K):#제일 큰수 K번 반복가능
        if M == 0:#M이 0이면 반복문 탈출
            break
        sum += first
        M -= 1
    if M == 0:
        break
    sum += second#두번째로 큰수 한번만 사용
    M -= 1

print(sum)

#다른 방법
#가장 큰수가 나오는 횟수
count = int(M / K+1)*K + M % K+1

sum = 0
sum += count*first
sum += (M-count)*second

print(sum)