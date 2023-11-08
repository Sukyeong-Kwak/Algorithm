n = int(input())
cost = list(map(int, input().split()))

max_cost = [0]*(n)

for i in range(1, n+1):
    max_value = cost[i-1]
    for j in range(1, i//2+1):
        max_value = max(max_cost[i-j-1]+max_cost[j-1], max_value)
    max_cost[i-1] = max_value

print(max_cost[-1])