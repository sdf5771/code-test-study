# 백준 12865
# 평범한 배낭

if __name__ == "__main__":

    N, K = map(int, input().split()) # 물품 갯수, 버틸 수 있는 무게

    # dp_table = [0] * (N + 1)
    # arr = [] # 물건 보관할 Array
    # arr.append(None)
    # for i in range(N):
    #     temp1, temp2 = map(int, input().split())
    #     obj = {
    #         "W": temp1,
    #         "V": temp2
    #     }
    #     arr.append(obj) # [{'W': 6, 'V': 13}] 딕셔너리 형태로 보관
    #
    # dp_table[0] = 0
    #
    # for i in range(1, len(arr)):
    #     if arr[i]['W'] > K:
    #         continue
    #     else:
    #         dp_table[i] = max()

    # x축에는 가방 1~k까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.
    stuff = [[0, 0]]
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for _ in range(N):
        stuff.append(list(map(int, input().split())))

    for i in range(1, N + 1): # 열
        for j in range(1, K + 1): # 행
            weight = stuff[i][0]
            value = stuff[i][1]

            if j < weight:
                # 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.
                knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다.
            else:
                # 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최대값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.
                # 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값 (knapsack[i-1][j])을 가져온다.
                # 둘 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

    print(knapsack[N][K]) # knapsack[N][K]는 K무게일 때의 최댓값