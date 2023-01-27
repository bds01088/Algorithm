import sys
from itertools import combinations

input = lambda : sys.stdin.readline().strip()

def overWatch(row, col):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    for i in range(4):
        r = row+dr[i]
        c = col+dc[i]
        
        catch = False
        while 0 <= r < N and 0 <= c < N :
            if board[r][c] == 'S':
                catch = True
                break
            elif board[r][c] in ('O', 'T') :
                break
            r += dr[i]
            c += dc[i]
        
        if catch :
            return True

    return False


N = int(input())

board = []

for i in range(N):
    board.append(list(input().split()))

teacher = []
nothing = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T' :
            teacher.append([i, j])
        if board[i][j] == 'X' :
            nothing.append([i,j])

candi = list(combinations(nothing, 3))

can = False

for ele in candi :
    cnt = 0
    for x, y in ele :
        board[x][y] = 'O'
    for x, y in teacher :
        if overWatch(x, y):
            break
        else :
            cnt += 1
    if len(teacher) == cnt:
        can = True
        break
    else :
        for x, y in ele:
            board[x][y] = 'X'

if can :
    print("YES")
else :
    print("NO")
    

