import sys
from collections import deque

input = sys.stdin.readline

def BFS(sr, sc):
    global n
    q = deque()
    q.append((sr,sc))

    while q :
        nr, nc = q.popleft()
        
        for i in range(6):
            nrow, ncol = nr+dr[i], nc+dc[i]
            if 0 <= nrow < n and 0 <= ncol < n and board[nrow][ncol] == 0 :
                if nrow == tr and ncol == tc :
                    return board[nr][nc]
                q.append((nrow,ncol))
                board[nrow][ncol] = board[nr][nc]+1
    return -1


n = int(input().strip())

board = [[0 for _ in range(n)] for _ in range(n)]

sr, sc, tr, tc = map(int, input().strip().split())

board[sr][sc] = 1

dr = (-2, -2, 0, 0, 2, 2)
dc = (-1, 1, -2, 2, -1, 1)

print(BFS(sr, sc))
