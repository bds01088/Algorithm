'''
10개의 테스트케이스
번호가 주어지고
16*16 미로가 들어옴
출발점은 2 도착점은 3이다
가능한 길이 있는지 파악되면 1 없으면 0을 출력하라
'''

import sys
sys.stdin = open('input.txt')

def find_start():
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                return i, j

def BFS(si, sj):
    q = []
    q.append([si,sj])
    visit = [[0]*16 for _ in range(16)]
    visit[si][sj] = 1

    while q :
        ci, cj = q.pop(0)
        for d in range(4):
            ni = ci + direction[d][0]
            nj = cj + direction[d][1]
            if 0 <= ni < 16 and 0 <= nj < 16 and visit[ni][nj] == 0 and board[ni][nj] != 1 :
                q.append([ni,nj])
                visit[ni][nj] = 1
                if board[ni][nj] == 3:
                    return 1
    return 0

direction = [[-1,0], [1,0], [0,-1], [0,1]]

for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    si, sj = find_start()

    result = BFS(si, sj)

    print(f'#{t} {result}')