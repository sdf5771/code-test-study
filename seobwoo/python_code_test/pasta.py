if __name__ == "__main__":
    pastaArr = []
    juiceArr = []

    for i in range(3) : pastaArr.append(int(input()))
    for i in range(2) : juiceArr.append(int(input()))

    result_array = []

    for i in range(3):
        for j in range(2):
            result_array.append(round((pastaArr[i] + juiceArr[j]) * 1.1, 1))

    result_array.sort()
    print(result_array[0])