n = int(input())
adv = list(map(int, list(input().split())))
adv.sort()
result = count = 0

for i in adv:
    count += 1 
    if count >= i : 
        result +=1
        count = 0
print(result)