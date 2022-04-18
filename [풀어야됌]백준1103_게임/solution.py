'''
배열 n, m을 받고
띄워쓰기 없는 값들을 받는다
H는 구멍을 뜻해서 문자로 다 받아야할 듯하다
무한히 움직이면 -1을 출력하는데
무한히 움직이는것은 visit가 1인 곳을 방문할 수 있을 경우인 것 같다
0,0에서 출발한다
board값만큼 이동하고 중간의 구멍은 무시한다

'''

import sys
sys.stdin = open('input.txt')
from collections import deque

def DFS(srow, scol):
    global visit
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = 1
    hole = []

    while q:
        row, col = q.pop()
        for i in range(4):
            nrow = row+dr[i]*int(board[row][col])
            ncol = col+dc[i]*int(board[row][col])
            if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] != 'H':
                if visit[nrow][ncol] != 0 :
                    return -1
                else :
                    q.append([nrow,ncol])
                    visit[nrow][ncol] = visit[row][col]+1
            elif 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'H':
                hole.append([visit[row][col]])
    if hole :
        return max(hole, visit[row][col])
    else :
        return visit[row][col]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))

visit = [[0]*m for _ in range(n)]

result = DFS(0,0)
print(result)