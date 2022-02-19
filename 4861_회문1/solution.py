'''
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

해결방법
for문을 돌면서 board에서 temp리스트에 m만큼의 길이를 저장하고
슬라이싱 정방향과 역방향을 비교해서 같으면 출력하는 걸로
안되네..
빈리스트를 인덱스값주고 불러오려하면 인덱스에러 뜬다
'''
import sys
sys.stdin = open("input.txt")

def searchP(n, m, board):
    # 가로 탐색 세로 탐색 따로 해야할듯
    another_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            another_board[j][i] = board[i][j]

    for i in range(n) :
        for j in range(n):
            temp = []
            another_temp = []
            if j+m <= n :
                for p in range(m):
                    temp.append(board[i][j+p])
                    another_temp.append(another_board[i][j+p])
                if temp == temp[::-1] :
                    return temp
                elif another_temp == another_temp[::-1] :
                    return another_temp
            else :
                break

tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        temp = []
        s = input()
        for x in s:
            temp.append(x)
        board.append(temp)
    result = searchP(n, m, board)
    p = ''
    for c in result :
        p += c
    print(f'#{t+1} {p}')

