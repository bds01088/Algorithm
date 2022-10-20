'''
#from datetime import datetime
#datetime 변환하는게 시간 제일 잡아먹는다.

import sys

import bisect

from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().strip().split())

querys = defaultdict(list)

for i in range(n):
    T, level = input().strip().split('#')
    #T = datetime.strptime(T, '%Y-%m-%d %H:%M:%S')
    querys[int(level)].append(T)
    
for i in range(m):
    startTime, endTime, level = input().strip().split('#')
    #ST = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
    #ET = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
    level = int(level)
    cnt = 0

    for i in range(level, 7):
        if i >= level and len(querys[i]) > 0:
            start_idx = bisect.bisect_left(querys[i], startTime)
            end_idx = bisect.bisect_right(querys[i], endTime)
            cnt += end_idx-start_idx
    print(cnt)
'''
import sys

from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().strip().split())

querys = defaultdict(list)

def BinarySearch(ls, start_target, end_target) :
    start = 0
    end = len(ls)-1
    while start <= end :
        mid = (start+end)//2
        if ls[mid] >= start_target :
            end = mid-1
        else :
            start = mid+1
    ans_start = start

    start = 0
    end = len(ls)-1
    while start <= end :
        mid = (start+end)//2
        if ls[mid] > end_target :
            end = mid-1
        else :
            start = mid+1
    ans_end = end

    return ans_end-ans_start+1
        


for i in range(n):
    T, level = input().strip().split('#')
    querys[int(level)].append(T)
    
for i in range(m):
    startTime, endTime, level = input().strip().split('#')
    level = int(level)
    cnt = 0

    for i in range(level, 7):
        if i >= level :
            cnt += BinarySearch(querys[i], startTime, endTime)

                
    print(cnt)


