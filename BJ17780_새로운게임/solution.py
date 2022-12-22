import copy
N, K = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
#0:흰색, 1:빨간색, 2:파란색

#우, 좌, 상, 하
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

unit = []
direction = []
isStacked = []
stackList = []
for i in range(K):
    x, y, d = map(int, input().split())
    unit.append([x-1, y-1])
    direction.append(d-1)
    isStacked.append(0)
    stackList.append([i])

turn = 0

flag = 0

while True :
    turn += 1
    if turn == 3 :
        xxx = 1
    for i in range(K):
        #가장 밑에 존재하는 말이면, 움직이자
        if isStacked[i] == 0 :
            nrow = unit[i][0]+dr[direction[i]]
            ncol = unit[i][1]+dc[direction[i]]
            uTurn = False
            #다음 행선지에 따른 분기 해주기
            if N <= nrow or nrow < 0 or N <= ncol or ncol < 0 or board[nrow][ncol] == 2 :
                #보드 범위를 벗어나면 파란색과 같음
                #방향 반대로 해줘야하니까, 짝수면 +1, 홀수면 -1 해주자
                if direction[i]%2 :
                    direction[i] -= 1
                else :
                    direction[i] += 1
                nrow = unit[i][0]+dr[direction[i]]
                ncol = unit[i][1]+dc[direction[i]]
                # N이 최소 4라 범위 벗어나서 방향 바꼈을때 또 범위 벗어나는 일은 없음
                # uTurn = True
                #만약 파란색이나 범위가 벗어나서 방향을 바꾼뒤, 이동해야하는데
                #해당 이동 지역도 파란색이거나 범위를 벗어나면 제자리에 있기
                #일단 uTurn을 했다는 flag만 변경해주고 아래에서 처리하자
            
            #흰, 빨, 파 다 처리해줘야함
            #파란색일 경우 이미 위에서 파란색이거나
            #범위를 벗어났거나 처리했기 때문에
            #그럼에도 파란색이므로 방향전환만 해주고 가만히 있자
            if 0 <= nrow < N and 0 <= ncol < N :
                #흰색일 때, 
                if board[nrow][ncol] == 0 :
                    isUnit = False
                    #모두 돌아 해당 위치인 유닛을 찾아보자
                    for j in range(K):
                        #해당 위치에 유닛이 있다면, 가장 밑에 있는 유닛을 찾아야함
                        if [nrow, ncol] == unit[j] and isStacked[j] == 0 :
                            stackList[j].extend(stackList[i])
                            isUnit = True
                            if len(stackList[j]) >= 4 :
                                flag = 1
                            #움직인 말은 가장 밑이 아니게 되므로
                            isStacked[i] = 1
                            break
                    #유닛이 없다면?
                    if isUnit == False :
                        unit[i][0] = nrow
                        unit[i][1] = ncol

                #빨간색일 경우
                elif board[nrow][ncol] == 1 :
                    stackList[i].reverse()
                    newStackList = copy.deepcopy(stackList[i])
                    isStacked[i] = 1
                    newBottom = stackList[i][0]
                    isStacked[newBottom] = 0
                    stackList[newBottom] = newStackList
                    #업혀 와서 위치 갱신 해줘야 됌
                    unit[newBottom][0] = nrow
                    unit[newBottom][1] = ncol

                    for j in range(K):
                        if [nrow, ncol] == unit[j] and j != newBottom and j != i and isStacked[j] == 0 :
                            stackList[j].extend(stackList[newBottom])
                            if len(stackList[j]) >= 4 :
                                flag = 1
                            #움직인 말은 가장 밑이 아니게 되므로
                            isStacked[newBottom] = 1
                            break
            else :
                continue

        if flag == 1 :
            break

    if flag == 1 :
        print(turn)
        break
    if turn >= 1000 :
        print(-1)
        break