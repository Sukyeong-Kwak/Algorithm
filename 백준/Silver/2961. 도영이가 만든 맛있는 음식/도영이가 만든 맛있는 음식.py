def recur(idx, s, b, use):
    global answer
    
    if (idx == N):
        if use == 0: return
        answer = min(answer, abs(s-b))
        return
    
    recur(idx+1, s*ingre[idx][0], b+ingre[idx][1], use+1)
    
    recur(idx+1, s, b, use)

N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 9999999999999999

recur(0, 1, 0, 0)

print(answer)