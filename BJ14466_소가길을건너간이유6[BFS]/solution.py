import sys
from collections import defaultdict, deque

input = lambda : sys.stdin.readline().strip()

def BFS(srow, scol):
    q = deque()
    q.append([srow, scol])

    while q: 
        row, col = q.popleft()
        road = roads[(row, col)]
        
        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]

            if 0 <= nrow < N and 0 <= ncol < N and visit[nrow][ncol] == False and (nrow, ncol) not in road :
                if board[nrow][ncol] == 1 :
                    cowsPerArea[areaNum] += 1
                visit[nrow][ncol] = True
                q.append([nrow, ncol])

    



N, K, R = map(int, input().split())

roads = defaultdict(list)
board = [[0 for _ in range(N)] for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    roads[(r1-1, c1-1)].append((r2-1, c2-1))
    roads[(r2-1, c2-1)].append((r1-1, c1-1))


for i in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

cowsPerArea = [0 for _ in range(N**2)]

areaNum = 1
for i in range(N):
    for j in range(N):
        if visit[i][j] == False and board[i][j] == 1:
            cowsPerArea[areaNum] += 1
            visit[i][j] = True
            BFS(i, j)
            areaNum += 1

s = 0
for i in range(1, areaNum):
    for j in range(i+1, areaNum):
        s += cowsPerArea[i]*cowsPerArea[j]

print(s)
