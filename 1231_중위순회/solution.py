import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node :
        inorder(arr[node][2])
        print(arr[node][1], end='')
        inorder(arr[node][3])


for t in range(1, 11):
    n = int(input())
    #노드번호, val, 좌, 우
    arr = [[0,0,0,0] for _ in range(n+1)]
    for i in range(1, n+1):
        str = input().split()
        #node, val, *next_node = input().split()
        #kwarg사용하면 가변입력 받을수있다
        while len(str) < 4 :
            str.append(0)
        for j in range(4):
            if j != 1 :
                arr[i][j] = int(str[j])
            else :
                arr[i][j] = str[j]

    print(f'#{t}', end=' ')
    inorder(1)
    print()
