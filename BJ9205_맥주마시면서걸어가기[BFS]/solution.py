'''
맥주는 20개가 최대, 편의점의 수 n은 100이하
어느 좌표에서 출발하기 전에 1병을 마시고 출발함
50미터마다 1병씩 마셔야됌
20*50 = 1000미터를 갈 수 있음
좌표는 -32768~32767 사이값으로 들어옴
맨하튼 거리로 이동
즉 1000미터 범위 내에 편의점이 없으면 sad
있으면 보충하고 계속 이동하는 걸로
도착하면 happy

그렇다면 갈 수 있는 모든 편의점들을 들리고
visit를 작성하고
어떻게든 페스티벌에 도착한다면 happy 끝끝내 못가면 sad
'''

from collections import deque

def Solution(startXY):
    global result

    q = deque()
    q.append(startXY)
    #먼저 좌표에서 갈 수 있는 지점을 구해야함
    while q :
        XY = q.popleft()
        for loc in locations :
            MX = abs(loc[0] - XY[0])
            MY = abs(loc[1] - XY[1])
            #맨하탄 거리로 1000미터 이내라면
            if loc[2] != 1 and (MX+MY) <= 1000 :
                #loc가 페스티벌이면 리턴
                if loc == festival :
                    result = True
                    return
                #페스티벌 아니면 visit처리
                loc[2] = 1
                q.append(loc)


t = int(input())

for _ in range(t):
    n = int(input()) #맥주를 파는 편의점의 개수
    home = list(map(int,input().split()))
    storeList = []
    for i in range(n):
        #+[0]은 visit
        storeList.append(list(map(int,input().split()))+[0])
    festival = list(map(int,input().split()))+[0]
    #순회를 위해 festival을 합친 리스트를 만든다
    storeList.append(festival)
    locations = storeList
    # print(locations)

    result = False
    Solution(home)
    if result == False:
        print("sad")
    else :
        print("happy")