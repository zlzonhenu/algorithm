n = int(input())
rope = list(int(input()) for _ in range(n))

#각 로프가 들수있는 무게를 내림차순
rope.sort(reverse=True)

# 최대중량
ww =0

#결국 뽑은 로프 중에 들수있는 무게가 가장작은 로프의 무게와 로프수로 최대중량이 결정된다.
for i, k in enumerate(rope):
    w = (i+1) * k
    if w > ww:
        ww = w
print(ww)

