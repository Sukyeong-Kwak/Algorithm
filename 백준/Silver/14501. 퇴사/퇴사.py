def recur(idx):
    global dp
    
    if idx == N:
        return 0

    if idx > N:
        return -9999999999
        
    if dp[idx] != -1:
        return dp[idx]
    
    dp[idx] = max(recur(idx + cons[idx][0]) + cons[idx][1], recur(idx+1))
    
    return dp[idx]
            
N = int(input())

cons = [list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N)]

recur(0)

print(max(dp))