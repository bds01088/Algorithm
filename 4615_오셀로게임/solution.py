'''
4*4, 6*6, 8*8 중 하나를 주고
정가운데
W B
B W 에 주어지고 시작한다
흑, 백 순서로 시작하며
놓인 위치와 원래 있던 돌의 사이에 존재하는 상대방의 돌을 모두 색깔을 바꾼다
사이는 대각선도 포함이다
1이 흑돌이고 2가 백돌이다

BFS를 쓰면 될듯?
주어지는 놓는 좌표를 기준으로
8방향을 모두 탐색하고
놓는 위치에는 반드시 근처에 상대방의 돌이 존재해야한다
못놓는다면 주어진 좌표는 스킵하면 될듯
'''
import sys
sys.stdin = open('input.txt')

def findally(r, c, color, way):
    global dr, dc
    ally = []
    nr = r + dr[way]
    nc = c + dc[way]
    while 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 0 :
        nr = nr+dr[way]
        nc = nc+dc[way]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == color :
            ally = [nr,nc]
            #검흰검흰 검놓으면 검검검검검이아니라 검흰검검검이 됨
            break
    return ally

def cando(r, c, color):
    global dr, dc
    waytoenemy = []
    if board[r][c] == 0 :
        for i in range(8):
            if 0 <= r+dr[i] < n and 0 <= c+dc[i] < n and\
                board[r+dr[i]][c+dc[i]] != 0 and board[r+dr[i]][c+dc[i]] != color:
                isally = findally(r, c, color, i)
                if isally :
                    #팀의 좌표와 방향을 추가
                    waytoenemy.append([isally,i])
    return waytoenemy

tc = int(input())

#     상,하,좌,우,좌상,좌하,우상,우하
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

for t in range(tc):
    n, m = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    #4*4 -> 1,1 1,2 2,1 2,2
    #6*6 -> 2,2 2,3 3,2 3,3
    #8*8 -> 3,3 3,4 4,3 4,4
    #기초값 설정
    board[n//2-1][n//2-1] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    board[n//2][n//2] = 2
    for time in range(m):
        row, col, color = map(int, input().split())
        row = row-1
        col = col-1
        changecolor = cando(row, col, color)
        if not changecolor :
            continue
        else :
            for team, way in changecolor :
                trow, tcol = row, col
                while trow != team[0] or tcol != team[1] :
                    board[trow][tcol] = color
                    trow = trow+dr[way]
                    tcol = tcol+dc[way]

    Wcnt = 0
    Bcnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 :
                Bcnt += 1
            elif board[i][j] == 2 :
                Wcnt += 1
    print(f'#{t+1} {Bcnt} {Wcnt}')