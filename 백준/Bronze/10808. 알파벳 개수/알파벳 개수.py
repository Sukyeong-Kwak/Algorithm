import sys 

inputs = sys.stdin.readline().strip()

result = [0] * 26

for char in inputs:
    result[ord(char)-97] += 1

print(' '.join(list(map(str, result))))
