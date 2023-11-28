def recur(idx, weight):
    global dp
    
    if weight > K:
        return -99999999
    
    if idx == N:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight] 
    
    dp[idx][weight] = max(recur(idx+1, weight + goods[idx][0]) + goods[idx][1], recur(idx+1, weight))
    
    return dp[idx][weight]
            
N, K = map(int, input().split())

goods = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(K+1)] for _ in range(N)]

print(recur(0, 0))
