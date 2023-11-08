n = int(input())
cost = [0] + list(map(int, input().split()))

min_cost = [0]*(n+1)

for i in range(1, n+1):
    min_value = cost[i]
    for j in range(1, i//2+1):
        min_value = min(min_cost[i-j]+min_cost[j], min_value)
    min_cost[i] = min_value

print(min_cost[n])