def my_solution(key, lock):
    def rotate_matrix(matrix):
        n = len(matrix)  # 행의 길이 -> 열의 갯수
        m = len(matrix[0])  # 열의 길이 -> 행의 갯수

        result = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = matrix[i][j]
        return result

    # 모든 자물쇠의 값이 1인지 확인하는 함수
    def check(key_length, lock_length, new_lock):
        # key_length, lock_length, new_lock
        for i in range(key_length - 1, key_length + lock_length - 1):
            for j in range(key_length - 1, key_length + lock_length - 1):
                if new_lock[i][j] != 1:
                    return False
        return True

    n = len(lock)
    m = len(key)

    # 자물쇠 크기 확장
    new_lock = [[0] * (n + (m - 1) * 2) for _ in range((n + (m - 1) * 2))]

    # 새로운 자물쇠 가운데에 lock 위치하게 함
    for i in range(n):
        for j in range(n):
            new_lock[m + i - 1][m + j - 1] = lock[i][j]

    for rotation in range(4):
        # 열쇠 한 칸씩 움직이기
        key = rotate_matrix(key)
        for x in range(n + m - 1):
            for y in range(n + m - 1):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(n, m, new_lock) is True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


print(my_solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
