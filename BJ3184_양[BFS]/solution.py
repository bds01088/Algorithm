import sys
from collections import deque
input = sys.stdin.readline


def BFS(r, c):
    global ansWolf, ansSheep
    q = deque()
    q.append([r,c])

    wolf = 0
    sheep = 0
    if board[r][c] == 'v' :
        wolf += 1
    elif board[r][c] == 'o' :
        sheep += 1


    while q :
        row, col = q.popleft()
        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] != 1 and board[nrow][ncol] != '#' :
                q.append([nrow, ncol])
                visit[nrow][ncol] = 1
                if board[nrow][ncol] == 'v' :
                    wolf += 1
                elif board[nrow][ncol] == 'o' :
                    sheep += 1
    
    if wolf < sheep :
        ansSheep += sheep
    else :
        ansWolf += wolf



n, m = map(int, input().strip().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visit = []
board = []
for i in range(n):
    board.append(list(input().strip()))
    visit.append([0 for _ in range(m)])

ansWolf = 0
ansSheep = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] != 1 and board != '#' :
            BFS(i,j)

print(ansSheep, end=' ')
print(ansWolf)