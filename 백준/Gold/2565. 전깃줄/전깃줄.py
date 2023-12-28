n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda arr:arr[1])
    
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i][0] > arr[j][0]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))