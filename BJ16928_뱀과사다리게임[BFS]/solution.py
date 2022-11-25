import sys
from collections import defaultdict, deque

input = lambda : sys.stdin.readline().strip()

def BFS(start):
    global ans, board, link

    q = deque()
    q.append(start)
    visit[start] = 1
    
    while q :
        now = q.popleft()
        turn = visit[now]

        if now == 100 :
            if turn < ans :
                ans = turn
            continue
        
        for i in range(6, 0, -1):
            future = now+i
            
            if future > 100 :
                continue

            if visit[future] != 0 and visit[future] <= turn+1 :
                continue

            if board[future] == 1 :
                q.append(link[future])
                visit[link[future]] = turn+1
                visit[future] = turn+1
            elif board[future] == 0 :
                q.append(future)
                visit[future] = turn+1
            else :
                q.append(link[future])
                visit[link[future]] = turn+1
                visit[future] = turn+1
                




ladderN, snakeN = map(int, input().split())

link = defaultdict(int)

board = [ 0 for _ in range(101)]
visit = [ 0 for _ in range(101)]

for i in range(ladderN):
    a, b = map(int, input().split())
    link[a] = b
    board[a] = 1

for i in range(snakeN):
    a, b = map(int, input().split())
    link[a] = b
    board[a] = 2
ans = 100
BFS(1)
print(ans-1)