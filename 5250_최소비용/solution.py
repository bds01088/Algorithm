'''
0,0에서 n-1,n-1까지 이동하는데
1칸 이동마다 연료 1씩 들고
높이가 증가하는경우 추가 연료가 발생한다
최소 연료 소비량을 출력하시오

칸을 이동할때마다 해당 칸의 높이를 같이 들고가서
다음 이동시에 높이가 더 높아지면 그 차이만큼 연료에 더해주는걸로

'''
from collections import deque
import sys
sys.stdin = open('input.txt')

def BFS(srow, scol):
    visit = [[99999]*n for _ in range(n)]
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = 0


    while q:
        r, c = q.popleft()
        for i in range(4):
            #다음 좌표에 대한 정보
            nrow = r+dr[i]
            ncol = c+dc[i]
            #범위 내인지 먼저 파악하고
            if 0 <= nrow < n and 0 <= ncol < n:
                # 높이 차이가 있다면
                nfuel = visit[r][c] + 1 + max(0, board[nrow][ncol] - board[r][c])
                if visit[nrow][ncol] > nfuel:
                    q.append([nrow, ncol])
                    visit[nrow][ncol] = nfuel

    return visit[-1][-1]

tc = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

for t in range(tc):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    result = BFS(0,0)
    print(f'#{t+1} {result}')

