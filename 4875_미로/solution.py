'''
n*n배열의 미로에서
출발점 2로부터 도착점3까지 이어지는 길이 있다면 1
없다면 0을 출력하라
미로에서 1은 벽을 의미한다

해결방법
시작점을 찾고
시작점으로 부터 0으로 된 곳을 타고 가되
지나간 지점은 1로 바꿔준다
4방향이 모두 이동불가능하다면
초기 시작점으로 돌아가고
0이 있는 방향을 다시 탐색한다
초기시작점에서도 4방향 모두 이동 불가능하다면
0을 출력한다
'''

import sys
sys.stdin = open("input.txt")

def findStart(board):
    for i in range(n) :
      for j in range(n):
        if board[i][j] == 2 :
            return i,j

def canGo(rnow, cnow, board) :
    #상 하 좌 우
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    for i in range(4):
        row = rnow + dr
        col = cnow + dc 
        if 0 <= row < n and 0 <= col < n and board[row][col] == 0 :
            return dr, dc

tc = int(input())

for t in range(tc):
    n = int(input())
    board = [list(map(int,input())) for _ in range(n)]
    
    s_row, s_col = findStart(board)
    dr, dc = canGo(s_row, s_col, board)
    
