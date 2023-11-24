def recur(idx, p, f, s, v, c, use):
    global cost, choices
    
    if (idx == N):
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if c < cost:
                cost = c
                choices = [use]
            elif c == cost:
                choices.append(use)
        return

    
    recur(idx+1, p + values[idx][0], f + values[idx][1], s + values[idx][2], v + values[idx][3], c + values[idx][4], use+[idx+1])
    
    recur(idx+1, p, f, s, v, c, use)


N = int(input())
mp, mf, ms, mv = map(int, input().split())
values = [list(map(int, input().split())) for _ in range(N)]

cost = 9999999999999999
choices = []


recur(0, 0, 0, 0, 0, 0, [])

choices.sort()

if len(choices) == 0: print(-1)
else:
    print(cost)
    print(*choices[0])