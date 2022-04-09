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

tc = int(input())

#상 하 좌 우
#0  1  2  3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for t in range(tc):
    n = int(input())
    atom = []
    crash = [0 for _ in range(n)]
    for i in range(n) :
        row, col, direction, energy = map(int, input().split())
        atom.append([row*2,col*2, direction, energy])
        
    ans = 0
    for _ in range(4002):
        del_list = []
        v = []
        trash_list = []
        #시작좌표가 동일한 적은 없다 했으니 이동부터 하자
        for i in range(len(atom)):
            atom[i][0] += dx[atom[i][2]]
            atom[i][1] += dy[atom[i][2]]
            if abs(atom[i][0]) > 2000 or abs(atom[i][1]) > 2000 :
                trash_list.append([atom[i][0],atom[i][1]])

        for i in range(len(atom)):
            x, y = atom[i][0], atom[i][1]
            if [x,y] in v:
                del_list.append([x,y])
            else :
                v.append([x,y])

        for i in range(len(atom)):
            prob = 0
            for j in range(len(atom)):
                #위로 이동하는데 y값이 더 큰게 없다면 가망성x
                if atom[i][2] == 0 and atom[i][1] < atom[j][1]:
                    prob += 1
                #아래로 이동할때 y값이 더 작은게 없다면 가망성x
                elif atom[i][2] == 1 and atom[i][1] > atom[j][1] :
                    prob += 1
                #왼쪽으로 이동할때 x값이 더 작은게 없으면 가망성x
                elif atom[i][2] == 2 and atom[i][0] > atom[j][0] :
                    prob += 1
                elif atom[i][2] == 3 and atom[i][0] < atom[j][0] :
                    prob += 1
            if prob == 0:
                trash_list.append([atom[i][0],atom[i][1]])
        if del_list:
            for i in range(len(atom)-1, -1, -1):
                if [atom[i][0], atom[i][1]] in del_list:
                    ans += atom[i][3]
                    atom.pop(i)

        if trash_list :
            for i in range(len(atom)-1, -1, -1):
                if [atom[i][0], atom[i][1]] in trash_list:
                    atom.pop(i)
        
        if len(atom) < 2:
            break

    print(f'#{t+1} {ans}')