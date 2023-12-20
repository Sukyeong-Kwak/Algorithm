n = int(input())

arr = sorted(list(map(int, input().split())))

x = int(input())


# 두 개의 마우스 커서, 포인터
s = 0
e = n-1
cnt = 0

while s < e:
    if arr[s]+arr[e] > x:
        e -= 1
    elif arr[s]+arr[e] == x:
        s += 1; e -- 1; cnt += 1
    else:
        s += 1

print(cnt)