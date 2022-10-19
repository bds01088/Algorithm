'''
시작점은 n-1, 0
도착점은 0, m-1 

'''

import sys

input = sys.stdin.readline

def DFS(srow, scol, visit):
    global n, m, k, board, ans

    #목적지 도착하면 리턴
    if srow == 0 and scol == m-1 and visit[srow][scol] == k :
        ans += 1
        return
    
    #길이가 초과하면 리턴
    if visit[srow][scol] >= k :
        return
    

    for i in range(4):
        nrow = srow+dr[i]
        ncol = scol+dc[i]
        if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] == 0 and board[nrow][ncol] != 'T' :
            visit[nrow][ncol] = visit[srow][scol]+1
            DFS(nrow, ncol, visit)
            visit[nrow][ncol] = 0



n, m, k = map(int, input().strip().split())

dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

board = []

ans = 0

visit = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board.append(tuple(input().strip()))

visit[n-1][0] = 1
DFS(n-1, 0, visit)

print(ans)