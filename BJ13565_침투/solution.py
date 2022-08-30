import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    q = deque()
    q.append([0,start])

    while q :
        row, col = q.popleft()
        visit[row][col] = 1
        if row == m-1 :
            return True
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and \
                board[nrow][ncol] == 0 and visit[nrow][ncol] == 0 :
                q.append([nrow,ncol])


def DFS(row, col) :
    visit[row][col] = 1
    if row == m-1 :
        return True
    for i in range(4) :
        nrow = row + dr[i]
        ncol = col + dc[i]
        if 0 <= nrow < n and 0 <= ncol < m and \
            board[nrow][ncol] == 0 and visit[nrow][ncol] == 0 :
            if DFS(nrow, ncol):
                return True
    return False


                
n, m = map(int, input().strip().split())

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visit = [[0] * m for _ in range(n)]
board = [list(map(int, input().strip())) for _ in range(n)]
# for i in range(n):
#     board.append(list(map(int, input().strip())))
#     visit.append([0 for _ in range(m)])

result = 0
for i in range(m):
    if board[0][i] == 0 and visit[0][i] == 0 :
        if DFS(0, i):
            result = 1
            break

if result == 1 :
    print("YES")
else :
    print("NO")