def gcdIter(a, b):
    if a <= b:
        smallerInteger = a
    else:
        smallerInteger = b
    for i in range(smallerInteger,0,-1):
        if i == 1:
            return 1
        elif a % i == 0 and b % i == 0:
            return i
            
print(gcdIter(1, 12))