'''
t(0) = 1
t(n) = t(0)*t(n-1) + t(1)*t(n-2) + ... + t(n-1)*t(0)
0 <= n <= 35

'''
arr = [0 for _ in range(36)]
arr[0] = 1

n = int(input())

for i in range(n):
    for j in range(i+1):
        arr[i+1] += arr[j]*arr[i-j]
print(arr[n])