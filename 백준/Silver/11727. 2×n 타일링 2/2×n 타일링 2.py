n = int(input())

dp = [0, 1, 3]

for i in range(2, n):
    dp.append(dp[-1]+2*dp[-2])

print(dp[n]%10007)