def my_solution(s):
    answer = []
    n = len(s)
    for step in range(1, n // 2):  # 압축하는 문자열의 갯수
        # aabbcc
        prev = s[0:step]
        compressed = ""

        for j in range(step, n, step): # (2, 12,2) [10, 12]
            if prev == s[j : j + step]:  # 현재의 앞에 있는거 s[2,4] = aa
                count += 1 # 2 
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
                # compressed = 2aa2bb + 2cc
        compressed += str(count) + prev if count >= 2 else prev
                # prev = aa s[4,6] = bb count = 2 2aa
        # answer.append(compressed)
        answer.append(len(compressed))
        
    return min(answer)


def other_solution(s):
    """
    접근 방식
    처음 prev = s[j: j +step] 으로 만들어놓고,
    for j in range(step, len(s), step)
    - 접근 방식을 확인하면, len(s) ##
    - 압축할 수 있다면,
    if prev == s[j: j+step]:
        count += 1
    else:
        compressed += str(count) + prev


    - 압축할 수 없다면, compressed += str(count) + prev if count>=2 else prev
    """
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j : j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


# 출처: https://ljhyunstory.tistory.com/18 [오늘도 열시미!:티스토리]

print(other_solution("abcdabcdeabcdabcd"))
