# 플로이드
# 이코테 385p
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
INF = int(1e9)
if __name__ == '__main__':
    n = int(input())
    m = int(input())

    # 그래프를 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신까지 가는 거리를 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 시작 도시 a, 도착 도시 b, 필요 비용 c를 입력받고, 버스 노선은 하나가 아닐 수 있으므로 가장 짧은 거리를 a에서 b로 가는 비용을 c로 초기화
    for _ in range(m):
        a, b, c = map(int, input().split())

        if c < graph[a][b]:
            graph[a][b] = c

    # 플로이드 워셜 알고리즘을 실행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과 출력 graph[a][b]가 INF면 도달할 수 없으므로 0을 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print(0, end=" ")
            else:
                print(graph[a][b], end=" ")
        print()

# 입력값
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4