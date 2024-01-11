def my_solution():
    factor = input().split("-")
    before = sum(int(x) for x in factor.pop(0).split("+"))
    after = 0

    if factor:
        for y in factor:
            after += sum(int(i) for i in y.split("+"))
    print(before - after)


def other_solution():
    factor = input().split("-")
    chk = [x.split("+") for x in factor]
    print(f"{chk=}")

    a, *b = [sum(map(int, x.split("+"))) for x in factor]
    print(f"{a=}")
    print(f"{b=}")
    """
    접근 방식 
    1. 괄호로 최소의 값 ->  괄호를 활용해 - 가 등장하는 순간부터 모두 - 연산을 할수있는 것 임 
    2. "1+2-3+4-5" -> - 로 먼저 구분하고, 
    3. 처음 - 연산자가 등장한 부분을 기준으로 before - after = 연산 최솟값
    4. + 연산자를 기준으로 더하기 
    4-1. 0이 맨처음 등장하는 숫자가 있다. 
         eval 사용 불가 -> int("0009") -> 9 로 변환가능
         모든 요소를 string -> int 변환하는 로직이 필요
         map(int, factor)
    개선여지 
    1. 반복되는 코드를 줄일 수 있음
    sum(int(i) for i in y.split("+")) # 이처럼 반복되는 것이 중요
    """


print(other_solution())
