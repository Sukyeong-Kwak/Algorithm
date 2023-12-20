n = int(input())
card = sorted(list(map(int, input().split())))

m = int(input())
check = list(map(int, input().split()))

for number in check:
    s = 0
    e = n-1
    flag = False
    
    while s <= e:
        mid = (s+e)//2
        if number == card[mid]:
            flag = True
            break
        elif number > card[mid]:
            s = mid+1
        else:
            e = mid-1
    print(int(flag), end=" ")