import math

n = int(input())

dp = [0, 1]


for i in range(2, n+1):
    min_values = []
    for j in range(1, int(math.sqrt(i))+1):
        min_values.append(dp[i-j**2]+1)
    dp.append(min(min_values))
    
print(dp[n])