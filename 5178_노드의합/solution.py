'''
노드의 개수와 리프노드의 개수가 주어지고
리프노드들의 합을 부모노드의 값으로 가지게 한다
노드L의 값을 출력하라
'''
def findchild(l):
    global s
    if l <= n :
        s += tree[l][0]
        findchild(l*2)
        findchild(l*2+1)

tc = int(input())

for t in range(tc):
    n, m, l = map(int, input().split())
    #val, 좌, 우, 부모
    tree = [[0,0,0,0] for _ in range(n+1)]
    #leaf node 받기
    for i in range(m):
        node, val = map(int, input().split())
        tree[node][0] = val
    '''
        #재귀로 풀면 필요없음
        #tree[node][3] = node//2


    last = n
    #목표 노드까지만 합을 구하면 됌
    while last >= l :
        tree[tree[last][3]][0] += tree[last][0]
        if tree[tree[last][3]][1] == 0 and last%2 == 0:
            tree[tree[last][3]][1] = last
        else :
            tree[tree[last][3]][2] = last
        tree[tree[last][3]][3] = tree[last][3]//2

        last -= 1
    print(tree)
    print(tree[l][0])
    
    #가지치기가 잘 안됌
    #부모노드를 타겟으로 노드의 개수보다 클때까지 자식노드를 탐색해나가면?
    #총 노드가 15개이고
    #4번노드를 찾는다면, 4*2, 4*2+1노드를 자식으로 가짐
    #4*2*2, 4*2*2+1, (4*2+1)*2,(4*2+1)*2+1 를 또 자식으로 가지고
    '''
    # 재귀로 풀기
    s = 0
    findchild(l)
    print(f'#{t + 1} {s}')
