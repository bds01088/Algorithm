import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

di = {}

ans = []
for i in range(n):
    di[input().strip()] = 1

for i in range(m):
    x = input().strip()
    if di.get(x) :
        ans.append(x)

print(len(ans))
ans.sort()
for el in ans :
    print(el)