# 위에서 아래로

if __name__ == '__main__':
    N = int(input())

    array = []

    for _ in range(N):
        array.append(int(input()))

    result = sorted(array, reverse=True)

    for i in result:
        print(i, end=' ')