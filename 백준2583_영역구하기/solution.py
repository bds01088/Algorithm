'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
왼쪽아래 x,y
오른쪽위 x,y
나뉘어진 백지(0)의 개수 구하기
'''
from collections import deque
def BFS(srow, scol):
    global visit
    count = 0
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = 1

    while q :
        r, c = q.popleft()
        count += 1
        for i in range(4):
            nrow = r+dr[i]
            ncol = c+dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] == 0 and board[nrow][ncol] == 0 :
                q.append([nrow,ncol])
                visit[nrow][ncol] = 1

    return count




n, m, k = map(int, input().split())

board = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x2 = x2-1
    y2 = y2-1
    # n-1-y1, x1 ; n-1-y2, x2
    for i in range(n-1-y2, n-y1):
        for j in range(x1, x2+1) :
            board[i][j] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

cnt = 0
w = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visit[i][j] == 0:
            cnt += 1
            w.append(BFS(i,j))
print(cnt)
print(*sorted(w))