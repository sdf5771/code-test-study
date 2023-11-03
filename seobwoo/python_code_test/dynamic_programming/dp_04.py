# 효율적인 화폐 구성

if __name__ == "__main__":
    N, M = input().split()
    toggle = False
    money_arr = []
    d = [10001] * (M * 1) # dp table

    for i in range(N):
        money_arr.append(input())

    d[0] = 0 # 0원은 0

    for i in range(N):
        for j in range(money_arr[i], M + 1):
            if d[j - money_arr[i]] != 10001:
                d[j] = min(d[j], d[j - money_arr[i]] + 1)

    if d[M] == 10001:
        print(-1)
    else:
        print(d[M])