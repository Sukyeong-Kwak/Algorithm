def numOfTwo(n):
    twos = 2
    while (twos <= n):
        twos *= 2
    
    result = 0
    nums = 0
    while (twos >= 1):
        nums= n // twos - n // (twos*2)
        result += nums*twos 
        twos //= 2
    return result

A, B = map(int, input().split())

print(numOfTwo(B)-numOfTwo(A-1))