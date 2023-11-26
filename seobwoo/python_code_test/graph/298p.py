# 팀 결성

if __name__ == '__main__':
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]


    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    n, m = map(int, input().split())
    parent = [0] * (n + 1) # 부모 테아블 초기화

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(0, n + 1):
        parent[i] = i

    # 각 연산을 하나씩 확인
    for i in range(m):
        oper, a, b = map(int, input().split())

        # 합집합(union) 연산인 경우
        if oper == 0:
            union_parent(parent, a, b)
        #찾기(find) 연산인 경우
        elif oper == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")


# 입력
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1