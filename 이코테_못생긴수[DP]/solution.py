n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 1

i2, i3, i5 = 0, 0, 0
n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(n2, n3, n5)
    if dp[i] == n2:
        i2 += 1
        n2 = dp[i2]*2
    if dp[i] == n3:
        i3 += 1
        n3 = dp[i3]*3
    if dp[i] == n5:
        i5 += 1
        n5 = dp[i5]*5
print(dp)