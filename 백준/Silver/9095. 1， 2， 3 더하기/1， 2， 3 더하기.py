dp = [1, 2, 4]

tolerance = 1

for i in range(3, 10):
    dp.append(dp[-1]+dp[-2]+dp[-3])
    
TC = int(input())

for i in range(TC):
    print(dp[int(input())-1])
