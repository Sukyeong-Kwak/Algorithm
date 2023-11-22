n, k = map(int, input().split())
seq = list(map(int, input().split()))


total = 0

for i in range(k):
    total += seq[i]
    
max_value = total

for i in range(n-k):
    total += (seq[i+k] - seq[i])
    max_value = total if total > max_value else max_value

print(max_value)