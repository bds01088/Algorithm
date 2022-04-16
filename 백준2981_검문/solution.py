'''
주어지는 n 개의 수 모두가
임의의 수로 나누었을때 나머지가 모두 같은 경우
그 임의의 수를 모두 출력하라
'''


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