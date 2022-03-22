'''
미로가 주어진다
2에서 출발해서 3까지 도착하는데 걸리는 시간을 출력하시오
시간은 가는 동안의 거친 0의 개수를 출력하면 된다
'''

import sys
sys.stdin = open('input.txt')

def BFS(si, sj):
    q = []
    visit = [[0]*n for _ in range(n)]
    visit[si][sj] = 1
    q.append([si,sj])

    while q :
        ci, cj = q.pop(0)
        for d in range(4):
            ni = ci+direction[d][0]
            nj = cj+direction[d][1]
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] == 0 and board[ni][nj] != 1:
                q.append([ni,nj])
                visit[ni][nj] = visit[ci][cj]+1
                if board[ni][nj] == 3:
                    return visit[ni][nj]
    #길이 없을 경우
    return 0


tc = int(input())

direction = [[-1,0],[1,0],[0,-1],[0,1]]

for t in range(tc):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        temp = input()
        for j in range(n):
            board[i][j] = int(temp[j])
            if int(temp[j]) == 2 :
                si = i
                sj = j

    result = BFS(si, sj)
    #BFS에서 visit을 가져오기때문에
    #visit은 시작지점이 1이고 시작지점을 기준으로 +1하기 때문에
    #목적지와 출발지의 사이에 존재하는 0의 개수는
    #시작지점과 도착지점을 빼준 result-2값이다
    if result != 0 :
        result = result-2
    print(f'#{t+1} {result}')
