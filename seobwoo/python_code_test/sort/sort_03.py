# 두 배열의 원소 교체

if __name__ == '__main__':
    result = 0
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break

    for i in A:
        result += i

    print(result)