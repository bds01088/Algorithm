
def findp(node):
    global s
    #마지막 노드 번호를 받아오되
    #마지막노드를 제외한 그 위의 부모 및 조상들의 값을 받아와야하므로
    #현재 노드의 부모 값이 있는지 확인하고
    #있으면 부모val을 가지고, findp에 부모idx를 node로 넣어준다
    parent = tree[node][3]
    if parent :
        s += tree[parent][0]
        findp(parent)

tc = int(input())

for t in range(tc):
    n = int(input())
    #val, 좌, 우, 부모
    tree = [[0,0,0,0] for _ in range(n+1)]
    arr = list(map(int, input().split()))
    for i in range(1, n+1):
        tree[i][0] = arr[i-1]
        if i*2 <= 6 :
            tree[i][1] = i*2
        if i*2+1 <= 6 :
            tree[i][2] = i*2+1
        tree[i][3] = i//2
    #print(tree)

    #첫노드부터 차례차례 비교하자
    for i in range(1,n+1):
        j = i
        #부모val이 자식val보다 클동안
        while tree[j][0] < tree[tree[j][3]][0] and tree[j][3] != 0:
            tree[j][0], tree[tree[j][3]][0] = tree[tree[j][3]][0], tree[j][0]
            j = tree[j][3]
    print(tree)

    s = 0
    findp(n)
    print(f'#{t+1} {s}')
