import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())

arr = []

for i in range(n):
    x = int(input().strip())
    if x == 0 :
        if len(arr) != 0 :
            print(heapq.heappop(arr)[1])
        else :
            print(0)
    else :
        heapq.heappush(arr, (abs(x), x))
    