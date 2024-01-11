# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

given = list(input())

# 알파벳 구분
chr_list = sorted(list(filter(lambda x: x.isalpha(), given)))

# numlist isdigit()
num_list = [int(x) for x in given if x.isdigit()]

# 숫자가 없는 경우 0 이 아닌 공백 출력하도록 예외처리
sum_num = sum(num_list) if sum(num_list) > 0 else ""


answer = "".join(chr_list) + str(sum_num)
print(f"{answer=}")
