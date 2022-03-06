'''
n, m이 주어진 다음
n*n배열이 주어지고
m개의 좌표값 x1, y1, x2, y2가 주어진다
좌상단 x1,y1좌표에서 우하단 x2,y2까지의 사각형의 합을 구하라

미완성, DP 이용하기로 하자
'''
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for num in range(m):
    s = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            s += board[i][j]
    print(s)
'''

#DP 구간합으로 구하기
#새로운 2차원 배열을 통해
#1,1부터 x,y까지의 사각형 합을 새로운 2차원배열x,y 좌표에 입력해준다
#(x1, y1)에서 (x2, y2)까지의 합 = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
#시작지점좌표 왼쪽대각선까지의 합은 2번 빠지기 때문에 1번추가해주는 것


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#첫행과 첫열은 0으로 해주어야 더해주기 편하다
sum_board = [[0]*(n+1) for _ in range(n+1)]
s = 0
for i in range(1, n+1):
    #지금 위치의 이전 행의 값 + 해당 위치의 값 + 지금 행의 이전 열들의 합
    #그 행의 이전 열 값들의 합 설정
    row_s = 0
    for j in range(1, n+1):
        #열 방향으로 누적합을 구해주기
        #board에서는 i와j는 -1씩해주어야함
        #해당 위치 값을 행의 합에 더해줌
        #즉 행의 이전값들의 합 + 지금 위치의 값을 저장
        row_s += board[i-1][j-1]
        #지금 열의 이전 행의 값을 더해줌
        sum_board[i][j] = row_s + sum_board[i-1][j]

for num in range(m):
    s = 0
    x1, y1, x2, y2 = map(int, input().split())
    #시작점 sum_board[x1][y1]
    #끝점 sum_board[x2][y2]
    #sum_board의 끝점은 그 지점까지의 모든 합을 가지고있고
    #시작점을 기준으로 왼쪽과 위쪽을 빼주어야하므로
    #x1-1,y2범위와 x2, y1-1범위를 빼주고 중복으로 빼진 x1-1,y1-1 범위를 더해준다
    result = sum_board[x2][y2]-sum_board[x1-1][y2]-sum_board[x2][y1-1]+sum_board[x1-1][y1-1]
    print(result)