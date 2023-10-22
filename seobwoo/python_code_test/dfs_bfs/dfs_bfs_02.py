# 미로 탈출
from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input())))

    count = 0

    # 상하좌우 순 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]

    def bfs(x, y):
        queue = deque()
        #queue에 시작값 append
        queue.append((x, y))

        # queue가 빈 공간이 될 때까지 반복
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 공간을 벗어나는지 확인하고 벗어나면 다음 반복 실행
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                # 벽이 있는지 확인하고 벽이라면 다음 반복 실행
                if graph[nx][ny] == 0:
                    continue

                # 해당 노드를 처음 방문하면 거리 기록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        return graph[N - 1][M - 1]


    print(bfs(0, 0))