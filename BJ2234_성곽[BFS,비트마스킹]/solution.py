import sys
from pprint import pprint
from collections import deque, defaultdict


input = lambda : sys.stdin.readline().strip()

def BFS(srow, scol):
    global board, visit, N, M, dic
    cnt = 1
    q = deque()
    q.append((srow, scol, False))
    visit[srow][scol] = True
    areaList = []
    anotherAreaList = []
    
    while q :
        row, col, flag = q.popleft()
        #벽을 안뚫고 도착했다면
        if flag == False :
            areaList.append((row, col))

        for i in range(4):
            nrow = row+dr[i]
            ncol = col+dc[i]
            #다음 좌표가 범위 내 일때
            if 0 < nrow < N*2 and 0 < ncol < M*2 :
                #벽을 뚫지 않은 상태에서 새로 도착했다면
                if visit[nrow][ncol] == False and flag == False:
                    #방자체라면, 개수를 증가
                    if board[nrow][ncol] == "0" :
                        cnt += 1
                    #벽이라면 뚫고
                    elif board[nrow][ncol] == "W":
                        flag = True
                    #뚤려진 벽이면 그냥 넘어간다
                    visit[nrow][ncol] = True
                    q.append((nrow,ncol,flag))
                    flag = False
                #벽 좌표에서 다음 좌표로 이동했을때, 그 좌표의 값이 W나 E가 아닐 경우
                #즉, 다른 지역 or 내가 아직 가지 않은 땅일 수 있으니
                #그냥 저장만 해준다
                elif visit[nrow][ncol] == False and flag == True and board[nrow][ncol].isdigit():
                    anotherAreaList.append((nrow, ncol))

    realAnother = []
    for area in anotherAreaList :
        if area not in areaList :
            realAnother.append(area)

    dic[cnt].append(set(realAnother))

    for r, c in areaList :
        board[r][c] = str(cnt)

    return cnt


M, N = map(int, input().split())



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


#하 우 상 좌
#1  1  1  1
bdr = [1, 0, -1, 0]
bdc = [0, 1, 0, -1]

dic = defaultdict(list)


board = [["W" for _ in range(M*2+1)] for _ in range(N*2+1)]
visit = [[False for _ in range(M*2+1)] for _ in range(N*2+1)]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        t = bin(tmp[j])[2:].rjust(4, '0')
        ti = i*2+1
        tj = j*2+1
        for b in range(len(t)) :
            if int(t[b]) == 1 :
                board[ti+bdr[b]][tj+bdc[b]] = "W"
            else :
                board[ti+bdr[b]][tj+bdc[b]] = "E"
        board[ti][tj] = "0"

room_num = 0
rooms = []
for i in range(1, N*2+1, 2):
    for j in range(1, M*2+1, 2):
        if board[i][j] == "0" and visit[i][j] == False:
            rooms.append(BFS(i, j))
            room_num += 1
# pprint(board)
mmax = 0 
# pprint(dic)
for key in dic.keys():
    for S in dic[key]:
        # print(key, S)
        for val in S :
            if key+int(board[val[0]][val[1]]) > mmax :
                mmax = key+int(board[val[0]][val[1]])


print(room_num)
print(max(rooms))
print(mmax)

