import sys
sys.stdin = open('input.txt')

def BFS(start_i, start_j):
    q = []
    room = []

    q.append([start_i, start_j])
    #visit이 0인것만 BFS시작되기때문에
    visit[start_i][start_j] = 1
    #시작부분이건 중간부분이건 끝부분이건 다 방의 일부분이기 때문에 추가해줌
    room.append(board[start_i][start_j])

    while q :
        now_i, now_j = q.pop(0)
        for x, y in direction:
            next_i = now_i+x
            next_j = now_j+y
            #다음 좌표와 차이가 정확히 1만 나야지 방이 연결되기 때문에
            if 0 <= next_i < n and 0 <= next_j < n and visit[next_i][next_j] == 0 and \
                abs(board[now_i][now_j]-board[next_i][next_j]) == 1:
                #abs를 통해 확인하고
                q.append([next_i,next_j])
                room.append(board[next_i][next_j])
                #룸의 길이는 len으로 구하기때문에 visit에는 그냥 1을 넣어 방문 여부만 파악
                visit[next_i][next_j] = 1
    return min(room), len(room)


direction = [[-1,0],[1,0],[0,-1],[0,1]]
tc = int(input())
for t in range(tc):
    n = int(input())
    board = [[0]*n for _ in range(n)]

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            board[i][j] = temp[j]

    start = n*n
    size = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 :
                temp_start, temp_size = BFS(i, j)
                if temp_size > size or temp_size == size and temp_start < start :
                    size = temp_size
                    start = temp_start
    print(f'#{t+1} {start} {size}')