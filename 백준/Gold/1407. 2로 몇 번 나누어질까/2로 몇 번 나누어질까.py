def numOfTwo(n):
    result = n
    twos = 2
    while (twos <= n):
        result += (n // twos) * (twos//2)
        twos *= 2
    return result

A, B = map(int, input().split())

print(numOfTwo(B) - numOfTwo(A-1))