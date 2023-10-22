def solution(n, plan):

    # L R U D
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # character location
    x, y = 1, 1

    # 최소 좌표인 1보다 작으면 True, 그렇지 않으면 False
    def isMinValue(value, moveTo, index):
        if value + moveTo[index] < 1:
            return True
        else:
            return False

    # 최대 좌표인 'n'보다 크면 True, 그렇지 않으면 False
    def isMaxValue(value, moveTo, index, maxValue):
        if value + moveTo[index] > maxValue:
            return True
        else:
            return False

    for i in plan:
        if i == 'L':
            if isMinValue(x, dx, 0) or isMinValue(y, dy, 0) or isMaxValue(x, dx, 0, n) or isMaxValue(y, dy, 0, n):
                continue
            x += dx[0]
            y += dy[0]
        elif i == 'R':
            if isMinValue(x, dx, 1) or isMinValue(y, dy, 1) or isMaxValue(x, dx, 1, n) or isMaxValue(y, dy, 1, n):
                continue
            x += dx[1]
            y += dy[1]
        elif i == 'U':
            if isMinValue(x, dx, 2) or isMinValue(y, dy, 2) or isMaxValue(x, dx, 2, n) or isMaxValue(y, dy, 2, n):
                continue
            x += dx[2]
            y += dy[2]
        elif i == 'D':
            if isMinValue(x, dx, 3) or isMinValue(y, dy, 3) or isMaxValue(x, dx, 3, n) or isMaxValue(y, dy, 3, n):
                continue
            x += dx[3]
            y += dy[3]

    return f'{y} {x}'


if __name__ == "__main__":
    n = int(input())
    plan = map(str, input().split())

    print(solution(n, plan))