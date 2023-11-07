n = int(input())


dp = [-1]*(n+1)
dp[1] = 0;

for i in range(2, n+1):
    a = 100; b = 100;
    if i%3 == 0:
        a = dp[i//3] + 1
    if i%2 == 0:
        b = dp[i//2] + 1
    c = dp[i-1] + 1
    dp[i] = min(a, b, c)
    

print(dp[n])