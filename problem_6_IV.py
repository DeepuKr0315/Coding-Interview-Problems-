# The following code performs integer division. What is its runtime (assume a and b are both positive)?

def division(a, b):
    sum = b
    count = 0
    while(sum <= a):
        sum += b
        count += 1
    return count

print(division(5, 2))