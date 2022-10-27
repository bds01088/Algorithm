'''
국경선을 공유하는 두 나라의 인구차이가
L이상 R이하면 연합으로 됨
연합되면 연합의 인구수 총합//연합의 넓이

while True로 전체 순환하면서
while문 한바퀴 돌면 ans += 1씩 해주자
날짜를 출력해야함
'''

import sys
input = sys.stdin.readline

from collections import deque

def BFS(srow, scol):
    global isU, N, L, R
    q = deque()
    q.append((srow,scol))
    
    total = board[srow][scol]
    cnt = 1

    U = [(srow, scol)]

    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < N and visit[nrow][ncol] == 0 :
                if L <= abs(board[row][col]-board[nrow][ncol]) <= R:
                    cnt += 1
                    total += board[nrow][ncol]
                    visit[nrow][ncol] = 1
                    q.append((nrow, ncol))
                    U.append((nrow, ncol))
                    isU = 1
    Avg = total//cnt
    for r, c in U :
        board[r][c] = Avg


N, L, R = map(int, input().strip().split())

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

board = []

for i in range(N):
    board.append(list(map(int, input().strip().split())))

ans = 0
while True:
    isU = 0
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 :
                visit[i][j] = 1
                BFS(i, j)
    if isU == 1 :
        ans += 1
    else :
        break

print(ans)
