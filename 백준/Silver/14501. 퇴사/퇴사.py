N = int(input())

cons = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

for idx in range(N)[::-1]:
    
    
    if idx + cons[idx][0] > N:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + cons[idx][0]] + cons[idx][1], dp[idx+1])

print(dp[0])