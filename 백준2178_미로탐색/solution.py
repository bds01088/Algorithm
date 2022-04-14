'''
1 이동가능
0 이동 불가
1,1에서 n,m까지 이동할때 최소칸수 구하기
BFS
'''

import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(srow, scol):
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = 1

    while q:
        row, col = q.popleft()
        if row == n-1 and col == m-1 :
            return visit[row][col]
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] == 0 and board[nrow][ncol] == 1:
                q.append([nrow, ncol])
                visit[nrow][ncol] = visit[row][col] + 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []
visit = []
for i in range(n):
    board.append(list(map(int,input())))
    visit.append([0 for _ in range(m)])


result = BFS(0,0)

print(result)