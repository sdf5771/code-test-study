# 선택 정렬 (Selection Sort)
# 데이터가 무작위로 여러 개 있을 때, 이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정

def solution():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스와프

    return array

if __name__ == '__main__':
    print('Result : ', solution())