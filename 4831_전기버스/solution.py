'''
문제
0번에서 출발해 n번 정류장까지 이동해야한다
한번에 이동할 수 있는 정류장 수 K
충전기가 설치된 m개의 정류장 번호가 주어진다.
최소한 몇번의 충전을 해야 종점에 도착하는 지 구해야한다
충전기 설치가 잘못되어 종점에 도착 못할 경우 0을 출력한다

입력
노선수 t == 테스트케이스 수
이동거리k 종점n 충전기수m
충전기가 설치된 정류장 번호들

출력
#테스트케이스번호 결과값

해결방법
이동거리 내에 충전소가 있어야한다
버스위치에서 +k 거리 내에 있어야하는데 만약 여러개면?
충전소 위치가 가장 먼 것을 골라야하는데
일단은 버스위치에서 +k 거리를 인덱스로 표시해서 리스트를 만들고
충전소의 인덱스가 리스트안에 있으면 그 중에서 가장 큰 인덱스를 들고오는 걸로
리스트 안에 없으면 break하고 바로 0 리턴하자
충전소의 위치도 리스트로 있으니까
set으로 변환해서 교집합이 있는지 여부만 알면 되지않을까?
'''

import sys
sys.stdin = open('input.txt')

def min_sup(k, n, sups):
    #버스의 현재위치 초기값
    bus = 0
    #충전회수 초기값
    cnt = 0
    #버스가 이동 가능한 거리 내에 n 값이 있다면 while문이 끝나도록 함
    while bus+k < n :
        #버스의 이동거리 내에 있는 정류장 위치를 list로 가져옴
        movable = list(range(bus+1, bus+k+1))
        #movable리스트와 충전소가 있는 정류장 리스트의 합집합을 구한다
        chargeable = list(set(sups)&set(movable))
        #만약 충전할 곳이 거리 내에 없다면 종점까지 못가므로 return 0을 한다
        if not chargeable :
            return 0
        #충전소가 있다면
        else :
            m = 0
            #가장 뒤쪽의 충전소를 사용해야하므로 idx의 max값을 구해준다
            for i in chargeable:
                if i > m :
                    m = i
            #가장 뒤쪽의 충전소를 기준으로 다시 이동거리를 계산해야하므로 bus위치를 m으로 바꿔준다
            bus = m
            #충전을 했으므로 횟수를 1증가시킨다
            cnt += 1
    return cnt

tc = int(input())

for t in range(tc):
    k, n, m = map(int, input().split())
    sup_list = list(map(int, input().split()))
    result = min_sup(k, n, sup_list)
    print(f'#{t+1} {result}')