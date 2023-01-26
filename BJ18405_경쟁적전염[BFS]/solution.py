import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

def FloodFill(srow, scol):
    global visit, board, N, VirusNum
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    changeList = []

    visit[srow][scol] = True
    
    q = deque()
    q.append([srow, scol])

    while q:
        row, col = q.popleft()
        #근처 바이러스중 가장 작은 바이러스로 감염시키자
        minVirus = VirusNum+1

        for i in range(4):
            nrow, ncol = row+dr[i], col+dc[i]
            
            if 0 <= nrow < N and 0 <= ncol < N :
                if board[nrow][ncol] == 0 and visit[nrow][ncol] == False:
                    q.append([nrow, ncol])
                    visit[nrow][ncol] = True
                if board[nrow][ncol] != 0 :
                    minVirus = min(board[nrow][ncol], minVirus)
        
        #해당 좌표에서 근처에 바이러스가 있다면 감염되어야함
        #하지만 바로 바꾸면 이번턴에 감염되지 않아야할 장소가 이번 장소에서 감염된 정보를 토대로
        #바로 바뀔 수 있기 때문에 변화 정보를 따로 저장해서 리턴한다.
        if minVirus != VirusNum+1 :
            changeList.append([row, col, minVirus])
    return changeList


N, VirusNum = map(int, input().split())

board = []


for i in range(N):
    board.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())


for t in range(S):
    #시간초과 뜰수도 있을듯
    #시간초과뜸..
    #차라리 빈공간을 탐색해서 근처에 있는 가장 작은 번호의 바이러스로 감염시키자
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visit[i][j] == False:
                for xx, yy, vv in FloodFill(i, j):
                    board[xx][yy] = vv


print(board[X-1][Y-1])
