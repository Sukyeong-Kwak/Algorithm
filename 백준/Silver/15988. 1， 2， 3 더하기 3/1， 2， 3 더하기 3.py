dp = [1, 2, 4]
    
TC = int(input())

for i in range(TC):
    n = int(input())
    m = len(dp)
    if n > m:
        for i in range(m, n+1):
            dp.append((dp[-1]+dp[-2]+dp[-3])%1000000009)
    print(dp[n-1])