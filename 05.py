a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21]
ret = []
for x in a:
    if x in b:
        ret.append(x)
print(ret)