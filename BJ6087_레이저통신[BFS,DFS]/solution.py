from collections import deque

#DFS로 푸는게 더 알맞는 문제같긴 함
def BFS(start, end):
    global visit, board, ans
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    q = deque()
    srow = start[0]
    scol = start[1]
    visit[srow][scol] = 0
    for i in range(4):
        nrow, ncol = srow+dr[i], scol+dc[i]
        if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] != '*' :
            q.append([nrow, ncol, 0, i])
            visit[nrow][ncol] = 0
        
    while q :
        row, col, countT, direction = q.popleft()

        if countT > ans :
            continue

        if row == end[0] and col == end[1] :
            if ans > countT :
                ans = countT

        for i in range(4):
            nrow, ncol = row+dr[i], col+dc[i]
            newcountT = countT
            if i != direction :
                newcountT += 1
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] != '*' :
                if visit[nrow][ncol] != -1 :
                    #같은 꺽은횟수로 도착해도, 도착할때의 방향이 다를 수 있기 때문에
                    #같은 꺽은횟수도 포함해야한다.
                    if visit[nrow][ncol] >= newcountT:
                        q.append([nrow, ncol, newcountT, i])
                        visit[nrow][ncol] = newcountT
                else :
                    q.append([nrow, ncol, newcountT, i])
                    visit[nrow][ncol] = newcountT


M, N = map(int, input().split())

board = []
visit = [[-1 for _ in range(M)] for _ in range(N)]
point = []
for i in range(N):
    tmp = list(input())
    board.append(tmp)
    for j in range(M):
        if board[i][j] == 'C' :
            point.append([i, j])
ans = N*M
BFS(point[0], point[1])

print(ans)
