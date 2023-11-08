# t(0) = 1, t(1) = 2, t(3) = 4
dp = [1, 2, 4]

tolerance = 1

for i in range(3, 10):
    # 해당 점화식 : t(n) = t(n-1) + t(n-2) + t(n-3) 
    dp.append(dp[-1]+dp[-2]+dp[-3])
    
TC = int(input())

for i in range(TC):
    print(dp[int(input())-1])
