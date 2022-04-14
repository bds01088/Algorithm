'''
1부터 노드가 시작하고
각 노드(친구)를 가지는데 있어서 최소비용이 들도록 방문해야한다
연결되어있는 노드는 모두 친구가 되므로
연결된 집합체 중 친구비가 가장 적게 드는 친구를 선택하자
모두 못사귀면 oh no를 출력하면된다고했음
크루스칼 알고리즘을 쓰면 쉽게 풀릴듯함
'''

import sys
sys.stdin = open('input.txt')

def findp(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    x = findp(x)
    y = findp(y)
    if x != y :
        parent[y] = x


n, m, k = map(int, input().split())

#일단 parent 리스트 만들어야됌
parent = [i for i in range(n+1)]

friend_cost = [0] + list(map(int, input().split()))

for i in range(m):
    node1, node2 = map(int, input().split())
    if friend_cost[findp(node1)] > friend_cost[findp(node2)]:
        union(node2, node1)
    else :
        union(node1, node2)

pay = 0
visit = []

for i in range(1, n+1):
    if findp(i) == i :
        visit.append(i)
        if pay+friend_cost[i] <= k :
            pay += friend_cost[i]
        else :
            pay = 'Oh no'
            break
print(pay)