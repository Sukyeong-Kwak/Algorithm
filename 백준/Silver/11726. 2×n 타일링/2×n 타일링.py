n = int(input())

dp = [0, 1, 2, 3]

for i in range(3, n):
    dp.append(dp[-1]+dp[-2])

print(dp[n]%10007)