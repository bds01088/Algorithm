
def in_order(node):
    global val
    if node :
        #중위순회를 이용해서
        #val의 첫값은 1인데
        #가장 왼쪽 아래에 1값이 들어가야하는걸 만족시켜줌
        in_order(tree[node][1])
        #왼쪽자식 탐색 후 돌아온 뒤에
        tree[node][0] = val
        #val값을 입력해주고, val을 1추가해준다
        val += 1
        #그래야만 오른쪽자식을 탐색하러 갔을때 3이 되기 때문
        in_order(tree[node][2])

tc = int(input())

for t in range(tc):
    n = int(input())
    #값, 좌, 우, 부모
    tree = [[0,0,0,0] for _ in range(n+1)]
    #tree에 1부터 n의 노드까지 정보 기입
    for i in range(1, n+1):
        #주어진 노드의 범위를 벗어났는지 확인하기
        #왼쪽 자식
        if i*2 <= n :
            tree[i][1] = i*2
            tree[i*2][3] = i
        #오른쪽 자식
        if i*2+1 <= n:
            tree[i][2] = i*2+1
            tree[i*2+1][3] = i
    val = 1
    in_order(1)
    print(f'#{t+1} {tree[1][0]} {tree[n//2][0]}')
