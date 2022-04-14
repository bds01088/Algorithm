'''
0,0에서 시작
방문했던 알파벳은 다시 방문 불가
최대 이동거리를 구하자

DFS로 하자
'''

import sys
sys.stdin = open('input.txt')

def DFS(srow, scol, l):
    global visit, mmax

    mmax = max(mmax, l)
    for i in range(4):
        nrow = srow+dr[i]
        ncol = scol+dc[i]
        if 0 <= nrow < row and 0 <= ncol < col and visit[board[nrow][ncol]] == 0:
            visit[board[nrow][ncol]] = 1
            DFS(nrow, ncol, l+1)
            visit[board[nrow][ncol]] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

row, col = map(int, input().split())

board = []
for i in range(row):
    board.append(list(map(lambda x :ord(x)-65, input())))

visit = [0 for _ in range(26)]
visit[board[0][0]] = 1

mmax = 0
DFS(0, 0, 1)

print(mmax)