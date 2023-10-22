# 왕실의 나이트

def solution(n):
    count = 0

    matrix_x_key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    dx = [2, 1, -1, -2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    key_x = n[0]
    key_y = n[1]

    for i in range(8):
        if int(matrix_x_key[key_x]) + dx[i] < 1 or int(matrix_x_key[key_x]) + dx[i] < 8:
            continue
        if int(key_y) + dy[i] < 1 or int(key_y) + dy[i] < 8:
            continue
        count += 1

    return count


if __name__ == "__main__":
    N = input()

    print('result ', solution(N))