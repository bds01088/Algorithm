import heapq
import sys

input = sys.stdin.readline

def sth(num):
    global heap
    if num == 0 :
        try :
            result = heapq.heappop(heap)
            print(result)
        except IndexError :
            print(0)
    else :
        heapq.heappush(heap, num)
        return

n = int(input().strip())

heap = []

for i in range(n):
    x = int(input().strip())
    sth(x)
