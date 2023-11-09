n = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]

for i in range(1, n):
    dp.append(max(seq[i]+dp[i-1], seq[i]))

print(max(dp))