'''
왼쪽에서 오른쪽으로 연결할 수 있는 파이프 최대 구하기
이동은 오른쪽위, 오른쪽, 오른쪽아래로만 이동 가능
stack을 쓰니까 오른쪽에서 뽑아오니까
위부터 탐색해야하는 상황에서는 맨위 탐색이 맨 뒤에오도록 direction의 맨마지막을 위로 가는걸로 한다

0,0 부터 0,n-1까지 차례대로 내려가면서 진행하고
x는 건물이니까 못감
최대한 위로 이동하는 걸로 하고
DFS를 쓰자

'''

import sys
sys.stdin = open('백준3109_빵집/input.txt')
from collections import deque

def DFS(srow, scol):
    global visit
    stack = deque()
    stack.append([srow, scol])
    
    
    while stack:
        row, col = stack.pop()
        visit[row][col] = 1
        if col == m-1 :
            return 1
        for i in range(3):
            nrow = row+dr[i]
            ncol = col+dc[i]
            if 0 <= nrow < n and 0 <= ncol < m and visit[nrow][ncol] == 0 and board[nrow][ncol] != 'x':
                stack.append([nrow,ncol])                
    return 0



#stack을 쓰니까 오른쪽에서 뽑아오니까
#위부터 탐색해야하는 상황에서는 맨위 탐색이 맨 뒤에 오도록 
#direction의 맨마지막을 위로 가는걸로 한다
#오른쪽 아래, 오른쪽, 오른쪽 위
dr = [1, 0, -1]
dc = [1, 1, 1]

n, m = map(int, input().split())

visit=[[0]*m for _ in range(n)]
board=[]
for i in range(n):
    board.append(list(input()))

ans = 0
for i in range(n):
    ans += DFS(i, 0)

print(ans)
