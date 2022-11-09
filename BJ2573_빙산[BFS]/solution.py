import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()


def BFS(srow, scol):
    global board, visit
    q = deque()
    q.append((srow, scol))
    visit[srow][scol] = 1

    melting = [] 

    while q:
        row, col = q.popleft()
        sea = 0

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            #어차피 테두리는 0으로 가득 차있고 시작을 거기서 안하기 때문에
            # if 0 <= nrow < N and 0 <= ncol < M :
            if board[nrow][ncol] == 0 :
                sea += 1
            if board[nrow][ncol] != 0 and visit[nrow][ncol] == 0 :
                q.append((nrow, ncol))
                visit[nrow][ncol] = 1
        if sea != 0 :
            melting.append([row, col, sea])

    #BFS다돌때까지 안빼주어야 제대로 계산됌
    for melt in melting :
        board[melt[0]][melt[1]] = max(0, board[melt[0]][melt[1]]-melt[2])
    

                


N, M = map(int, input().split())

board = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    board.append(list(map(int, input().split())))


year = 0
while True :
    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j] != 0 and visit[i][j] == 0:
                BFS(i, j)
                cnt += 1
    if cnt >= 2 :
        break
    if cnt == 0 :
        year = 0
        break
    year += 1

print(year)


