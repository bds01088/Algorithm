import sys
from collections import deque, defaultdict

input = lambda : sys.stdin.readline().strip()

def throwStick(H, S, D):
    global board, M, dr, dc
    for _ in range(M):
        if board[H][S] == 'x' :
            board[H][S] = '.'
            candi = deque()
            for i in range(4):
                nrow = H+dr[i]
                ncol = S+dc[i]
                if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] == 'x' :
                    candi.append([nrow, ncol])
            return candi
        else :
            S += D
    return None

def BFS(srow, scol):
    global visit
    clusterList = defaultdict(list)
    clusterList[scol].append(srow)
    q = deque()
    q.append([srow,scol])
    visit[srow][scol] = True
    touched = False
    while q :
        row, col = q.popleft()
        if row == N-1 :
            touched = True
        
        for i in range(4):
            nrow, ncol = row+dr[i], col+dc[i]
            if 0 <= nrow < N and 0 <= ncol < M and visit[nrow][ncol] != True and board[nrow][ncol] == 'x':
                q.append([nrow, ncol])
                clusterList[ncol].append(nrow)
                visit[nrow][ncol] = True
    
    return (not touched, clusterList)
        
# 최소 차이를 구해야하는데 이게 잘 안됌
def findDiff(cluster) :
    mmin = 99999
    for key in list(cluster.keys()): 
        for val in cluster[key] :
            height = 0
            for qq in range(val+1, N):
                #한칸 떨어졌을때 그곳이 x이면 val+1부터 시작해서 1만큼 떨어지는 것이므로 height는 1임
                if qq not in cluster[key] and board[qq][key] == 'x' :
                    break
                height += 1
                if height > mmin :
                    break
            if height < mmin :
                mmin = height
    return mmin


N, M = map(int, input().split())

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
board = []

for i in range(N):
    board.append(list(input()))

T = int(input())
stick = list(map(int, input().split()))

for i in range(T):
    stick[i] = N-stick[i]

for i in range(T):
    # print(i)
    # for j in range(N):
    #     print(board[j])
    D = 0
    S = 0
    #0, 2, 4 ..
    #왼쪽에서 오른쪽으로 던짐
    if i%2 == 0 :
        D = 1
    #오른쪽에서 왼쪽으로 던짐
    else :
        D = -1
        S = M-1
    candi = throwStick(stick[i], S, D)
    visit = [[False for _ in range(M)] for _ in range(N)]
    makeFalling = False
    cluster = defaultdict()

    if i == 3 :
        xxx= 1

    while candi :
        r, c = candi.popleft()
        if not visit[r][c]:
            makeFalling, cluster = BFS(r, c)
            if makeFalling :
                break

    if makeFalling :
        diff = findDiff(cluster)
        for key in list(cluster.keys()) :
            cluster[key].sort(reverse=True)
            for hp in cluster[key] :
                row = hp
                board[row][key] = '.'
                row = row+diff
                board[row][key] = 'x'


for i in range(N):
    for j in range(M):
        print(board[i][j], end='')
    print()