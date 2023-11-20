# 정확한 순위
# 386p
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받고, a에서 b로 가는 비용을 1로 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    # 플로이드 워셜 알고리즘에 따라 3중 반복문 내에서 점화식을 실행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 성적 순위를 정확하게 알 수 있는 학생의 수
    result = 0

    # 각 학생들 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
    for a in range(1, n + 1):
        count = 0
        for b in range(1, n + 1):
            # 해당 학생이 다른 학생보다 성적이 낮거나, 높을 경우를 모두 카운팅
            if graph[a][b] != INF or graph[b][a] != INF:
                count += 1

        # 해당 학생보다 성적이 낮거나 높은 학생들의 합이 본인을 포함해서 n과 같다면
        # 해당 학생의 정확한 순위를 알 수 있음
        if count == n:
            result += 1

    print(result)


# 입력값
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
