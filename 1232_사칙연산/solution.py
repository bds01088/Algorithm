import sys
sys.stdin = open('input.txt')

def treeCal(node):
    #만약 해당 노드의 val이 연산자면
    if tree[node][0] in opers :
        #자식노드들이 있을거고, 그 위치를 값으로 받아온다
        a = treeCal(tree[node][1])
        b = treeCal(tree[node][2])
        if tree[node][0] == '+' :
            tree[node][0] = a + b
        elif tree[node][0] == '-' :
            tree[node][0] = a - b
        elif tree[node][0] == '*' :
            tree[node][0] = a * b
        elif tree[node][0] == '/' :
            tree[node][0] = a / b
        #자식들로부터 두개의 값을 가져와서 계산한뒤
        #결과값을 해당 노드의 val값에 넣어준다
        return tree[node][0]

    #val값이 연산자가 아닐경우 값이므로 리턴해준다
    else :
        return tree[node][0]


opers = ['+','-','/','*']

for t in range(1, 11):
    n = int(input())
    #val, 좌, 우, 부모
    tree = [[0,0,0,0] for _ in range(n+1)]
    for i in range(1, n+1):
        #node, val, child1, child2
        arr = list(input().split())
        #길이를 4로 맞추기위해 0을 추가로 넣어줌
        while len(arr) < 4 :
            arr.append(0)
        #val 위치에 연산자가 들어오면 그대로 넣어주고
        if arr[1] in opers :
            tree[i][0] = arr[1]
        #아닐경우 정수로 변환
        else :
            tree[i][0] = int(arr[1])
        #나머지 자식위치들의 정보도 다 정수로 변환
        tree[i][1] = int(arr[2])
        tree[i][2] = int(arr[3])
        #leaf node에는 tree[0][3]에 i를 입력하게 될거같은데 tree[0]은 사용안하니 상관없을듯?
        tree[int(arr[2])][3] = i
        tree[int(arr[3])][3] = i
    #print(tree)
    result = treeCal(1)
    print(f'#{t} {int(result)}')

