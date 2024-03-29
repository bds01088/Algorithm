'''
n*m행렬이 있다
벽은 1
이동가능은 0
1칸까지는 벽을 부수고 이동 가능

'''
from collections import deque

def bfs(srow, scol) :
    global ans
    q = deque()
    q.append([srow,scol, 1, False])
    visit[srow][scol][0] = 1

    while q :
        row, col, distance, chance = q.popleft()
        #도착했을때 길이가 더 짧을 경우 정답 갱신
        if row == n-1 and col == m-1:
            if ans > distance :
                ans = distance
            continue

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            ndistance = distance + 1
            nchance = chance

            if 0 <= nrow < n and 0 <= ncol < m :
                #벽이고 뚫을수있을때
                if board[nrow][ncol] == 1 and nchance is False :
                    nchance = True
                    visit[nrow][ncol][1] = ndistance
                    q.append([nrow, ncol, ndistance, nchance])
                #벽 안뚫은 상태일때
                #벽 안뚫고 갔던 적이 없거나, 있어도 보다 적은 길이로 도착했을 경우
                elif nchance is False and (visit[nrow][ncol][0] > ndistance or visit[nrow][ncol][0] == 0) \
                        and board[nrow][ncol] != 1 :
                    visit[nrow][ncol][0] = ndistance
                    q.append([nrow, ncol, ndistance, nchance])
                #벽 뚫은 상태일때
                #벽 안뚫은 상태로 진행한 적보다 더 멀리 돌아왔을 경우 실행x
                #벽 뚫은 상태로 이전에 안 지나갔거나, 보다 적은 길이로 도착했을 경우
                elif nchance is True and (visit[nrow][ncol][1] > ndistance or visit[nrow][ncol][1] == 0) \
                    and (ndistance < visit[nrow][ncol][0] or visit[nrow][ncol][0] == 0) and board[nrow][ncol] != 1 :
                    visit[nrow][ncol][1] = ndistance
                    q.append([nrow,ncol,ndistance, nchance])

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int, input().split())
board = []
visit = []
ans = 99999999
for i in range(n):
    board.append(list(map(int, input())))
    visit.append([[0,0] for _ in range(m)])

bfs(0, 0)
if ans == 99999999 :
    print(-1)
else :
    print(ans)
