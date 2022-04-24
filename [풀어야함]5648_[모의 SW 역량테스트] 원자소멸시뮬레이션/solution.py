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

# def find(startnode):
#     global crash, ans, atom, board
#     node = startnode
#     while crash[node] != 1:
#         #시작원자에서 가장 작은 거리를 가진 원자번호 구하기
#         idx = board[node].index(min(board[node]))
#         #만약 그 원자가 안사라져있고, 거기서 최솟값이 시작원자와 같다면
#         #시작원자 A와 가장 작은 거리를 가진 원자 B가 제일 먼저 부딧힘
#         if crash[idx] == 0 and min(board[idx]) == min(board[node]) :
#             #B와의 강능성이 있는 노드들 중 동시에 부딧히는 원자가 더 있는지 확인하고
#             for j in range(n):
#                 #있다면 답에 에너지 넣어주고 충돌했다고 상태를 변경해줌
#                 if board[idx][j] == min(board[idx]):
#                     #최소한 A원자는 값이 더해짐
#                     ans += atom[j][3]
#                     crash[j] = 1
#             #마지막으로 B의 에너지를 넣어줌
#             ans += atom[idx][3]
#             crash[idx] = 1
#         #시작원자 A의 최소거리와 A의 최소거리에 해당하는 원자 B의 최소거리가 다르다면
#         #B는 다른 원자 C와 먼저 부딧혀 소멸할 것이다
#         #그러나 C가 먼저 따른원자 D와 부딧혀 소멸하면, B의 최소거리 원자는 달라질 것이다
#         #이걸 어떻게 해결하지?
#         else :
#             x = min(board[idx])
#             newstartnode = board[idx].index(x)
#             find(newstartnode)

def find(startnode):
    global crash, ans, atom, board
    #이미 각 노드별로 최소값을 구했다.
    #board에서 최소값과 같은 곳들은 다 동시에 부딧히는거임
    mmin = min(board[startnode])
    for j in range(n):
        if startnode != j:
            mmmin = min(board[j])
            if mmin == mmmin :
                ans += atom[j][3]
                crash[j] = 1
        

tc = int(input())

#상 하 좌 우
#0  1  2  3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for t in range(tc):
    n = int(input())
    ans = []
    atom = []
    board = [[9999999]*n for _ in range(n)]
    crash = [0 for _ in range(n)]
    for i in range(n) :
        x, y, direction, energy = map(int, input().split())
        atom.append([x*2,y*2, direction, energy])
    
    #가망성 있는 원자와의 거리 구하기
    for i in range(n):
        for j in range(n):
                #기준원자의 방향이 위로 갈때
                if atom[i][2] == 0 :
                    #비교원자의 방향이 아래일때
                    if atom[j][2] == 1 and atom[i][0] == atom[j][0] :
                        c = atom[j][1] - atom[i][1]
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c
                    #오른쪽에서 왼쪽으로 올때
                    elif atom[j][2] == 2 and atom[j][0]-atom[i][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[j][0]-atom[i][0] == atom[j][1]-atom[i][1] :
                        c = (atom[j][0]-atom[i][0]) + (atom[j][1]-atom[i][1])
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c
                    #왼쪽에서 오른쪽으로 올때
                    elif atom[j][2] == 3 and atom[i][0] - atom[j][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[i][0]-atom[j][0] == atom[j][1]-atom[i][1] :
                        c = (atom[i][0]-atom[j][0]) + (atom[j][1]-atom[i][1])
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c
                # #기준원자의 방향이 왼쪽으로 갈때
                elif atom[i][2] == 2 :
                    #비교원자의 방향이 오른쪽으로 움직일때
                    if atom[j][2] == 3 and atom[i][1] == atom[j][1] :
                        c = atom[i][0] - atom[j][0]
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c
                    #위에서 아래로 올때
                    elif atom[j][2] == 1 and atom[i][0]-atom[j][0] > 0 and atom[j][1]-atom[i][1] > 0 and atom[i][0]-atom[j][0] == atom[j][1]-atom[i][1]:
                        c = (atom[i][0]-atom[j][0]) + (atom[j][1]-atom[i][1])
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c
                #기준원자가 위에서 아래로 내려올때
                elif atom[i][2] == 1 :
                    #비교원자가 왼쪽에서 오른쪽으로 올때
                    if atom[j][2] == 3 and atom[i][0]-atom[j][0] > 0 and atom[i][1]-atom[j][1] > 0 and atom[i][0]-atom[j][0] == atom[i][1]-atom[j][1]:
                        c = (atom[i][0]-atom[j][0]) + (atom[i][1]-atom[j][1])
                        if board[i][j] > c and board[j][i] > c:
                            board[i][j] = c
                            board[j][i] = c

    #모든 원자들의 결과가 정해질때까지 반복
    #충돌되거나, 가능성 있는 짝이 없다거나 
    while sum(crash) != n :
        #가능성 board를 완전탐색을 계속 반복할거임
        for i in range(n):
            #만약 아래 코드들을 돌면서 crash가 되어 결과가 정해진 i값이면 continue로 스킵해주고
            if crash[i] == 1 :
                continue
            #현재 i의 최소값을 구하고
            mmin = min(board[i])
            #근데 가능성이 하나도 없어서 맥스값이 최소값으로 뜨면 가능성 있는 짝이 없다는 거니까 crash를 1로 해줌
            if mmin == 9999999 :
                crash[i] = 1
                continue
            #결과가 정해지지않거나 가망성이 있는 짝이 존재하는 상황이라면
            for j in range(n):
                #자기자신이 아니고, 해당 i에서 가지고있는 최소값인 j열을 찾는다
                if i != j and board[i][j] == mmin:
                    #i와 최소값으로 연결된 j값이 지금 당장 i값과 충돌할 것인가는 j가 가장먼저 만나는 값이 i일 경우에 가능하다
                    mmmin = min(board[j])
                    #그러므로 mmin과 mmmin이 같다면 i와 j는 가장 먼저 충돌하는 것
                    if mmin == mmmin and crash[j] == 0:
                        ans.append(atom[j])
                        #i와 j를 충돌한 결과로 만들어주고
                        crash[j] = 1
                        crash[i] = 1
                        #여러개가 부딧힐 가능성을 생각해서 A에서 B를 먼저만나고 나중에 C도 부딧히는데 for문이
                        #0부터 n까지 차례대로 탐색하니까
                        #나중에 C를 발견해도 A는 중복해서 들어가면 안되니까 중복 걸러주기
                        if atom[i] not in ans :
                            ans.append(atom[i])
                    #만약에 mmin과 mmmin이 같지만 j가 이미 충돌해서 결과가 정해진 친구라면
                    #i에게 j는 더이상 가망성이 없는것이니
                    #맥스값으로 바꾸어준다
                    elif crash[j] == 1 :
                        board[i][j] = 9999999
                        #또한 while반복을 돌면서 i가 완전히 가망성이 사라질때까지 돌아야하므로
                        #mmin값을 변경한다음 탐색하기 위해 break해준다
                        break

    print(f'#{t+1}', end=' ')
    ss = 0
    #원자정보자체를 ans에 추가해줬기때문에
    for aa, bb, cc, dd in ans:
        #4번째에 충돌에너지들을 모두 더해준다
        ss += dd
    print(ss)