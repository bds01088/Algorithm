'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

테스트 케이스 10개가 주어짐
가장 처음에 tc들어옴
ex)
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

#1 49

n-m만큼 2차원 배열을 돌고
해당좌표에서 +m만큼의 범위의 합 구하고
합들을 중에 max 구하기
'''

import sys
sys.stdin = open("input.txt")

def max_kill(n, m, board) :
    max = 0
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            sum = 0
            #i, j좌표 기준으로 m*m 합구하기
            for p in range(m):
                for q in range(m):
                    sum += board[i+p][j+q]
            if sum > max :
                max = sum
    return max


tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = max_kill(n, m, board)
    print(f'#{t+1} {result}')