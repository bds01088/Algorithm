import sys
from bisect import bisect
from collections import deque

input = lambda : sys.stdin.readline().strip()

n = int(input())

arr = list(map(int, input().split()))

# dp = [1]
# x = deque()
# x.append(arr[0])

# for i in range(1, n):
#     if arr[i] < x[0] :
#         x.appendleft(arr[i])
#         dp.append(dp[-1]+1)
#     else :
#         idx = bisect(x, arr[i])
#         x[idx-1] = arr[i]

# print(n-dp[-1])

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))