# from collections import deque
import sys
from itertools import permutations

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

inningList = []

for i in range(N):
    inningList.append(list(map(int, input().split())))

ans = 0
for xx in permutations(range(1,9)) :
    candiList = list(xx)
    candiList.insert(3, 0)
    score = 0
    j = 0
    
    for i in range(N):

        outCount = 0
        # runner = deque()
        base1 = False
        base2 = False
        base0 = False

        inning = inningList[i]

        while True :      
            if inning[candiList[j]] == 0 :
                outCount += 1
                if outCount >= 3:
                    j = (j+1)%9
                    break
            else :
                #실제야구와 달리 1루타 치면 다 1루 진루함
                #고로 3루가 차있어도 1루타 치면 진루함
                if inning[candiList[j]] == 1 :
                    if base2 :
                        score += 1
                        base2 = False
                    if base1 :
                        base2 = True
                        base1 = False
                    if base0 :
                        base1 = True
                    base0 = True

                if inning[candiList[j]] == 2 :
                    if base2 :
                        score += 1
                        base2 = False
                    if base1 :
                        score += 1
                        base1 = False
                    if base0 :
                        base2 = True
                        base0 = False
                    base1 = True
                
                if inning[candiList[j]] == 3 :
                    if base2 :
                        score += 1
                        base2 = False
                    if base1 :
                        score += 1
                        base1 = False
                    if base0 :
                        score += 1
                        base0 = False
                    base2 = True

                if inning[candiList[j]] == 4 :
                    if base0 :
                        score += 1
                        base0 = False
                    if base1 :
                        score += 1
                        base1 = False
                    if base2 :
                        score += 1
                        base2 = False
                    score += 1
                # runner.appendleft(inningList[i][candiList[j]])
                # for _ in range(inningList[i][candiList[j]]-1) :
                #     runner.appendleft(10)
            # while len(runner) >= 4 :
            #         x = runner.pop()
            #         if x == 10:
            #             continue
            #         else :
            #             score += 1
            j = (j+1)%9
    if score > ans :
        ans = score
print(ans)
                
