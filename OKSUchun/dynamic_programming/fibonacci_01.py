# 피보나치 함수를 재귀로 구현
def fibo(x):
    if x == 1 or x == 2:  # x-1 , x-2 은 예외처리해주기
        return 1
    return fibo(x - 1) + fibo(x - 2)  # x-1 , x-2 > 0 이므로


if __name__ == "__main__":
    print(fibo(4))
