# 미래 도시
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    INF = int(1e9) # 무한을 10억으로 초기화
    start = 1  # start node

    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받음
    for _ in range(m):
        # A에서 B로 양방향으로 서로 이동하는 비용은 1이라고 설정
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    # 노드 x와 최종 목적 노드 k를 입력받음
    x, k = map(int, input().split())

    # 점화식 D(ab) = min(D(ab), D(ak) + D(kb))에 따라 플로이드 워셜 알고리즘 실행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = graph[1][k] + graph[k][x] # 1 -> k까지의 거리와 k부터 x까지의 거리를 더한 값이 정답

    # 만약 result가 무한보다 크거나 같다면 도달할 수 없으므로 -1 출력
    if result >= INF:
        print("-1")
    # result가 무한보다 작다면 도달할 수 있으므로 값 출력
    else:
        print(result)


# 입력 값
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# [
#     [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
#     [1000000000, 0, 1, 1, 1, 2], [1000000000, 1000000000, 0, 1000000000, 1, 2],
#     [1000000000, 1000000000, 1000000000, 0, 1, 1],
#     [1000000000, 1000000000, 1000000000, 1000000000, 0, 1],
#     [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0]
# ]
