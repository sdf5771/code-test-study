# 개미 전사

if __name__ == '__main__':
    N = int(input())
    K = list(map(int, input().split()))

    result = 0
    toggle = False

    for i in range(N):
        if toggle:
            toggle = False
            continue
        else:
            if K[i] >= K[i + 1]:
                result += K[i]
                toggle = True
            else:
                result += K[i + 1]
                toggle = True

    print(result)