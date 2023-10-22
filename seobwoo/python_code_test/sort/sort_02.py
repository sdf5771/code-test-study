# 성적이 낮은 순서로 학생 출력하기

if __name__ == "__main__":
    N = int(input())

    arr = []

    for _ in range(N):
        student = input().split()
        arr.append((student[0], int(student[1])))

    result = sorted(arr, key=(lambda data: data[1]))

    for i in result:
        print(i[0], end= ' ')