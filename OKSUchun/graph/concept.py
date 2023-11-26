"""
트리 자료구조 : 우선순위 큐를 구현하기 위해 최소 힙, 최대 힙 이용
최소 힙
- 부모 노드가 자식 노드보다 크기가 작은 자료 구조
- 트리 자료 구조

그래프 
- 방향 / 무방향 그래프
- 순환 / 비순환
- 루트 노드 없음
- 부모 / 자식 관계 없음
- 네트워크 모델

구현 방법
- 인접 행렬
- 인접 리스트

서로소 집합
- 중요 연산 : Union, find
- union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
- find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

서로소 집합 자료구조
- 트리 자료 구조를 이용한 집합 연산을 어떻게 구현하나
1. union 연산 -> 연결된 두 노드 확인
- A, B 의 루트 노드 : A`, B`

- A`를 B`의 부모 노드로 설정 ( B` -> `A)

1. 부모테이블 : 노드 별 부모 노드를 기록한 테이블
2. union 연산을 하며 부모테이블을 최신화 함
3. 최종적으로 루트를 찾기 위해서 계속해서 재귀적으로 부모를 거슬러 올라가야한다.

"""


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
