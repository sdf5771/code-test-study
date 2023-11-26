import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력 받기
start = int(input())

graph = [[] for i in range(n + 1)]

print([] for i in range(n + 1))

# List comprehensioin
