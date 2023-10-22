# 떡볶이 떡 만들기
def binary_search(array, target, start, end, rice_cake_list):
    if start > end:
        return None
    mid = (start + end) // 2

    sum = 0

    for i in rice_cake_list:
        if i > array[mid]:
            sum = sum + (i - array[mid])

    if sum == target:
        return mid
    elif sum > target:
        return binary_search(array, target, mid + 1, end, rice_cake_list)
    else:
        return binary_search(array, target, start, mid - 1, rice_cake_list)

if __name__ == '__main__':
    N, M = map(int, input().split())
    rice_cake_list = list(map(int, input().split()))

    sort_list = sorted(rice_cake_list, reverse=True)

    array = []

    for i in range(sort_list[0] + 1):
        array.append(i)

    result = binary_search(array, M, 0, len(array) - 1, rice_cake_list)
    print(result)

