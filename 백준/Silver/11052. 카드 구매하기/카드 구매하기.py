n = int(input())
cost = [0] + list(map(int, input().split()))

max_cost = [0]*(n+1)

for i in range(1, n+1):
    # 각각의 카드 장수마다 최대로 비싸게 사는 비용 계산
    ## 1장을 살 때 가장 비싸게 사는 비용, 2장을 살 때 가장 비싸게 사는 비용 ...
    max_value = cost[i]
    for j in range(1, i//2+1):
        # 각각의 카드 개수마다 비싸게 사는 비용을 계산해 놓았음
        # 카드를 가장 비싸게 사는 비용을 비교를 통해서 구함
        # 만약 7장을 산다고 한다면
        # 해당 카드를 통째로 사는 비용
        # 1장을 살 때 가장 비싸게 사는 비용 + 6장을 살 때 가장 비싸게 사는 비용
        # 2장을 살 때 가장 비싸게 사는 비용 + 5장을 살 때 가장 비싸게 사는 비용
        # 3장을 살 때 가장 비싸게 사는 비용 + 4장을 살 때 가장 비싸게 사는 비용
        # 이렇게 4가지 비용을 비교해서 가장 비싼 비용을 저장함
        max_value = max(max_cost[i-j]+max_cost[j], max_value)
    max_cost[i] = max_value

print(max_cost[n])
