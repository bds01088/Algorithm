'''
단방향 그래프
가장 많은 컴퓨터를 해킹할 수 있는 번호를 오름차순으로 출력

메모리 초과시 2차원배열은 안쓰도록해야한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    global n, board, mmax, result
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n+1)]
    visit[start] = 1
    cnt = 1
    while q :
        now = q.popleft()
        for i in board[now]:
            if visit[i] != 1 :
                q.append(i)
                cnt += 1
                visit[i] = 1
    if cnt > mmax :
        result = [start]
        mmax = cnt
    elif cnt == mmax :
        result.append(start)
    else :
        return

n, v = map(int, input().strip().split())

board = [[]for _ in range(n+1)]


for i in range(v):
    a, b = map(int, input().strip().split())
    board[b].append(a)

result = []
mmax = 0

for i in range(1,n+1) :
    BFS(i)

for ele in sorted(result) :
    print(ele, end=' ')