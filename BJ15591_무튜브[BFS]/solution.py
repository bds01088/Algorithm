from collections import deque, defaultdict
import sys

input = lambda : sys.stdin.readline().strip()

n, Q = map(int, input().split())
E = 1000000001

board = defaultdict(list)


for i in range(n-1):
    a, b, v = map(int, input().split())
    board[a].append([b, v])
    board[b].append([a, v])

#defaultdict(<class 'list'>, {1: [[2, 3]], 2: [[1, 3], [3, 2], [4, 4]], 3: [[2, 2]], 4: [[2, 4]]})

for i in range(Q):
    k, start = map(int, input().split())
    cnt = 0
    visit = [0 for _ in range(n+1)]

    q = deque()
    q.append([start, E])
    visit[start] = 1

    while q :
        srow, usado = q.popleft()

        for node, next_usado in board[srow] :
            if visit[node] == 0 and min(usado, next_usado) >= k :
                cnt += 1
                q.append([node, min(usado, next_usado)])
                visit[node] = 1
                

    print(cnt)
