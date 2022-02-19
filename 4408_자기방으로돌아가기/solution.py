'''
방은 4백개
홀수방과 짝수방 사이에 복도가 존재한다
예를 들어 (방1 -> 4) 와 (방3 -> 6) 은 복도 구간이 겹치므로 한 사람은 기다렸다가 다음 차례에 이동해야 한다.
이동하는 데에는 거리에 관계없이 단위 시간이 걸린다고 하자.
각 학생들의 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때,
최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지를 구하시오.
'''

import sys
sys.stdin = open("input.txt")

tc = int(input())

for t in range(tc):
    n = int(input())
    room_list = [0]*400

    for i in range(n):
        start, end = map(int, input().split())
        #작은수에서 큰수로 가도록 고정
        if start > end :
            start, end = end, start
        #홀수 출발 홀수 도착시
        if start%2 == 1 and end%2 == 1:
            #도착하는방 아랫방까지 영향을 주기때문에 도착에 +1함
            end += 1
        #홀수 출발 짝수 도착시
        elif start%2 == 1 and end%2 == 0:
            #출발하는 방부터 도착하는 방까지만 영향줌
            pass
        #짝수 출발 짝수 도착시
        elif start%2 == 0 and end%2 == 0:
            #출발하는 방 윗방에 영향을 주기때문에 -1함
            start -= 1
        #짝수 출발 홀수 도착시
        elif start%2 == 0 and end%2 == 1:
            #도착방의 아랫방까지 영향을 주기때문에 +1함
            end += 1

        for j in range(400):
            if start <= j <= end :
                room_list[j] += 1
    print(f'#{t+1} {max(room_list)}')