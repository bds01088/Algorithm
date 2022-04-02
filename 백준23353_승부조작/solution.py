'''
n*n에서 흑돌 백돌을 이용하여 게임함
랑이 = 흑돌
메리 = 백돌
랑이 점수는 가로 세로 대각선 중 하나의 방향으로 연속하여 존재하는
가장 긴 흑돌의 길이가 됨
백돌 하나를 흑돌로 바꿀수 잇다
이때 얻을 수 있는 최대 점수를 구하라

0은 빈위치, 1은 흑돌, 2는 백돌

바꾸지 않은 상태로 가장 긴 점수를 찾고
모든 백돌을 한번씩 흑돌로 바꾸고
그지점에 대해서 가로 세로 대각선 방향으로 뻗어서 길이를 구한뒤
맥스값보다 크면 바꿔주고
아니면 안바꾸고

백돌을 바꾸기 전의
최대 길이를 구해야한다
가로 세로 좌대각선 우대각선 4방향이 있고
가로 세로는 그냥 방향을 한쪽으로 정해주면된다
어차피 0,0에서 시작하기 때문에
가로탐색은 오른쪽으로만 해주면 된다
단 visit의 i,j,0이 0일 경우에 오른쪽으로 탐색을 시작한다
0,0에서 시작한 가로탐색은 1씩 증가하며 흑돌일때까지하고
지나온 곳은 visit의 i,j,0을 1로 바꾸어준다
세로탐색은 아래로만 해주면 된다
단 visit의 i,j,1이 0일 경우에 아래로 탐색을 시작한다
0,0에서 시작한 세로탐색은 1씩 증가하며 흑돌일때까지하고
지나온 곳은 visit의 i,j,1을 1로 바꾸어준다

n <= 1000이므로
n*n 완전탐색해도 될듯
그래도 1백만이라
'''
import sys
sys.stdin = open('input.txt')


def cal_length(i, j):
    global mmax, visit
    row = i
    col = j
    cnt = [0,0,0,0]
    #가로 탐색
    while col < n and board[row][col] == 1 and visit[row][col][0] == 0:
        cnt[0] += 1
        visit[row][col][0] = 1
        col += 1
    col = j
    #세로 탐색
    while row < n and board[row][col] == 1 and visit[row][col][1] == 0:
        cnt[1] += 1
        visit[row][col][1] = 1
        row += 1
    row = i
    #좌하단대각선 탐색
    while row < n and  0 <= col < n and board[row][col] == 1 and visit[row][col][2] == 0:
        cnt[2] += 1
        visit[row][col][2] = 1
        row += 1
        col -= 1
    row, col = i, j
    #우하단대각선 탐색
    while row < n and 0 <= col < n and board[row][col] == 1 and visit[row][col][3] == 0:
        cnt[3] += 1
        visit[row][col][3] = 1
        row += 1
        col += 1
    if max(cnt) > mmax :
        mmax = max(cnt)

n = int(input())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

visit = [[[0,0,0,0] for i in range(n)] for j in range(n)]

mmax = 0
q = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and (0 in visit[i][j]) :
            cal_length(i, j)
        if board[i][j] == 2 :
            q.append([i,j])

for row, col in q :
    cnt = [1,1,1,1]
    #좌로 탐색
    i = row
    j = col-1
    while 0 <= j and board[i][j] == 1:
        j -= 1
        cnt[0] += 1
    #우로 탐색
    i = row
    j = col+1
    while j < n and board[i][j] == 1:
        j += 1
        cnt[0] += 1
    #위로 탐색
    i = row-1
    j = col
    while 0 <= i and board[i][j] == 1:
        i -= 1
        cnt[1] += 1
    #아래로 탐색
    i = row+1
    j = col
    while i < n and board[i][j] == 1:
        i += 1
        cnt[1] += 1
    #좌상 탐색
    i = row-1
    j = col-1
    while 0 <= i and 0 <= j and board[i][j] == 1:
        i -= 1
        j -= 1
        cnt[2] += 1
    #우하 탐색
    i = row+1
    j = col+1
    while i < n and j < n and board[i][j] == 1:
        i += 1
        j += 1
        cnt[2] += 1
    #우상 탐색
    i = row-1
    j = col+1
    while 0 <= i and j < n and board[i][j] == 1:
        i -= 1
        j += 1
        cnt[3] += 1
    #좌하 탐색
    i = row+1
    j = col-1
    while i < n and 0 <= j and board[i][j] == 1:
        i += 1
        j -= 1
        cnt[3] += 1
    if max(cnt) > mmax :
        mmax = max(cnt)


print(mmax)
