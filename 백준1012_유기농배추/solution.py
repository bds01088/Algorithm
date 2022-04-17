'''
1은 배추심어진 땅
배추심어진 땅 개수만큼 출력

tc가 맨처음 주어짐
'''

import sys
sys.stdin = open('input.txt')
from collections import deque


def BFS(srow, scol):
    q = deque()
    q.append([srow, scol])
    visit[srow][scol] = 1

    while q :
        row, col = q.popleft()
        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] == 0 and board[nrow][ncol] == 1:
                q.append([nrow,ncol])
                visit[nrow][ncol] = 1
    return 0

dr = [-1,1,0,0]
dc = [0,0,-1,1]

ans = []
tc = int(input())
for t in range(tc):
    n, m, k = map(int, input().split())

    board = [[0]*m for _ in range(n)]

    for _ in range(k):
        i, j = map(int, input().split())
        board[i][j] = 1

    visit = [[0]*m for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visit[i][j] == 0:
                BFS(i, j)
                cnt += 1
    ans.append(cnt)

for a in ans :
    print(a)
