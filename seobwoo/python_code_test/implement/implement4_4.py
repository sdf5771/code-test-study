# 게임 개발

def solution():
    count = 0
    n, m = map(int, input().split()) # 맵의 크기 n * m
    a, b, d = map(int, input().split()) # 좌표 (a, b), 바라보는 방향 d

    # 북, 동, 남, 서
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    direction_index = d

    visited = [[0 for _ in range(n)] for _ in range(m)]

    # map 입력 받기
    game_map = []
    for _ in range(m):
        game_map.append(list(map(int, input().split())))

    # 초기 위치가 0이면 count + 1
    if game_map[b][a] == 0:
        count += 1
        visited[b][a] = 1

    while True:
        if direction_index >= 4: # 북, 동, 남, 서 순으로 방향을 전부 체크하면 break
            break

        if game_map[b + dy[direction_index]][a + dx[direction_index]] == 1 or visited[b + dy[direction_index]][a + dx[direction_index]] == 1:
            direction_index += 1 # 반 시계 방향으로 벡터 좌표이동
        else:
            count += 1 # 방문 카운트

            visited[b + dy[direction_index]][a + dx[direction_index]] = 1 # 방문 체크

            a = a + dx[direction_index] # 좌표 이동
            b = b + dy[direction_index] # 좌표 이동

            direction_index = 0 # 다시 북쪽에서부터 시작하게 초기화


    return count


if __name__ == "__main__":
    print('result : ', solution())