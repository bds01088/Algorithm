'''
n과 m이 주어지고
n개의 수가 들어온다
연속되는 수의 합에서
m이 되는 경우의 수를 구하자
'''

n, m = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
idx = 0
while idx < n :
    s = 0
    for i in range(idx, n):
        s += arr[i]
        if s > m :
            break
        elif s == m :
            cnt += 1
            break
    idx += 1

print(cnt)