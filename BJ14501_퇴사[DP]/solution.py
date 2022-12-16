n = int(input())

arr = [[0,0]]
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

mmax = 0
for i in range(n, 0, -1):
    time = arr[i][0]+i-1
    if time <= n :
        dp[i-1] = max(arr[i][1]+dp[time], mmax)
        mmax = dp[i-1]
    else :
        dp[i-1] = mmax
    
print(dp[0])

# n = int(input())
# t = []
# p = []
# dp = [0]*(n+1)
# mmax = 0

# for _ in range(n):
#     x, y = map(int, input().split())
#     t.append(x)
#     p.append(y)

# for i in range(n-1, -1, -1):
#     time = t[i]+i
#     if time <= n :
#         dp[i] = max(p[i] + dp[time], mmax)
#         mmax = dp[i]
#     else : 
#         dp[i] = mmax
# print(dp)