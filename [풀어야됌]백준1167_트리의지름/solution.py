'''
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
트리의 지름을 출력하자

노드의 개수 n이 주어지고
노드는 1부터 n개까지 있다

각 노드 번호
연결된 노드 번호 노드까지의 거리가 주어지며, -1이 들어올때까지 반복한다
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

연결 상태 배열을 하나 만들고
1부터 n까지 가는 길
완전탐색해야할듯
'''

def DFS(start, visit, s) :
    global ans, board
    for i in range(1, v+1):
        if board[start][i] != 0 and visit[i] == 0:
            visit[i] = 1
            DFS(i, visit, s+board[start][i])
            visit[i] = 0

    if s > ans :
        ans = s


v = int(input())

board = [[0]*(v+1) for _ in range(v+1)]
visit = [0 for _ in range(v+1)]
ans = 0

for i in range(1, v+1):
    temp = list(map(int, input().split()))
    l = len(temp)
    #l이 4면 1개, 6이면 2개 8이면 3개
    for node in range(1, l-1, 2):
        board[temp[0]][temp[node]] = temp[node+1]

#그냥 시작 노드에서
#연결 할 수 있는 지점 넣고 빼고 해서
#모든 가능성을 다 찾아보자
#visit된 곳 밖에 선택지가 없는 노드에 도착하면
#끝내고 그 중간에 거쳐갔던 노드들은 적어도 끝난노드까지 가는 길이보다는 적을거니까

###############################
##트리로 주어져서 트리특성을 이용해야하는듯
##메모리 초과가 뜬다..
#트리구조니까 정점노드를 찾아서
#정점노드에서 갈 수 있는 가장 먼 노드 2개를 찾아서 더하면 되지않나?
###############################

for i in range(1, v+1):
    visit[i]=1
    DFS(i, visit, 0)
    visit[i] = 0

print(ans)