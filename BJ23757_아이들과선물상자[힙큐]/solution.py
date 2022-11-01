import sys

import heapq

input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

boxs = list(map(int, input().split()))

reqs = list(map(lambda x : int(x)-1, input().split()))

heap = []

for box in boxs :
    heapq.heappush(heap, [-box, box])

flag = 0
for i in range(m):
    x = heapq.heappop(heap)
    if reqs[i] > x[1] :
        flag = 1
        print(0)
        break
    else :
        x[1] = x[1]-reqs[i]
        x[0] = -x[1]
        heapq.heappush(heap, x)
    
if not flag :
    print(1)

