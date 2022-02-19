'''
5천개의 버스정류장
1~5000
노선은 N개
i번째 노선은 번호가 Ai이상이고
Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇개의 버스노선이 다니는지 구하라

입력
tc 입력
n주어지고
n개의 줄에서
i번째 줄에는 Ai, Bi가 공백하나로 구분되어 주어짐
그다음 줄에는 1 <= P <= 500이 주어진다
P개의 줄에서
j번째줄에는 정수 Cj가 주어진다

출력
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수

해결방법
즉, 노선이 몇개인지 주어지고 각 노선들이 정류장 a~b사이 숫자들을 지나고
정류소번호 목록을 받는데 그 정류소번호들을 지나는 노선의 개수를 출력하라는 것

리스트하나 5000짜리를 만들어서
싹다 0으로 넣고
입력받는 노선들있으면 그 인덱스에 +1씩해주고
마지막에 입력받은 p값들을 인덱스로 해서 출력하면됨
'''

import sys
sys.stdin = open("input.txt")

tc = int(input())

for t in range(tc):
    n = int(input())
    stop_list = [0]*5000
    for i in range(n):
        start, end = map(int, input().split())
        for j in range(5000):
            if start <= j <= end :
                stop_list[j] += 1
    result = []
    m = int(input())
    for i in range(m):
        idx = int(input())
        result.append(stop_list[idx])

    print(f'#{t+1}', end=' ')
    for x in result :
        print(x, end=' ')
    print()



