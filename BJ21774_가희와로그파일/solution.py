from datetime import datetime
import sys

from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().strip().split())

querys = defaultdict(list)

for i in range(n):
    T, level = input().strip().split('#')
    T = datetime.strptime(T, '%Y-%m-%d %H:%M:%S')
    querys[int(level)].append(T)
    
for i in range(m):
    startTime, endTime, level = input().strip().split('#')
    ST = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
    ET = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
    level = int(level)
    cnt = 0
    for i in range(level, 7):
        for j in range(len(querys[i])) :
            if ST <= querys[i][j] :
                cnt += len(querys[i][j:])
                break
    print(cnt)