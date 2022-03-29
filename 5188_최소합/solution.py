'''
n*n이 주어지고
오른쪽이나 아래로만 이동할 수 있다
지나가는 칸의 숫자합이 최소가 되도록 움직일때
합이 얼마인지 출력하라
'''

import sys
sys.stdin = open('input.txt')

def DFS(row, col, case):
    global mmin
    #가지치기
    if mmin < sum(case):
        return

    if len(case) == 2*n-1:
        if mmin > sum(case) :
            mmin = sum(case)
        return

    else :
        for i in range(2):
            nr = row+dr[i]
            nc = col+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                case.append(board[nr][nc])
                DFS(nr, nc, case)
                case.pop()


#하, 우
dr = [1, 0]
dc = [0, 1]

tc = int(input())

for t in range(tc):
    n = int(input())
    board = []

    for i in range(n):
        board.append(list(map(int,input().split())))

    mmin = 13*13*10
    case = [board[0][0]]

    DFS(0, 0, case)

    print(f'#{t+1}', end=' ')
    print(mmin)