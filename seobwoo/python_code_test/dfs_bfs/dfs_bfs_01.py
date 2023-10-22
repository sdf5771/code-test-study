# 음료수 얼려 먹기
if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input())))

    count = 0 # result

    def dfs(x, y):
        # 상하좌우 범위를 넘어가는가
        if x <= -1 or x >= N or y <= -1 or y >= M:
            return False

        if graph[x][y] == 0:
            # 방문처리
            graph[x][y] = 1

            # 상하좌우 순서로 재귀호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                count += 1

    print('result : ', count)