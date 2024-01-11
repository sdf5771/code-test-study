import heapq


def book_solution(food_times, k):
    answer = 0
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # 시간이 짧은 순으로 정렬
        # heapq
        # [3,1,2]
        # (3,1), (1, 2), (2, 3)
        # q = [(1,2), (2,3), (3,1)]

    sum_value = 0
    previous = 0

    # food_times 의 합계가 k 보다 작으면 이제 return -1
    if sum(food_times) <= k:
        return -1

    # 작은 거 부터 다 빼봐
    length = len(food_times) # 3 
    # 현재 시간 - 이전에 돌아간 시간 * 남은 length 의 길이
    # (1초 - 0초 )* 3개 

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # (1, 2) (2, 3) # 지금 가장 먹는 시간이 짧은 애가 튀어나옴
        sum_value += (now - previous) * length # 2초짜리 (2 - 1초) * 2개 # 1초짜리를 다 먹는데 걸린 시간
        length -= 1 # 총 개수 - 다 먹은 원소 빼주기
        previous = now # 1

    result = sorted(q, key=lambda x: x[1])  # 여기 까지는 이해됨
    # [1, 2, 3, 4] 2 초% 4= 2
    return result[(k - sum_value) % length][1]

    return answer
