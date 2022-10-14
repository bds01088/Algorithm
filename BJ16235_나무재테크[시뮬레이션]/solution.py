'''
n, m, k가 들어오는데
n^2 = 땅의 크기
m = 나무 개수
k = 흘러갈 년수

초기 양분은 5로 고정
!
처음 입력 나무는 중복된 위치가 주어지지않음
!

봄 : 나무가 나이만큼 양분을 먹고, 나이가 1증가
    1칸에 여러 나무가 존재할 수 있으며, 나이가 어린 나무부터 양분을 먹는다
    양분이 부족하면 죽음
여름 : 죽은 나무의 나이를 //2한 값을 양분으로 추가함
가을 : 나무의 나이가 5의 배수인 것만 팔방향으로 나이가 1인 나무를 생성함
겨울 : 주어진 배열 땅의 양분만큼 증가됨

봄부터 시작하니까
'''

import sys

from collections import deque


input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

board = [[5 for _ in range(n)] for _ in range(n)]

treeList = [[deque() for _ in range(n)] for _ in range(n)]

Earr = []
for i in range(n):
    Earr.append(tuple(map(int, input().strip().split())))


for i in range(m):
    r, c, a = map(int, input().strip().split())
    treeList[r-1][c-1].append(a)


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


for year in range(k):
    #봄
    deadList = []

    for i in range(n):
        for j in range(n):
            for l in range(len(treeList[i][j])-1, -1, -1):
                if board[i][j] >= treeList[i][j][l] :
                    #나이증가
                    #양분 감소
                    board[i][j] -= treeList[i][j][l]
                    treeList[i][j][l] += 1
                else :
                    #양분이 부족하면 죽은 나무로 추가
                    for _ in range(l+1):
                        #여름 처리
                        board[i][j] += treeList[i][j].popleft()//2
                    #여름처리 끝난후 해당 위치 처리 마감
                    break

    
    #가을
    for i in range(n):
        for j in range(n):
            for p in range(len(treeList[i][j])):
                if treeList[i][j][p]%5 == 0:
                    for q in range(8):
                        nrow = i+dr[q]
                        ncol = j+dc[q]
                        if 0 <= nrow < n and 0 <= ncol < n :
                            treeList[nrow][ncol].append(1)
        
    #겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += Earr[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(treeList[i][j])
print(ans)