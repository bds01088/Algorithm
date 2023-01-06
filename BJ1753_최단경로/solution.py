from collections import defaultdict
import heapq

def djikstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:

        dist, node = heapq.heappop(q)

        if distance[node] < dist :
            continue
        
        for next, cost in graph[node]:
            if distance[next] > distance[node]+cost :
                distance[next] = distance[node]+cost
                heapq.heappush(q, [distance[next], next])



N, V = map(int, input().split())
graph = defaultdict(list)
INF = 999999999
distance = [INF for _ in range(N+1)]

start = int(input())
for i in range(V):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])



djikstra(start)

for i in range(1, N+1):
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])