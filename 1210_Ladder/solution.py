'''
0과 1로 이루어진 100x100인 판때기에서
2로 표기된 도착점에 도달할 수 있는 출발점의 좌표x값을 구하라
한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
-> 횡이동으로 쭉가다가 0나오면 방향전환 하면될듯

10개의 테스트케이스가 주어진다

해결방법
가장 밑쪽에 2로 표기된 도착점에서 역으로 출발하여 찾아가면 모든 출발점을 찾아볼 필요가 없을듯
'''

import sys
sys.stdin = open("input.txt")

def find_start(board, t) :
    #도착점 찾기
    col = 0
    row = 99
    for i in range(len(board[row])) :
        if board[row][i] == 2:
            col = i
            break
    #print(col)
    #방향 설정
    #상 우 좌만 필요함
    d = 0 #상=0 우=1 좌=2
    dr = [-1, 0, 0]
    dc = [0, 1, -1]

    while row != 0 :
        row += dr[d]
        col += dc[d]
        if d == 0 :
            #좌우에 다리가 있는지 확인
            lside = col-1
            rside = col+1
            ######################################
            #중요!
            #인덱스 값을 이용하는 조건은 먼저 넣지말고 뒤쪽으로 미뤄둔다
            #앞쪽에 넣으면 인덱스 에러를 발생시킨다
            ######################################
            if lside >= 0 and board[row][lside] != 0:
                d = 2
            elif rside <= 99 and board[row][rside] != 0 :
                d = 1

        if d == 1 :
            #####################################
            #중요!
            #두 조건을 붙이게 되면 col+1일때 조건을 만족하니까 뒤 조건까지도 확인하게된다
            #그렇게 되면 인덱스에러가 뜬다
            #####################################
            if col+1 > 99 :
                d = 0
            elif board[row][col+1] == 0:
                d = 0
        if d == 2 :
            if col-1 < 0 :
                d = 0
            elif board[row][col-1] == 0:
                d = 0
    return col


for _ in range(10) :
    t = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    result = find_start(board, t)
    print(f'#{t} {result}')
