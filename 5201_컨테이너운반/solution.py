'''
n개의 컨테이너를
m대의 트럭으로 운반하자
트럭당 한개의 컨테이너만 운반 가능하고
초과적재 불가능하다
편도로 한번만 운행할때
가능한 중량이 최대가 되도록 한다면 중량이 얼만지 출력하라
한개도 못옮길 경우 0을 출력한다

n, m이 주어지고
컨테이너 무게
트럭 적재가능량이 주어진다
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    container_weight = sorted(list(map(int, input().split())), reverse=True)
    truck_weight = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    # print(container_weight)
    # print(truck_weight)
    visit = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if container_weight[i] <= truck_weight[j] and visit[j] == 0:
                ans += container_weight[i]
                visit[j] = 1
                break
    print(f'#{t+1} {ans}')
