'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할때
가중치 합이 최소가 되는 경우의 그래프를 구하고
가중치 합을 출력하라
'''
import sys
sys.stdin = open('input.txt')

def findset(x):
    while p[x] != x :
        x = p[x]
    return x

def union(x,y):
    X = findset(x)
    Y = findset(y)
    if X < Y:
        p[Y] = X
    else :
        p[X] = Y

tc = int(input())

for t in range(tc):
    #v : 노드의 끝값 (0부터 시작)
    #e : 간선의 수
    v, e = map(int, input().split())

    #크루스칼로 풀자
    arr = []
    for i in range(e):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x : x[2])
    # print(arr)

    p = list(range(v+1))

    s = 0
    i = 0
    u = []
    while len(u) != v :
        if findset(arr[i][0]) != findset(arr[i][1]):
            union(arr[i][0], arr[i][1])
            s += arr[i][2]
            u.append(arr[i])
        i += 1
    print(f'#{t+1} {s}')


    ######################################
    #시간초과뜸
    # graph = [[9999]*(v+1) for _ in range(v+1)]
    #
    # for i in range(e):
    #     n1, n2, weight = map(int, input().split())
    #     graph[n1][n2] = weight
    #     graph[n2][n1] = weight
    # u = [0]
    # s = 0
    # ux = range(v+1)
    # while set(u) != set(ux) :
    #     m_weight = 9999
    #     m_node = -1
    #     for node in u :
    #         for i in list(set(ux)-set(u)):
    #             if graph[node][i] < m_weight :
    #                 m_weight = graph[node][i]
    #                 m_node = i
    #     u.append(m_node)
    #     s += m_weight
    # print(f'#{t+1} {s}')
