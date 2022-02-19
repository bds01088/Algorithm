'''
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)
3. 보드판 n*n만큼 들어옴
k길이에 딱떨어지는 빈칸을 찾아야한다
빈칸은 1로 표기됌

가로로 쭉 훑고
세로로 쭉 훑고
한 줄에 1갯수가 k면 될듯
cnt +=1 해주고\
'''

import sys
sys.stdin = open("input.txt")

def canwordIn(n, k, board):
    result = 0
    for i in range(n):
        rcnt = 0
        ccnt = 0
        for j in range(n):
            if board[i][j] == 1 :
                rcnt += 1
                if rcnt == k :
                    if j+1 < n and board[i][j+1] == 0:
                        result += 1
                    elif j+1 == n:
                        result += 1
            else :
                rcnt = 0

            if board[j][i] == 1 :
                ccnt += 1
                if ccnt == k :
                    if j+1 < n and board[j+1][i] == 0:
                        result += 1
                    elif j+1 == n :
                        result += 1
            else :
                ccnt = 0
    return result
tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    r = canwordIn(n, k, board)
    print(f'#{t+1} {r}')