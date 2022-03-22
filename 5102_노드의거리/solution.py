'''
V와 E가 주어지는데
E개만큼 간선을 받고
시작노드와 도착노드를 받는다
노드 번호는 1번부터 V번까지 존재하며
시작과 도착이 연결 안되어있다면 0을 출력
'''

import sys
sys.stdin = open('input.txt')

def BFS(start, end):
    q = []
    q.append(start)
    visit = [0 for _ in range(V+1)]
    visit[start] = 1
    while q :
        now = q.pop(0)
        for x in range(1, V+1) :
            if arr[now][x] == 1 and visit[x] == 0:
                q.append(x)
                visit[x] = visit[now] + 1
                #BFS라 거리측정을 동시에 하니까 동 시간대에 가장 먼저 도착노드에 도착하면
                #그게 최소값이지 않은가?
                if x == end :
                    #시작값 빼주기
                    return visit[x]-1
    return 0



tc = int(input())

for t in range(tc):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(1, E+1):
        p, c = map(int, input().split())
        arr[p][c] = 1
        arr[c][p] = 1
    start, end = map(int, input().split())

    result = BFS(start, end)

    print(f'#{t+1} {result}')