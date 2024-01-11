def my_solution():
    n = int(input())
    k = int(input())
    board = [[0] * (n+1) for _ in range(n+1)]
    info = []
    direction = 0
    # 사과의 갯수
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    def turn(direction, c):
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        return direction
    
    l = int(input())

    for _ in range(l):
        x, c = input().split()
        info.append((int(x), c))

    x, y = 1, 1
    direction = 0
    time = 0
    index = 0

    board[x][y] = 2
    q = [(x,y)]
    
    # 오른쪽, 아래, 왼쪽, 위 -> 오른쪽 방향으로 회전시 움직임 방향 표시
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        nx = x + moves[direction][0]
        ny = y + moves[direction][1]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] !=2 :
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
            else:
                px, py = q.pop(0) # 기존의 꼬리를 제거
                board[px][py] = 1
                board[nx][ny] = 2 # 1로의 변화
                q.append((nx, ny))
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        
        if index < 1 and time == info[index][0]:
            direction = turn(direction , info[index][1])
            index += 1
            
    return time
print(my_solution())



def other_solution():
    n = int(input())
    k = int(input())
    data = [[0] * n for _ in range(n)]
    info = []

    # 맵 정보
    for _ in range(k):
        a, b = map(int, input().split()) 
        data[a][b] = 1 # 이차행렬에 표시

    l = int(input()) # 방향 전환 하는 횟수
    for _ in range(l):
        x, c = input().split()
        info.append((int(x), c)) # 방향 전환하는 시간, 전환 방향

    dx = [0 ,1, 0, -1] # 방향 전환 시, 좌표 이동 방향 확인
    dy = [1 ,0 ,-1, 0]

    def turn(direction, c):
        if c == "L":
            direction = (direction -1) % 4 # 역방향
        else:
            direction = (direction +1 ) % 4 # 정방향
        return direction
    
    def simulate():
        x, y = 1, 1 # 시작 지점 
        data[x][y] = 2 # 현재 뱀이 위치한 곳은 2로 표기 
        direction = 0 # 방향
        time = 0 # 시간
        index = 0 # 다음에 회전할 정보
        q = [(x, y)] # 뱀이 차지하고 있는 위치 정보 list 로 구현
        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 1 <= nx and nx <= n  and 1 <= ny and ny <= n and data[nx][ny] != 2:
                if data[nx][ny] == 0: #사과가 없다면 꼬리를 제거
                    data[nx][ny] = 2
                    q.append((nx,ny)) # 이동 좌표 append 
                    px, py = q.pop(0) # 이전 좌표를 pop 함
                    data[px][py] = 0
                if data[nx][ny] == 1:
                    data[nx][ny] = 2
                    q.append((nx,ny)) # 새로운 좌표를 append 만 함
            else:
                time+= 1 # nx 가 map 밖에 있을 경우, 
                break
            time += 1
            if index <1 and time == info[index][0]:
                direction = turn(direction, info[index][1])
                index += 1
        return time
    print(simulate())