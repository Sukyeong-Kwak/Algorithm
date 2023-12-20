n, m = map(int, input().split())

trees = list(map(int, input().split()))

def sumOfTree(h):
    cnt = 0
    for tree in trees:
        if tree-h > 0:
            cnt += tree-h
    
    return cnt
    
s = 1
e = max(trees) - 1
result = 0

while s <= e:
    mid = (s+e)//2
    
    if sumOfTree(mid) >= m:
        s = mid + 1
    else:
        e = mid - 1


print(e)
