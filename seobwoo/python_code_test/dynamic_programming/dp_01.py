# 1로 만들기
import time
if __name__ == '__main__':
    X = int(input())
    start = time.time()
    count = 0

    while True:
        if X == 1:
            break

        count += 1

        if X % 5 == 0:
            X = X / 5
            continue
        else:
            X -= 1
            continue

        if X % 3 == 0:
            X = X / 3
            continue
        else:
            X -= 1
            continue

        if X % 2 == 0:
            X = X / 2
            continue
        else:
            X -= 1
            continue


    print(count)
    end = time.time()

    print(f"{end - start:.5f} sec")