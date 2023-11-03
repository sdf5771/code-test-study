# 전보
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9) # 무한으로 10억 값 초기화
if __name__ == "__main__":
    n, m, c = map(int, input().split()) # 도시의 개수 n, 통로의 개수 m, start node c

    graph = [[] for i in range(n + 1)] # 각 노드들의 정보를 담을 리스트

    distance = [INF] * (n + 1) # 최단 경로 테이블 무한으로 초기화

    for _ in range(m):
        # x 에서 y로 이어지는 통로가 있고 비용은 z이다
        x, y, z = map(int, input().split())
        graph[x].append((y, z))


    def dijkstra(start):
        q = []

        heapq.heappush(q, (0, start)) # 시작노드에서 출발하는 비용은 0
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            # 이미 방문했다면 무시
            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(c)

    # 도달할 수 있는 노드 개수
    count = 0

    # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
    max_distance = 0
    for d in distance:
        # 도달할 수 있는 노드인 경우
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)

    # 시작 노드는 제외해야 하므로 count - 1을 출력
    print(count - 1, max_distance)