'''
방향없는 그래프가 주어질때
연결요소의 개수를 출력하라
즉
연결된 뭉치가 몇개인지 출력하는듯

유니온파인드 문제
'''

def findp(x):
    while x != parent[x]:
        x = parent[x]
    return x

#정점은 1부터 시작
#정점의 개수n
#간선의 개수m
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    if parent[findp(node1)] < parent[findp(node2)] :
        #중요
        #밑에서 전체 순환하면서 최종자기부모를 리뉴얼 시켜줌
        #그러므로 각 최종 부모끼리의 값들을 지정해놓아주어야
        #나중에 최종 리뉴얼이 제대로 됌
        parent[findp(node2)] = findp(node1)
    else :
        parent[findp(node1)] = findp(node2)

for i in range(1,n+1):
    parent[i] = findp(i)

print(len(set(parent))-1)