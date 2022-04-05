'''
n, m이 들어오고
1부터 n까지의 사람들이있다
2개씩 끊어서 신청서를 받아
사람들의 조 연결을 그리자
1~n까지 중 나타나지 않은 사람은 혼자 조를 만드는거임
'''

import sys

sys.stdin = open('input.txt')

def findset(x):
    while p[x] != x :
        x = p[x]
    return x

def union(x,y):
    #크기가 작은것을 루트로 해주어야함
    #잘못하면 사이클이 발생할 수 있음
    X = findset(x)
    Y = findset(y)
    if X < Y:
        p[Y] = X
    else :
        p[X] = Y


tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    arr = p = list(range(n+1))

    for i in range(m):
        union(temp[2*i], temp[2*i+1])

    head = []
    for i in range(1,n+1):
        head.append(findset(i))

    print(f'#{t + 1} {len(set(head))}')

#################################################
#시간초과뜸 왜?
    # for i in range(m):
    #     # 3이 1을 부모로 가지고있는데
    #     # 3이 2도 부모로 가지려고 하면 덮어씌워져서
    #     # 원래는 하나의 조가 되어야하는데 이상하게 바뀐다
    #     #그러므로 3이 3을 가리키는게 아니라면
    #     #합쳐줘야됌
    #     #예시) 1, 2, 3, 2이면
    #     #1 - 2
    #     #3 - 2
    #     if arr[temp[i*2+1]] == temp[i*2+1] :
    #         arr[temp[i*2+1]] = temp[i*2]
    #     else :
    #         #이미 부모를 가지고 있다면
    #         #부모를 찾아서 그 부모와 연결시키기
    #         x = temp[i*2+1]
    #         while arr[x] != x:
    #             x = arr[x]
    #         arr[x] = temp[i*2]
    #
    # head = []
    # for i in range(1,n+1):
    #     j = i
    #     while j != arr[j] :
    #         j = arr[j]
    #     if j not in head :
    #         head.append(j)
    #
    # print(f'#{t+1} {len(head)}')

