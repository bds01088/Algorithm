'''
n*m행렬이 있다
벽은 1
이동가능은 0
1칸까지는 벽을 부수고 이동 가능

'''
from collections import deque

def BFS(srow, scol, n, m):
    q = deque()
    visit = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append([0,0])
        visit.append(temp)
    visit[srow][scol][0] = 1
    chance = 0
    q.append([srow, scol, chance])

    while q :
        row, col, chance = q.pop(0)
        if row == n - 1 and col == m - 1:
            return

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            #벽을 부수고 이 좌표에 왔는가
            if 0 <= nrow < n and 0 <= ncol < m :
                if board[nrow][ncol] == 0:
                    q.append([nrow, ncol, chance])
                    visit[nrow][ncol] = visit[row][col] + 1
            #벽을 안부수고 이 좌표에 왔는가
                if board[nrow][ncol] == 1 and chance < 1:
                    q.append([nrow, ncol, chance + 1])
                    visit[nrow][ncol] = visit[row][col] + 1


    #갈 수 있는 길이 없을때
    return -1

#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input())))

print(BFS(0, 0, n, m))
