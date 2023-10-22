def solution(numbers):
    answer = [0] * len(numbers)
    stack = []

    print('1stack', stack)
    print('answer', answer)

    for i in range(len(numbers)):
        while stack and stack[-1] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            print('2stack', stack)
            print('2answer', answer)

    return answer