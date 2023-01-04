from pprint import pprint
from copy import deepcopy
from collections import defaultdict
R, C, N = map(int, input().split())

#!!!!!!!!!!!!!!!!!반복이 아니다!!!!!!!!!!!
#초기, 꽉, 초기터짐, 꽉, 이전꽉터짐==다른형태될수있음, 꽉, 다른 형태 초기
board1 = []
for i in range(R):
    board1.append(list(input()))

board2 = [['O' for _ in range(C)] for _ in range(R)]
board3 = deepcopy(board2)


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

ashList1 = defaultdict(set)

for i in range(R):
    for j in range(C):
        if board1[i][j] == 'O' :
            ashList1[i].add(j)
            for t in range(4):
                row, col = i+dr[t], j+dc[t]
                if 0 <= row < R and 0 <= col < C and board1[row][col] == '.' :
                    ashList1[row].add(col)

for r in ashList1.keys() :
    for c in ashList1[r] :
        board2[r][c] = '.'

ashList2 = defaultdict(set)

for i in range(R):
    for j in range(C):
        if board2[i][j] == 'O' :
            ashList2[i].add(j)
            for t in range(4):
                row, col = i+dr[t], j+dc[t]
                if 0 <= row < R and 0 <= col < C and board1[row][col] == '.' :
                    ashList2[row].add(col)
for r in ashList2.keys() :
    for c in ashList2[r] :
        board3[r][c] = '.'

T = N%4
if T == 0 or T == 2 :
    for i in range(R):
        print('O'*C)

elif T == 1 :
    if N != 1 :
        for i in range(R):
            for j in range(C):
                print(board3[i][j], end='')
            print()
    else :
        for i in range(R):
            for j in range(C):
                print(board1[i][j], end='')
            print()
else :
    for i in range(R):
        for j in range(C):
            print(board2[i][j], end='')
        print()



