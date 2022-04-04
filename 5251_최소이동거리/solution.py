'''
시작지점에서 끝지점까지 가는데 최소 비용을 구하자

'''

import sys
sys.stdin = open('input.txt')

def Dijkstra(start, n, arr, distancefromstart):
    U = [start]
    V = list(range(0,n+1))

    for i in range(n+1) :
        #연결되어있다면 0이 아니라 거리값이 들어 있을 것
        if arr[start][i] != 0 :
            #distance에는 0을 제외한 모든값이 999로 지정되어있으니까
            #0과 연결된 곳은 거리값을 넣어주는 것
            distancefromstart[i] = arr[start][i]

    #0에서 출발한 리스트가 모든 노드를 방문할 때까지
    while set(U) != set(V) :
        mmin = 99999
        min_idx = -1
        #전체 노드 중에서 이미 방문했던 노드들을 제외한 노드들 중에서
        #가장 적은 거리값을 가지고 있는 idx를 뽑아서 방문하도록 해야한다
        #연결되어있지 않는 곳은 999값으로 되어서 선택 불가능하도록 만들었다
        for idx in list(set(V)-set(U)):
            if mmin > distancefromstart[idx] :
                mmin = distancefromstart[idx]
                min_idx = idx

        #거리값이 가장 작고 U에 포함되지 않은 노드의 번호를 추가해준다
        #노드의 번호가 곧 인덱스이다
        U.append(min_idx)

        #연결정보를 나타내는 arr배열에서
        #추가된 min_idx의 노드와 연결된 노드들의 거리값들을 찾아와야한다
        #다만 U에 포함된 노드들과의 접점이 있어 거리값이 초기값(99999)가 아닌 곳들도 있다
        #0에서 1과 2를 갈 수 있고, 1에서 2를 갈 수 있는데
        #0에서 거리값이 1로 이동할때 더 작아서 1이 들어온 것이다
        #0에서 2까지의 거리값이 8이라면
        #0에서 1까지 온 거리값 + 1에서 2까지의 거리값이 7이면
        #교체를 해주겠지만 9라면 기존의 거리값인 8을 유지시켜주어야한다
        #기존값과 추가된 min_idx에서 해당 노드로 갈때의 거리값과 비교하여 작은걸 저장해야한다
        for i in range(n+1):
            if arr[min_idx][i] != 0 :
                distancefromstart[i] = min(distancefromstart[i], distancefromstart[min_idx] + arr[min_idx][i])
    return distancefromstart[n]

tc = int(input())

for t in range(tc):
    #n : 마지막 연결지점 번호
    #v : 도로의 개수
    n, v = map(int, input().split())

    arr = [[0]*(n+1) for _ in range(n+1)]

    for i in range(v):
        start, end, weight = map(int, input().split())
        arr[start][end] = weight

    distancefromstart = [99999 for _ in range(n+1)]
    distancefromstart[0] = 0

    print(f'#{t+1} {Dijkstra(0, n, arr, distancefromstart)}')
