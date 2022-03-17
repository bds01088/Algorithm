'''
노드n을 루트로 하는 서브트리에 속하는 노드의 개수를 출력하라
'''

def count_node(node):
    global cnt
    if node :
        cnt += 1
        count_node(tree[node][0])
        count_node(tree[node][1])

tc = int(input())
for t in range(tc):
    E, n = map(int, input().split())
    #왼, 오, 부모
    tree = [[0,0,0] for _ in range(E+2)] #간선의 개수=E, 노드의개수=간선+1
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(E):
        parent, child = arr[i*2], arr[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else :
            tree[parent][1] = child
        tree[child][2] = parent

    count_node(n)
    print(f'#{t+1} {cnt}')