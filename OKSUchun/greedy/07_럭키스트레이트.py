n = input()
sum1 = sum2 = 0
half= int((len(n)/2))
for i in range(half):
    sum1 += int(n[i])
for j in range(half, len(n)):
    sum2 += int(n[j])
print("LUCKY") if sum1 == sum2 else print("READY")
