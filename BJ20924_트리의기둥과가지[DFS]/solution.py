import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def bodyAndGigaNode(start) :
    global graph, visit
    root = start
    body = 0
    gigaNode = 0
    noLeaf = False

    while len(graph[start]) < 3 :
        visit[start] = True
        #리프가 없다면?
        if len(graph[start]) == 1 or len(graph[start]) == 0:
            noLeaf = True
            break
        #루트가 기가노드임과 동시에 2개의 리프노드만 가진다면,
        #딕셔너리에 2개의 노드 정보만 들고 있으므로
        #루트에다가 자기 스스로에 대한 노드정보를 넣어줌으로써 길이를 맞춰줄까..?
        for node, dist in graph[start] :
            if visit[node] == False :
                body += dist
                start = node

    gigaNode = start

    return (body, gigaNode, noLeaf)

def DFS(start, D):
    global graph, branch
    
    for node, dist in graph[start] :
        if visit[node] == False :
            visit[node] = True
            DFS(node, D+dist)
    
    if D > branch :
        branch = D

    return

input = lambda : sys.stdin.readline().strip()

N, R = map(int, input().split())

graph = defaultdict(list)

visit = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b, d = map(int, input().split())
    #그냥 연결되어있다만 주는 것이기 때문에 한쪽이 루트고 한쪽이 리프인지 판별 못함
    graph[a].append([b, d])
    graph[b].append([a, d])

#루트 노드가 가지고 있는 노드정보의 개수가 다른 노드와 달리 1개가 부족하기 때문에
#스스로에대한 정보를 가짜로 넣어주자
graph[R].append([R, 0])
visit[R] = True

body, giga, noleaf = bodyAndGigaNode(R)

if noleaf :
    print(body, 0)
else :
    branch = 0
    visit[giga] = True
    for node, dist in graph[giga]:
        if visit[node] == False :
            visit[node] = True
            DFS(node, dist)
    print(body, branch)