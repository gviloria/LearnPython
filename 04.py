number = int(input("Enter a number: "))
# range is (inclusive, exclusive) so add 1
num_range = range(1,(number/2) + 1)
ret = []
for n in num_range:
    if number % n == 0:
        ret.append(n)
print(ret)