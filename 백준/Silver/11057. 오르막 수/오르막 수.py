import copy

n = int(input())

before_arr = [1] * 10
after_arr = [1] * 10


for i in range(n-1):
    for i in range(10):
        after_arr[i] = sum(before_arr[i:]) 
    before_arr = copy.deepcopy(after_arr)

print(sum(after_arr)%10007)