import sys

n = int(sys.stdin.readline())

hints = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if (a == b) or (b == c) or (a == c):
                continue
            
            cnt = 0
            for hint in hints:
                number = hint[0]
                strike = hint[1]
                ball = hint[2]
                strike_count = 0
                ball_count = 0
                A, B, C = list(map(int, str(number)))
                if A == a: strike_count+=1
                if B == b: strike_count+=1
                if C == c: strike_count+=1
                if A == b or A == c: ball_count += 1
                if B == a or B == c: ball_count += 1
                if C == a or C == b: ball_count += 1

                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == n: answer += 1

print(answer)