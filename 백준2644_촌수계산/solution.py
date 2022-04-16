'''
입력받은 두사람의 촌수를 출력하라
친척관계가 없어 촌수를 계산 못하면 -1출력

BFS
'''

import sys
sys.stdin = open('백준2644_촌수계산/input.txt')
from collections import deque

def BFS(start, end):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n+1)]
    visit[start] = 1

    while q :
        now = q.popleft()

        if now == end :
            return visit[now]-1
        
        for i in range(1,n+1):
            if board[now][i] == 1 and visit[i] == 0 :
                q.append(i)
                visit[i] = visit[now]+1
    return -1


#사람 수 1부터 시작함
n = int(input())
x, y = map(int, input().split())
#간선 수
m = int(input())

board = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    board[node1][node2] = 1
    board[node2][node1] = 1

result = BFS(x, y)

print(result)