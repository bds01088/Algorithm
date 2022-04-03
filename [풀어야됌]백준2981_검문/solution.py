# import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

# print(arr)
mmin = min(arr)
mmax = max(arr)

ans = []

for x in range(2, mmax+1):
    cnt = 1
    for i in range(1, n) :
        if arr[0]%x == arr[i]%x :
            cnt += 1
        else :
            break
    if cnt == n :
        ans.append(x)

for a in ans :
    print(a, end=' ')