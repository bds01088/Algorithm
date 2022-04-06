'''
그래프를
DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하시오
정점의 번호가 작은것부터 먼저 방문하고
더이상 방문할 점이 없는 경우 종료한다
정점 번호는 1부터 N번까지이다
N : 정점의 개수
M : 간선의 개수
V : 탐색을 시작할 정점의 번호
어떤 두 정점 사이에 여러개의 간선이 있을 수 있고
간선은 양방향이다
'''
from collections import deque

def BFS(startnode) :
    q = deque()
    visit = [0 for _ in range(n+1)]
    q.append(startnode)
    visit[startnode] = 1
    ans = [startnode]

    while q:
        now_node = q.popleft()
        for i in range(1, n+1):
            if board[now_node][i] != 0 and visit[i] == 0:
                q.append(i)
                ans.append(i)
                visit[i] = 1
    return ans

def DFS(startnode):
    q = deque()
    visit = [0 for _ in range(n + 1)]
    q.append(startnode)
    visit[startnode] = 1
    ans = []

    while q:
        now_node = q.pop()
        #사이클이 되는 그래프들이 들어오기 때문에
        #DFS이기 때문에 q에 먼저 들어갔다해서 완전히 방문한 것은 아니기때문에
        #팝된 시기에 답안에 넣어주어야한다
        if now_node not in ans:
            ans.append(now_node)
        visit[now_node] = 1
        #DFS임과 동시에 문제에서 같은 level이면 낮은 값을 가지고 있는 노드를 먼저 방문하기때문에
        #사이클이 안되는 경우를 대비해서
        #일단은 q에 큰수부터 작은수 순으로 역방향탐색하면서 맨 오른쪽에 작은수가 존재하도록한다
        for i in range(n, 0, -1):
            if board[now_node][i] != 0 and visit[i] == 0:
                q.append(i)


    return ans


n, m, v = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    board[node1][node2] = 1
    board[node2][node1] = 1

#노드의 번호가 작은것부터 먼저 방문해야한다
bfs_result = BFS(v)
dfs_result = DFS(v)
print(*dfs_result)
print(*bfs_result)
