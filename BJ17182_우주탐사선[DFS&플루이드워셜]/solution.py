import sys

input = lambda : sys.stdin.readline().strip()


def FloydWarshall(start):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                board[i][j] = min(board[i][j], board[i][k]+board[k][j])

    visit[start] = True
    DFS(start, 0)

def DFS(start, cost):
    global ans
    
    if cost >= ans :
        return

    if len(set(visit)) == 1:
        ans = cost
        return
    
    for i in range(N):
        if visit[i] == False:
            visit[i] = True
            DFS(i, cost+board[start][i])
            visit[i] = False

N, S = map(int, input().split())

board = []
visit = [False for _ in range(N)]
ans = 9999999

for _ in range(N):
    board.append(list(map(int, input().split())))

FloydWarshall(S)

print(ans)
