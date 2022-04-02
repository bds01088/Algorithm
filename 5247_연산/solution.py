'''
자연수 n에 몇번의 연산을 통해 다른 자연수 m을 만들려고 한다
사용할 수 있는 연산은
+1, -1, *2, -10 네가지 뿐이고
최소 몇번의 연산을 거쳐야하는지 알아내자
단, 연산 중간 결과도 항상 백만 이하의 자연수여야 한다

그러면 BFS로 하자
+1로 먼저 걸렸을때는 너무 오래걸릴거같음
모든 경우를 돌고
해당 연산을 한 뒤에 목적 값과 비교해주면서 가지치자

#1 3
#2 4
#3 8
'''

import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(value, target):
    global ans
    q = deque()
    cnt = 0
    visit = [0 for _ in range(1000001)]
    q.append([value, cnt])
    visit[value] = 1

    while q :
        now, ncnt = q.popleft()
        if ncnt > ans :
            continue
        if now == target :
            if ncnt < ans :
                ans = ncnt
        else :
            next = now+1
            next_cnt = ncnt+1
            if 1 <= next < 1000001 and visit[next] == 0 :
                q.append([next, next_cnt])
                visit[next] = 1

            next = now * 2
            if 1 <= next < 1000001 and visit[next] == 0:
                q.append([next, next_cnt])
                visit[next] = 1

            next = now-1
            if 1 <= next < 1000001 and visit[next] == 0:
                q.append([next, next_cnt])
                visit[next] = 1

            next = now-10
            if 1 <= next < 1000001 and visit[next] == 0:
                q.append([next, next_cnt])
                visit[next] = 1
    return ans

tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    ans = 9999999
    result = BFS(n, m)
    print(f'#{t+1} {result}')
