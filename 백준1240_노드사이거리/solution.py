'''
n, m
n개의 간선정보
node1, node2, distance
이후
m개의 찾는 node1,node2
그리고 찾는 노드의 거리를 출력
'''

import sys
sys.stdin = open('input.txt')
from collections import deque
def BFS(snode, enode):
    q = deque()
    q.append(snode)
    visit = [0 for _ in range(n+1)]
    visit[snode] = 1

    while q:
        node = q.popleft()
        if node == enode :
            return visit[node]-1
        for i in range(1, n+1):
            if board[node][i] != 0 and visit[i] == 0:
                q.append(i)
                visit[i] = visit[node] + board[node][i]
    return 0


n, m = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(n-1):
    node1, node2, distance = map(int ,input().split())
    board[node1][node2] = distance
    board[node2][node1] = distance

for i in range(m):
    fromtarget, totarget = map(int, input().split())
    print(BFS(fromtarget, totarget))
