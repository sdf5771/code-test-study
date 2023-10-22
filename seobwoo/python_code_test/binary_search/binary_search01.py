# 부품 찾기
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))

    M = int(input())
    M_list = list(map(int, input().split()))

    result_array = []

    N_list.sort()

    for i in M_list:
        result = binary_search(N_list, i, 0, N)
        if result == None:
            result_array.append('no')
        else:
            result_array.append('yes')

    for i in result_array:
        print(i, end=' ')