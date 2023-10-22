# 효율적인 화폐 구성

if __name__ == "__main__":
    N, M = input().split()
    toggle = False
    money_arr = []
    d = [10001] * 10001 # dp table

    for i in range(N):
        money_arr.append(input())

    for i in range(1, len(money_arr)):
        