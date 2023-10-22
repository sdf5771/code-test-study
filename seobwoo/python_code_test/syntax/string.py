# 문자열 자료형
# 문자열 변수를 초기화할 때는 큰따옴표(")나 작은 따옴표(')를 이용합니다.
# 문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우가 있습니다.
# 전체 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있습니다.
# 전체 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 포함할 수 있습니다.
# 혹은 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있습니다.

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
# 문자열 변수에 덧셈(+)을 이용하면 문자열이 더해져서 연결(Concatenate)됩니다.
# 문자열 변수를 특정한 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해집니다.
# 문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있습니다.
# 다만 문자열은 특정 인덱스의 값을 변경할 수는 없습니다. (Immutable)
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

