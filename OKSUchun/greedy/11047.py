n, k = map(int, input().split())
coin = []
cnt = 0
# 인수 입력
for _ in range(n):
    coin.append(int(input()))

coin.reverse()
for i in coin :
    cnt += k//i
    k %= i
print(cnt)