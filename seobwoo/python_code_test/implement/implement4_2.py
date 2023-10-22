def solution(n):
    count = 0

    # minute_count = 0
    # second_count = 0
    # for i in range(60):
    #     parse_i = str(i)
    #     if len(parse_i) == 2:
    #         if parse_i[0] == '3' or parse_i[1] == '3':
    #             second_count += 1
    #             minute_count += 1
    #         else:
    #             continue
    #     else:
    #         if parse_i == '3':
    #             second_count += 1
    #             minute_count += 1
    #         else:
    #             continue
    #
    # minute_count *= n
    #
    # print('minute_count : ', minute_count)
    # print('second_count : ', second_count)
    # count = minute_count * second_count

    for h in range(n + 1):
        parse_h = str(h) # h 형변환 int -> str
        h_is_tens = True if len(parse_h) == 2 else False # h의 자리 수가 2자리면 True 아니면 False

        for m in range(60):
            parse_m = str(m) # m 형변환 int -> str
            m_is_tens = True if len(parse_m) == 2 else False # m의 자리 수가 2자리면 True 아니면 False

            for s in range(60):
                if h_is_tens:
                    if parse_h[0] == '3' or parse_h[1] == '3':
                        count += 1
                        continue
                else:
                    if parse_h == '3':
                        count += 1
                        continue

                if m_is_tens:
                    if parse_m[0] == '3' or parse_m[1] == '3':
                        count += 1
                        continue
                else:
                    if parse_m == '3':
                        count += 1
                        continue

                parse_s = str(s)
                s_is_tens = True if len(parse_s) == 2 else False

                if s_is_tens:
                    if parse_s[0] == '3' or parse_s[1] == '3':
                        count += 1
                        continue
                else:
                    if parse_s == '3':
                        count += 1
                        continue
                    else:
                        continue

    return count


if __name__ == '__main__':
    N = int(input())

    print('count: ',solution(N))