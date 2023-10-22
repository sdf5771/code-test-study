# 선택 정렬
# 가장 원시적인 방법으로 매번 '가장 작은 것을 선택' 해서 맨 앞에 있는 데이터와 바꾸고, 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정

if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)