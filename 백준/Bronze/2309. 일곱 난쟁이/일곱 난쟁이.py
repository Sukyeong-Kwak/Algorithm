import sys

heights = sorted(list(map(lambda x: int(x[:-1]), sys.stdin.readlines())))

liar1 = 0
liar2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if (sum(heights) - heights[i] - heights[j]) == 100:
            liar1 = i
            liar2 = j

for i in range(9):
    if (i != liar1 and i != liar2):
        print(heights[i])