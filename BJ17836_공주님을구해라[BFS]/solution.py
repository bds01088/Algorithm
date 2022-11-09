import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

'''
그람 위치파악해서, 그람위치와 공주위치 사이의 길이를 구하고
주인공 시작지점 1,1에서 그람위치가는 길이 + 그람에서 공주까지 길이 보다
BFS해서 공주를 찾을 수 있는 시간이 길어지면 리턴시키는걸로
공주는 무조건 N,M에 위치
'''
def BFS(srow, scol):
    global ans, N, M, gramToTarget, visit, board, dr, dc
    q = deque()
    q.append((srow, scol))
    visit[srow][scol] = 1

    while q :
        row, col = q.popleft()
        
        #그람위치일때
        if board[row][col] == 2 :
            dist = visit[row][col]-1+gramToTarget
            if dist < ans :
                ans = dist
            #그람을 먹으면 공주로 바로 직행할 수 있고,
            #설사 공주까지 최단길이라 하더라도 그람먹었을때와 같으니 그냥 넘어가자
            continue

        if visit[row][col] > ans :
            continue
        
        #공주에 도착하면
        if row == N-1 and col == M-1 :
            if visit[row][col]-1 < ans :
                ans = visit[row][col]-1
            continue


        for i in range(4):
            nrow, ncol = row+dr[i], col+dc[i]

            if 0 <= nrow < N and 0 <= ncol < M and visit[nrow][ncol] == 0 and board[nrow][ncol] != 1 :
                q.append((nrow, ncol))
                visit[nrow][ncol] = visit[row][col]+1



N, M, T = map(int, input().split())

board = []
visit = []

gram = []
gramToTarget = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    tmp = list(map(int, input().split()))
    if 2 in tmp :
        gram.extend([i, tmp.index(2)])
        gramToTarget = abs(N-1-gram[0])+abs(M-1-gram[1])
        # print(gram)
        # print(gramToTarget)
    board.append(tmp)
    visit.append([0 for _ in range(M)])

ans = 99999999999
BFS(0, 0)

if ans > T :
    print('Fail')
else :
    print(ans)

