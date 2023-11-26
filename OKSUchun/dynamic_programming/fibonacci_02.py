# 피보나치 DP - 메모이제이션

if __name__ == "__main__":
    # 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
    d = [0] * 100

    # 탑다운 방식 = 재귀적 방식으로 DP 구현

    def fibo(x):
        # 종료 조건 명시
        if x == 1 or x == 2:
            return 1
        if d[x] != 0:  # 이미 계산한 결과라면, 계산된 값을 return
            return d[x]
        # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

    print(fibo(99))
