# 1로 만들기

if __name__ == '__main__':
    X = int(input())
    dp_table = [0] * (X + 1)

    # 탑 다운 방식
    def solution(x):
        if x == 1:
            return 0

        if dp_table[x] != 0:
            return dp_table[x]

        temp_5, temp_3, temp_2 = int(1e9), int(1e9), int(1e9)

        if x % 5 == 0:
            temp_5 = solution(x // 5)
        if x % 3 == 0:
            temp_3 = solution(x // 3)
        if x % 2 == 0:
            temp_2 = solution(x // 2)


        dp_table[x] = min(temp_5, temp_3, temp_2, solution(x - 1)) + 1
        return dp_table[x]

    print(solution(X))