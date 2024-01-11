n = int(input())
p = list(map(int, input().split()))

# p 를 sort 
p.sort() # [1,1,2,2,3]
add = answer = 0
for x in p:
    add += x # 1 1+1 1+1+2 ..
    answer += add # 1+ (1+1) + (1+1+2) + 
print(answer)