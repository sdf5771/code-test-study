"""
볼링공 고르기
1 - M 볼링공 무게
두사람이 서로 무게가 다른 볼링공을 치려고 함 
서로 다른 공을 고르는 경우의 수 
"""
def mySolution():
    n, m = map(int, input().split())
    balls = list(map(int, input().split())) # 볼링공 무게 받기
    result = count_a = count_b = 0
    for weight_a in range(1, m + 1): # [ 1, 2, 3 ]
        for i in balls: # [1, 2, 2, 3, 3]
            if weight_a == i: # 1
                count_a += 1 # 1kg의 개수
            else:
                count_b += 1 # 남은 2키로, 3키로 개수
        result += count_a * count_b # 순열의 경우의 수
        count_a = count_b = 0
        # weight_b= len(list(filter(lambda x: x!= weight_a, balls)))
    print(result/2) # 순열 / 인원수(a, b 2명) -> 조합

def bookSolution():
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    arr = [0] * 11 # 무게별 가짓수
    result = 0
    for i in balls: #[1, 2, 2, 3, 3]
        arr[i] += 1 # arr 에 빈도수 적기 [ 0, 1, 2, 2 ]
    for j in range(1, m+1): # j = 1 , j = 2 
        n -= arr[j] # 5 - 1 = 4 , 4 - 2 = 2 
        result += arr[j] * n # 1 (볼링공 1kg ) * 4 (1kg 로 제외 후 공의 갯수)
        # 2가지(2kg) * 2가지(3kg)
    print(result)

bookSolution()
        
        