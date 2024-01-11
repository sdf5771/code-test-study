s=list(map(int,list(input())))
group = 1
for i in range(len(s)):
    if i == 0:
        pass
    else:
        past= s[i-1] 
        current = s[i]
        if past != current:
            group +=1
        else:
            continue
print(group//2)

