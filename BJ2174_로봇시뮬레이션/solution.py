import sys

# sys.stdin = open('BJ2174_로봇시뮬레이션/input.txt')

input = sys.stdin.readline

def ANSWER() :
    for i in range(M):
        while orders[i][2] != 0 :
            #명령어 카운트 줄이고
            orders[i][2] -= 1
            if orders[i][1] == 'F' :
                #방향대로 이동하고
                nrow = robots[orders[i][0]][0]+dr[robots[orders[i][0]][2]]
                ncol = robots[orders[i][0]][1]+dc[robots[orders[i][0]][2]]
                #범위 벗어나면
                if not (0 <= nrow < B and 0 <= ncol < A) :
                    print(f'Robot {orders[i][0]+1} crashes into the wall')
                    return
                #이동한 위치가 다른 로봇이 있다면
                if board[nrow][ncol] != 0 :
                    print(f'Robot {orders[i][0]+1} crashes into robot {board[nrow][ncol]}')
                    return
                #없다면 그 위치로 이동
                else :
                    board[robots[orders[i][0]][0]][robots[orders[i][0]][1]] = 0
                    board[nrow][ncol] = orders[i][0]+1
                    robots[orders[i][0]][0] = nrow
                    robots[orders[i][0]][1] = ncol
            elif orders[i][1] == 'L' :
                robots[orders[i][0]][2] = ((robots[orders[i][0]][2]+4)-1)%4
            else :
                robots[orders[i][0]][2] = ((robots[orders[i][0]][2]+4)+1)%4

    print("OK")



# num = int(input().strip())

# for t in range(num):
    # print(f'{t+1} : ', end='')
#col, row
A, B = map(int, input().strip().split())
N, M = map(int, input().strip().split())

board = [[0 for _ in range(A)] for _ in range(B)]

robots = []

orders = []

#상, 우, 하, 좌
#90도씩 돌아가기 때문에 인덱스를 -1 하거나 +1 하면 방향이 변경되도록
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

direction = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}

for i in range(N) :
    c, r, d = input().strip().split()
    robots.append([B-int(r), int(c)-1, direction[d]]) #X, Y 좌표를 row,col로 바꿈
    board[B-int(r)][int(c)-1] = i+1

for i in range(M):
    robot, order, time = input().strip().split()
    orders.append([int(robot)-1, order, int(time)])

ANSWER()