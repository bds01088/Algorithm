from collections import deque

def BFS1(srow, scol):
    q = deque()
    q.append([srow, scol])
    visit[srow][scol][0] = 1

    while q :
        row, col= q.popleft()

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]

            if 0 <= nrow < n and 0 <= ncol < n and visit[nrow][ncol][0] == 0 and board[row][col] == board[nrow][ncol] :
                q.append([nrow, ncol])
                visit[nrow][ncol][0] = 1

def BFS2(srow, scol):
    q = deque()
    q.append([srow, scol])
    visit[srow][scol][0] = 1
    startColor = board[srow][scol]

    while q :
        row, col= q.popleft()

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]

            if 0 <= nrow < n and 0 <= ncol < n and visit[nrow][ncol][1] == 0 :
                if startColor == "B" and board[row][col] == board[nrow][ncol]:
                    q.append([nrow, ncol])
                    visit[nrow][ncol][1] = 1
                elif startColor in ("G", "R") and board[nrow][ncol] in ("G", "R") :
                    q.append([nrow, ncol])
                    visit[nrow][ncol][1] = 1

n = int(input())

board = []
visit = []

for i in range(n):
    board.append(list(input()))
    visit.append(list([0, 0] for _ in range(n)))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
normal = 0
disable = 0
for i in range(n):
    for j in range(n):
        if visit[i][j][0] == 0 :
            normal += 1
            BFS1(i, j)
        if visit[i][j][1] == 0 :
            disable += 1
            BFS2(i, j)
                

print(normal, disable)