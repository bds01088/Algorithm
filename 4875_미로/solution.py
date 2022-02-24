'''
n*n배열의 미로에서
출발점 2로부터 도착점3까지 이어지는 길이 있다면 1
없다면 0을 출력하라
미로에서 1은 벽을 의미한다

해결방법
시작점을 찾고
시작점으로 부터 0으로 된 곳을 타고 가되
도착한 지점은 1로 바꿔준다
4방향이 모두 이동불가능하다면
이전 좌표로 돌아가야함
'''

import sys
sys.stdin = open("input.txt")

def findStart(board):
    for i in range(n) :
      for j in range(n):
        if board[i][j] == 2 :
            return i,j

def DFS(rnow, cnow) :
    global result
    #for문을 돌면서 4방향의 가능성을 파악하는것
    for i in range(4):
        #현재 좌표는 rnow, cnow로 이 위치가 1이건 0이건 3이건 상관이없다
        #왜냐하면 우리가 검사하는것은 다음 이동할 좌표의 값이 1인지 0인지 3인지 파악하는것이기 때문
        row = rnow + dr[i]
        col = cnow + dc[i]
        #상하좌우 탐색시 갈 길이 있다면
        #범위 안벗어나고, 좌표의 값이 0이거나 3이여야하고, 결과가 안찾아졌어야함
        if (0 <= row < n and 0 <= col < n) and (board[row][col] not in [1,2]) and (result == 0):
            #만약 탐색된 좌표의 값이 3이면
            if board[row][col] == 3 :
                #결과를 1로 바꾸고 바로 리턴
                result = 1
                return
            #아닐경우 좌표를 1로 변경해서 DFS가 끝나고 다시 이 지점에 왔을때 갔던 방향은 안가도록
            else :
                board[row][col] = 1
            #해당 다음 좌표에 가능성이 있으므로 그 좌표를 기준으로 다시 새로운 다음 좌표를 찾기
            DFS(row, col)
            #======================================================
            #4방향이 모두 갈 수 없다면 이전좌표로 돌아오고 이전좌표에서 상하좌우 중 안가봤던 곳을 파악하기 위해 for문이 재개됌
            #위로 이동했는데 그 좌표에서 4방향이 모두 막혓다면 return을 통해 이전좌표로 돌아오고
            #위로 이동하자 라는 것은 재귀DFS에서 끝까지 돌고 나왔기 때문에 더이상 위로 가는 선택지는 없어짐
            #그럼 나머지 하 좌 우를 for문이 돌고 있던 중이기 때문에 나머지를 검사함
            # ======================================================
    #4방향을 모두 살펴봐도 가능성이 있는 곳이 한군데도 없으면 그냥 리턴해서 result를 0으로 유지
    return

tc = int(input())
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(tc):
    n = int(input())
    result = 0
    board = [list(map(int,input())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    s_row, s_col = findStart(board)
    visited[s_row][s_col] = True
    DFS(s_row, s_col)
    print(f'#{t+1} {result}')
