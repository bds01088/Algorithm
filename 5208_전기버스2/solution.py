'''
정류장 마다 배터리가 있다
해당 idx에 배터리를 추가한 만큼의 idx로 이동할 수 있다
1 2 3 4 5
2 3 1 1
일때
2번 정류장에서 미리 배터리를 교체하면
추가 교체없이 목적지에 도착 가능하다

입력
정류장 수, 정류장 수-1개의 정류장 별 배터리 용량 리스트

모든 경우의 수를 다 해보는 걸 바탕으로하자
일단 1번 정류장은 무조건 이용해야함
1번정류장 이용은 횟수에 포함되지 않는다
그럼 1번에서 얻은 이동거리 내의 인덱스를 모두 방문할 수 있다
배터리 용량은 최소 1이다
배터리 용량이 가장 큰 정류장에서 새로 출발했을 때 거리가
지금 정류장의 최대 거리보다 클 경우에만
가능성 있는 방문지로 넣자

5 2 5 2 4 3 1 1 0일때
          까지 갈수있고
          마지막을 이용하면 1번 충전하고 끝
    5를 이용하면?
    도착지 -1지점에 도착함
    2번충전해야함
    5 2 4 2 1 1 0일 경우
    마지막인 2를 이용하면 또 2번충전해야함
    근데 4를 이용하면 1번만에 감

'''

import sys
sys.stdin = open('input.txt')

def findmincharge():
    cnt = 0
    start = 1
    #종료조건으로 시작지점에서 최대 갈 수 있는 거리가
    #도착지의 거리를 넘어설 때 까지
    while start+battery[start] < destination :
        #최대 이동 거리
        mmax = 0
        #최대 이동 거리를 가지는 인덱스값
        imax = start
        #출발지점은 포함안하니까
        #start+1부터 최대 이동할 수 있는 지점 start+battery[start]을 포함해야 해서 +1
        for i in range(start+1, start+battery[start]+1) :
            #만약 해당 지점의 최대 이동거리가 가장 크다면
            #거기를 다음 시작 좌표로 하기 위해 최대값과 인덱스값을 저장
            if mmax <= battery[i]+i :
                mmax = battery[i]+i
                imax = i
        #새로 구한 최대 이동 거리가
        #현재 지점에서 최대 이동가능한 거리보다 크다면
        #그곳을 새 시작점으로 잡아줌
        if start+battery[start] < imax+mmax :
            cnt += 1
            start = imax
        #만약 새로 구한 최대 이동 거리가
        #현재 좌표에서의 최대 이동 거리 보다 작거나 같다면
        #굳이 그 좌표를 쓸 필요가 없으니까
        #그냥 맨 마지막 좌표를 다음 좌표로 사용하자
        else :
            start += battery[start]
    return cnt

def DFS():
    start = 1
    stack = []
    stack.append([start,0])

    #스택에 현재 위치에서 갈 수 있는 좌표들 다 넣어준다
    #근데 visit 쓰면 안됌
    #재귀라면 들어가고 난 다음 나왔을때 초기화함으로써
    #visit의 초기화를 이룰 수 있는데
    #while, stack으로 하면
    #초기화 해 줄 방법이 없음
    ans = destination
    while stack :
        now, cnt = stack.pop()
        #가지치기
        if cnt >= ans :
            continue
        #종료조건
        if now+battery[now] >= destination :
            if cnt < ans :
                ans = cnt
            continue
        for next in range(now+1, now+battery[now]+1) :
            if next < destination :
                stack.append([next, cnt+1])
    return ans


tc = int(input())

for t in range(tc):
    temp = list(map(int, input().split()))
    destination = temp[0]
    battery = [0] + temp[1:]
    result = DFS()
    print(f'#{t+1} {result}')
