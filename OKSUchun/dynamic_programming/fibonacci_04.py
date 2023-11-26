d = [0] * 100

# 첫번째 , 두번째 항의 값을 지정
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n + 1):  # 1, 2 는 스킵 # 3 ~ n 까지 구현해야하므로
    d[i] = d[i - 1] + d[i - 2]


"""
[what I learned]
반복문으로 구현 :  bottom - up 
재귀문으로 구현 : top - down
 """
