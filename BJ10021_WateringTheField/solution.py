'''
MST 문제니까
union find 써야함 -> 사이클이 없는 그래프여야 하기 때문에
근데 밭과 밭 사이에 길이가 최소인 지점을 구하려면
모든 점들과의 거리를 계산해야함
근데 그 거리도 C값을 넘는 것 중에 최소인 것
N의 범위는 1~2000이라 N^2시간이 걸릴 수 있음
따로 방법이 없어 보임
모든 거리를 계산하고
sort한다음 k보다 큰 지점부터 연결하는 건?
sort하는건 시간초과 뜬다 -> heapq 우선순위 큐를 사용해서 해결
'''

import sys
import heapq

input = lambda : sys.stdin.readline().strip()

N, C = map(int, input().split())

arr = []

heap = []

def uclDist(pointA, pointB):
    return (pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2

def findP(x):
    if parent[x] != x :
        #경로 압축 : 시간 줄여줌
        parent[x] = findP(parent[x])
        return parent[x]
    else :
        return x



for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.append(i)
    arr.append(tmp)

parent = [i for i in range(N)]

for i in range(N):
    for j in range(i+1, N):
        dist = uclDist(arr[i], arr[j])
        if dist >= C :
            heapq.heappush(heap, [dist, arr[i], arr[j]])

cost = 0
v = 0

while heap:
    nodeInfo = heapq.heappop(heap)
    aP = findP(nodeInfo[1][2])
    bP = findP(nodeInfo[2][2])
    if aP != bP :
        cost += nodeInfo[0]
        parent[bP] = aP
        v += 1
    
    #가지치기 안하니까 시간초과 뜸
    if v == N-1 :
        break

if v != N-1 :
    print(-1)
else :
    print(cost)
    
    


