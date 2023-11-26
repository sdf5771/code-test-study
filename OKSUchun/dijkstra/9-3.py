INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기자신 0 으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 간선에 대한 정보 입력
for _ in range(m):
    (
        a,
        b,
        c,
    ) = map(int, inpu().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")

"""
플로이드 워셜 알고리즘
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 경우

1. 거쳐 가는 노드를 기준으로 알고리즘 수행
2. 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다. 
3. 노드의 개수가 N개일때, 알고리즘 상으로 n번의 단계 수행
4. 시간 복잡도 : O(N^2)

"""
