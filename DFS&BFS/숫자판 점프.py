# 2차원 리스트의 맵 정보 입력 받기
graph = [list(map(str, input().split())) for _ in range(5)]

def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    dx = [1, -1, 0, 0] #상하좌우 확인 x
    dy = [0,  0, 1, -1] #상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if 0 <= ddx < 5 and 0 <= ddy < 5:#범위내에 있는지 확인
            dfs(ddx, ddy, number + graph[ddx][ddy]) #6글자될때까지 재귀


result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(result))
