'''
인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
주어진 정보에서 같은 색인 영역은 겹치지 않는다.

입력
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)

해결방법
0으로 가득찬 10x10에다가
0일경우 입력받은 값 넣고
같은색이면 그냥 덮어씌우고
다른색이면 +시켜서 3으로 만든다
마지막에 다시 전체 탐색해서 3개수 세면될듯
'''

import sys
sys.stdin = open("input.txt")

tc = int(input())

for t in range(tc):
    #0으로 가득찬 판때기 생성
    board = [[0]*10 for _ in range(10)]
    #색칠 개수 받기
    pnum = int(input())
    for _ in range(pnum):
        #시작지점 좌표, 끝지점 좌표, 색깔 받기
        srow, scol, erow, ecol, color = map(int, input().split())
        for i in range(10) :
            for j in range(10):
                #판때기 전체순회하면서 색칠하기
                if srow <= i <= erow and scol <= j <= ecol :
                    #0이아니거나 현재 색칠중인 색깔이 아닌 곳에는 더해주기
                    #다른색깔이 칠해져있기 때문
                    if board[i][j] != 0 or board[i][j] != color :
                        #보라색은 3으로한다
                        board[i][j] += color
                    else :
                        #같거나 0일경우에는 그냥 색 덮어씌우면됌
                        board[i][j] = color

        cnt = 0
        #전체 순회하면서 보라색인경우 찾기
        for i in range(10):
            for j in range(10):
                if board[i][j] == 3:
                    cnt += 1
    print(f'#{t+1} {cnt}')
