'''
1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)
4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.
5. 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.
7. 원자들의 최초 위치는 서로 중복되지 않는다.
8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.
9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.
10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.

가능성이 없는 종류
방향도 고려해야함
위로 이동하는 원자일때 자신보다 y값이 낮은게 없을 경우 가능성x
아래로 이동하는 원자일 때 자신보다 y값이 높은게 없을 경우 가능성x
좌로 이동하는 원자일 때 자신보다 x값이 낮은 게 없을 경우 가능성x
우로 이동하는 원자일 때 자신보다 x값이 높은게 없을 경우 가능성x

0.5초에 충돌하는건 어떻게하지?
좌표를 -1000 이상 1000이하의 정수로 주어지는걸
*2해서 0.5초를 1초로 바꾸어 계산하자
즉 좌표는 -2000~2000이 되는거다

해결방법
모든 원자들의 좌표와 이동방향을 저장하고
0.5초 마다 한칸씩 이동시킨다
이동 후 원자들의 좌표 목록에서
동일한 좌표가 있다면 그 좌표에 있는 모든 원자들을 삭제함과 동시에
들고있는 에너지들을 결과에 더해주자
'''
import sys
sys.stdin = open('input.txt')

def find(startnode):
    global crash, ans, atom, board
    node = startnode
    while crash[node] != 1:
        #시작원자에서 가장 작은 거리를 가진 원자번호 구하기
        idx = board[node].index(min(board[node]))
        #만약 그 원자가 안사라져있고, 거기서 최솟값이 시작원자와 같다면
        #시작원자 A와 가장 작은 거리를 가진 원자 B가 제일 먼저 부딧힘
        if crash[idx] == 0 and min(board[idx]) == min(board[node]) :
            #B와의 강능성이 있는 노드들 중 동시에 부딧히는 원자가 더 있는지 확인하고
            for j in range(n):
                #있다면 답에 에너지 넣어주고 충돌했다고 상태를 변경해줌
                if board[idx][j] == min(board[idx]):
                    #최소한 A원자는 값이 더해짐
                    ans += atom[j][3]
                    crash[j] = 1
            #마지막으로 B의 에너지를 넣어줌
            ans += atom[idx][3]
            crash[idx] = 1
        #시작원자 A의 최소거리와 A의 최소거리에 해당하는 원자 B의 최소거리가 다르다면
        #B는 다른 원자 C와 먼저 부딧혀 소멸할 것이다
        #그러나 C가 먼저 따른원자 D와 부딧혀 소멸하면, B의 최소거리 원자는 달라질 것이다
        #이걸 어떻게 해결하지?
        else :
            x = min(board[idx])
            newstartnode = board[idx].index(x)
            find(newstartnode)
        

tc = int(input())

#상 하 좌 우
#0  1  2  3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for t in range(tc):
    n = int(input())
    ans = 0
    atom = []
    board = [[9999999]*n for _ in range(n)]
    crash = [0 for _ in range(n)]
    for i in range(n) :
        row, col, direction, energy = map(int, input().split())
        atom.append([row*2,col*2, direction, energy])
    
    #가망성 있는 원자와의 거리 구하기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9999999:
                #기준원자의 방향이 위로 갈때
                if atom[i][2] == 0 :
                    #비교원자의 방향이 아래일때
                    if atom[j][2] == 1 and atom[i][0] == atom[j][0] :
                        c = atom[j][1] - atom[i][1]
                        board[i][j] = c
                        board[j][i] = c
                    #오른쪽에서 왼쪽으로 올때
                    elif atom[j][2] == 2 and atom[j][0]-atom[i][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[j][0]-atom[i][0] == atom[j][1]-atom[i][1] :
                        c = (atom[j][0]-atom[i][0]) + (atom[j][1]-atom[i][1])
                        board[i][j] = c
                        board[j][i] = c
                    #왼쪽에서 오른쪽으로 올때
                    elif atom[j][2] == 3 and atom[i][0] - atom[j][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[i][0]-atom[j][0] == atom[j][1]-atom[i][1] :
                        c = (atom[i][0]-atom[j][0]) + (atom[j][1]-atom[i][1])
                        board[i][j] = c
                        board[j][i] = c
                #기준원자의 방향이 왼쪽으로 갈때
                elif atom[i][2] == 2 :
                    #비교원자의 방향이 오른쪽으로 움직일때
                    if atom[j][2] == 3 and atom[i][1] == atom[j][1] :
                        c = atom[i][0] - atom[j][0]
                        board[i][j] = c
                        board[j][i] =c
                    #위에서 아래로 올때
                    elif atom[j][2] == 1 and atom[i][0]-atom[j][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[i][0]-atom[j][0] == atom[j][1]-atom[i][1]:
                        c = (atom[i][0]-atom[j][0]) + (atom[j][1]-atom[i][1])
                        board[i][j] = c
                        board[j][i] = c
                #기준원자가 위에서 아래로 내려올때
                elif atom[i][2] == 1 :
                    #비교원자가 왼쪽에서 오른쪽으로 올때
                    if atom[j][2] == 3 and atom[i][0]-atom[j][0] > 0 and atom[i][1]-atom[j][1] > 0 and atom[i][0]-atom[j][0] == atom[i][1]-atom[j][1]:
                        c = (atom[i][0]-atom[j][0]) + (atom[i][1]-atom[j][1])
                        board[i][j] = c
                        board[j][i] = c

    for i in range(n):
        if min(board[i]) == 9999999:
            crash[i] = 1
            continue
        if crash[i] == 0:
            find(i)
    print(f'#{t+1} {ans}')