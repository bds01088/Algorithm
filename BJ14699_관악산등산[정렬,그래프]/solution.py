import sys

input = lambda : sys.stdin.readline().strip()
        
'''
똑같은 높이는 없다.
고로 맨 위 정상부터 계산하면 정상은 자기 자신밖에 못들리니까 1
그 정상과 연결된 하위 휴식터는 연결된 정상들 중 최대값을 가진 것에 +1 한 값이 최대값
'''
N, M = map(int, input().split())

height = list(map(int, input().split()))

node_list = []
for i in range(N):
    node_list.append((i, height[i]))
node_list.sort(key=lambda x: (x[1]), reverse=True)


ans_list = [0 for _ in range(N)]

board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if height[a] < height[b] :
        board[a][b] = 1
    elif height[a] > height[b] :
        board[b][a] = 1


for i in range(N):
    for j in range(N):
        if board[node_list[i][0]][j] == 1 :
            if ans_list[node_list[i][0]] < ans_list[j]+1 :
                ans_list[node_list[i][0]] = ans_list[j]+1
    if ans_list[node_list[i][0]] == 0 :
        ans_list[node_list[i][0]] = 1

for i in range(N):
    print(ans_list[i])
