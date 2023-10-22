# def solution(wallpaper):
#     answer = [51, 51, 0, 0]
#     lux, luy, rdx, rdy = 0, 1, 2, 3
#
#     for index_i, i in enumerate(wallpaper):
#         for index_j, j in enumerate(i):
#             if j == "#":
#                 answer[lux] = min(answer[lux], i)
#                 answer[luy] = min(answer[luy], j)
#                 answer[rdx] = max(answer[rdx], i+1)
#                 answer[rdy] = max(answer[rdy], j+i)
#
#     return answer
#
# print(solution([".#...", "..#..", "...#."]))

n = 4
m = 3
array = [[0] * m for _ in range(n)]

print(array)