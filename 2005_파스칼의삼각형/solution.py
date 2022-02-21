'''
크기가 n인 파스칼의 삼각형 만들기
첫번째줄은 항상 1이다.
두번째줄부터 각 숫자들은 자신의 왼쪽위와 위의 합으로 구성된다.
n = 4
1
1 1
1 2 1
1 3 3 1

해결방법
n*n배열을 0으로 가득채우고
0,0은 1로 시작시킨다.
이중for문으로 j는 i+1까지 range 범위를 준다
델타를 사용해서 j기준으로 좌상과 상의 값을 더해서 값으로 입력한다
'''

import sys
sys.stdin = open("input.txt")

def pascal(n, board):
    for i in range(1, n):
        for j in range(n):
            if j == 0 :
                board[i][j] = board[i-1][j]
            else :
                board[i][j] = board[i-1][j] + board[i-1][j-1]
    return board

tc = int(input())
for t in range(tc):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    board[0][0] = 1
    result = pascal(n, board)
    print(f'#{t+1}')
    for i in range(n):
        for j in range(n):
            if result[i][j] != 0 :
                print(result[i][j], end=' ')
        print()
