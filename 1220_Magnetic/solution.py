'''
총 10개의 테스트 케이스가 주어진다.
1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며
테이블의 윗 부분에 N극이 아랫 부분에 S극이 위치한다고 가정한다.
100*100판에서 교착상태인 것의 갯수를 구하라

해결방법
결국 교착상태가 될 것의 개수를 구하면 됌
N극이 아래 S극이 위쪽이니
열방향 조회를 하되
S극을 가진 자성체면 스킵하고,
N극을 가진 자성체면 flag를 1로 만들고
그다음에 S극 자성체가 나타나면 교착상태 cnt+1을 하면 되겠다
교착상태를 더하면 flag를 0으로 다시 초기화함
'''

import sys
sys.stdin = open("input.txt")

def countMag(board):
    #1=N, 2=S
    cnt = 0
    for i in range(100):
        flag = 0
        for j in range(100):
            #N극을 기준으로함
            if board[j][i] == 1 :
                flag = 1
            #N극이 위쪽에 존재하고 S극이 발견되면
            elif board[j][i] == 2 :
                if flag == 1 :
                    cnt += 1
                    #깃발 초기화
                    flag = 0
    return cnt

for t in range(10):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = countMag(board)
    print(f'#{t+1} {result}')