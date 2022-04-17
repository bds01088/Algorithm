'''
w h가 주어지고
1은 땅 0은 바다다

입력의 마지막 줄에는 0이 두개 주어진다

섬의 개수를 출력하라
완전탐색하면서 1일때 BFS돌아서 섬 침몰시키기
'''


import sys
sys.stdin = open('백준4963_섬의개수/input.txt')
from collections import deque

def BFS(srow, scol):
    global visit
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = 1

    while q :
        r, c = q.popleft()
        for i in range(8):
            nrow = r+dr[i]
            ncol = c+dc[i]
            if 0 <= nrow < row and 0 <= ncol < col and visit[nrow][ncol] == 0 and board[nrow][ncol] == 1 :
                q.append([nrow,ncol])
                visit[nrow][ncol] = 1

    return


dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,-1,1]

ans = []
while True :
    col, row = map(int, input().split())
    if row == 0 and col == 0 :
        break
    board = []
    for i in range(row):
        board.append(list(map(int, input().split())))
    visit = [[0]*col for _ in range(row)]

    cnt = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1 and visit[i][j] == 0 :
                cnt += 1
                BFS(i, j)
    ans.append(cnt)

for a in ans :
    print(a)