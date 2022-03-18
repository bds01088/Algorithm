'''
시작점으로부터 시작해서 가장 멀리 떨어진 노드의 val값이 가장 큰 것을 추출하라
거리가 동일하다면 val이 큰것을 출력
'''

import sys
sys.stdin = open('input.txt')

def BFS(start):
    q = []
    visit = [0]*101
    q.append(start)
    visit[start] = 1
    answer = start

    while q :
        now = q.pop(0)
        #더 멀리 갔거나, 같은 거리를 떨어져 있고, 값이 더 작다면
        if visit[answer] < visit[now] or visit[answer] == visit[now] and answer < now :
            answer = now

        for i in range(1, 101):
            #지금 노드와 연결되어있으면서, 방문한 적 없는 곳
            if board[now][i] == 1 and visit[i] == 0 :
                #대기열에 넣어줌과 동시에
                q.append(i)
                #방문한것과 동일하므로 바로 방문리스트에 추가함
                #방문표시와 같이 거리를 측정하기 위해
                #now보다 거리 1이 더 늘어난 것을 추가
                visit[i] = visit[now]+1
    return answer


for t in range(1,11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [[0]*101 for _ in range(101)]

    for i in range(n//2) :
        board[arr[i*2]][arr[i*2+1]] = 1

    result = BFS(start)
    print(f'#{t} {result}')