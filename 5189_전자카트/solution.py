'''
사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야한다
각 구역은 한번씩만 방문하며
돌아왔을때 최소 배터리 사용량을 구해야한다
사무실의 인덱스는 1이고
2부터 n까지의 인덱스는 관리구역 번호다

일단 시작지점은 사무실이니까
row가 1인곳을 시작으로하고
출발지점을 row 도착지점을 col로 사용하자
'''

import sys
sys.stdin = open('input.txt')

def DFS(start_point, path, visit):
    global mmin
    #가지치기
    if path > mmin:
        return

    #종료 조건
    if all(visit) == 1:
        path += board[start_point][1]
        if path < mmin :
            mmin = path
        path -= board[start_point][1]
        return

    else :
        for i in range(2, n+1):
            if visit[i] == 0 and i != start_point:
                path += board[start_point][i]
                visit[i] = 1
                DFS(i, path, visit)
                path -= board[start_point][i]
                visit[i] = 0



tc = int(input())

for t in range(tc):
    n = int(input())
    board = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        temp = list(map(int, input().split()))
        for j in range(1, n+1):
            board[i][j] = temp[j-1]

    visit = [0 for _ in range(n + 1)]
    visit[0] = visit[1] = 1

    mmin = 100000000
    path = 0
    DFS(1, path, visit)

    print(f'#{t+1} {mmin}')
