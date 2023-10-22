def solution(park, routes):
    answer = []
    area = {}

    for index_i, i in enumerate(park):
        for index_j, j in enumerate(i):
            if j == "S":
                answer.append(index_i)
                answer.append(index_j)
                pass

            if j == "X":
                area[str(index_i) + '_' + str(index_j)] = "X"
                pass
            else:
                area[str(index_i) + '_' + str(index_j)] = "O"
                pass
    print(area)
    for i in routes:
        route, move = i.split(' ')

        for j in range(1, int(move) + 1):
            if route == 'N':
                if area.get(str(answer[0] - j) + '_' + str(answer[1])):
                    if area[str(answer[0] - j) + '_' + str(answer[1])] == 'O':
                        if j == int(move):
                            answer[0] -= int(move)
                    else:
                        pass
            elif route == 'S':
                if area.get(str(answer[0] + j) + '_' + str(answer[1])):
                    print(str(answer[0] + j) + '_' + str(answer[1]))
                    if area[str(answer[0] + j) + '_' + str(answer[1])] == 'O':
                        if j == int(move):
                            answer[0] += int(move)
                    else:
                        pass
            elif route == 'W':
                if area.get(str(answer[0]) + '_' + str(answer[1] - j)):
                    print(str(answer[0]) + '_' + str(answer[1] - j))
                    if area[str(answer[0]) + '_' + str(answer[1] - j)] == 'O':
                        if j == int(move):
                            answer[1] -= int(move)
                    else:
                        pass
            elif route == 'E':
                if area.get(str(answer[0]) + '_' + str(answer[1] + j)):
                    print(str(answer[0]) + '_' + str(answer[1] + j))
                    if area[str(answer[0]) + '_' + str(answer[1] + j)] == 'O':
                        if j == int(move):
                            answer[1] += int(move)
                    else:
                        pass

    print(answer)

    return answer