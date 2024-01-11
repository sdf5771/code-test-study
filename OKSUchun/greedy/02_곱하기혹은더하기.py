s = list(map(int,list(input())))
result = 0
for index, x in enumerate(s):
    if index == 0:
        result = x
    else:
        add = result + x
        multiply = result * x
        if add >= multiply:
            result = add
        else:
            result = multiply

print(result)
