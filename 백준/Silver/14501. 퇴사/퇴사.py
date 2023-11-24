def recur(idx, cost):
    global max_cost
    
    if idx == N:
        max_cost = max(max_cost, cost)
        return
   
    if idx > N:
        return
    
    recur(idx + cons[idx][0], cost + cons[idx][1])
    recur(idx+1, cost)
            
N = int(input())

cons = [list(map(int, input().split())) for _ in range(N)]

max_cost = 0

recur(0, 0)

print(max_cost)