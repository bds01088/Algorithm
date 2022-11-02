import sys
from collections import defaultdict
import heapq

input = lambda : sys.stdin.readline().strip()

T = int(input())

for _ in range(T):
    N = int(input())
    max_heap = []
    min_heap = []

    record = defaultdict(int)

    for i in range(N):
        order, num = input().split()
        num = int(num)
        if order == 'I' :
            record[num] += 1
            heapq.heappush(max_heap, (-num, num))
            heapq.heappush(min_heap, num)
        else :
            try :
                if num == 1 :
                    target = heapq.heappop(max_heap)[1]
                    while record[target] == 0 :
                        target = heapq.heappop(max_heap)[1]
                    record[target] -= 1
                else :
                    target = heapq.heappop(min_heap)
                    while record[target] == 0 :
                        target = heapq.heappop(min_heap)
                    record[target] -= 1
            except IndexError :
                max_heap = []
                min_heap = []

    flag1 = 1
    flag2 = 1

    try :
        mmax = heapq.heappop(max_heap)[1]
        while record[mmax] == 0 :
            if len(max_heap) == 0 :
                flag1 = 0
                break
            mmax = heapq.heappop(max_heap)[1]
        
        mmin = heapq.heappop(min_heap)
        while record[mmin] == 0 :
            if len(min_heap) == 0 :
                flag2 = 0
                break
            mmin = heapq.heappop(min_heap)
    except IndexError :
        flag1 = 0
        flag2 = 0

    
    if flag1*flag2 == 1 :
        print(f"{mmax} {mmin}")
    else :
        print("EMPTY")

            
