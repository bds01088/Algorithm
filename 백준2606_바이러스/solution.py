'''
그래프가 주어지고
1번부터 노드는 시작한다
1번이 감염되면 연결된 모든 노드가 감염되는데
총 몇개가 감염되는지 출력하라
1은 포함 안되는듯
'''
from collections import deque

def BFS(startnode):
    q = deque()
    q.append(startnode)
    cnt = 0
    visit = [0 for _ in range(n+1)]
    visit[startnode] = 1

    while q:
        now = q.popleft()
        for i in range(1, n+1):
            if board[now][i] == 1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1
                cnt += 1
    return cnt


n = int(input())
m = int(input())

board = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    board[node1][node2] = 1
    board[node2][node1] = 1

result = BFS(1)
print(result)