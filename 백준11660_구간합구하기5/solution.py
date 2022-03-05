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
sum_board, board = [[0]*n for _ in range(n)]
s = 0
for i in range(n):
    for j in range(n):
        #일단 받고
        board[i][j] = int(input())
        #열 방향으로 누적합을 구해주기
        s += board[i][j]
        sum_board[i][j] = s
        #그러면 열이 증가할때마다 첫값을 어떻게 하지?

for num in range(m):
    s = 0
    x1, y1, x2, y2 = map(int, input().split())