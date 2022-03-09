'''
인터넷에 퍼져있는 DP풀이 방법

이동은 오른쪽 또는 아래 밖에 못하기 때문에
해당 좌표의 값은 왼쪽과 위쪽에서 오는 길의 개수를 더해주면 해당 좌표로 올 수 있는 길의 개수가 나타난다
고로 첫행과 첫열은 0으로 넣어주고
1,1을 1로 잡아준다음
길의 개수를 표시하는 2차원 리스트를 만든다

코드
n, m, k = map(int, input().split())
dp = [[0] * (m + 1) for i in range(n + 1)]
dp[0][1], cnt = 1, 1 #dp[0][1] 위치를 1로 해주어 dp[1][1]에서 왼쪽 위쪽을 더할때 1이 더해지고 초기값을 가지도록 함
for i in range(1, n + 1):
    for j in range(1, m + 1):
        #문제에서 2차원리스트의 좌표위치에는 이전 좌표들의 개수를 값으로 가지기 때문에
        #동그라미로 표시된 값의 위치 찾기
        if cnt == k:
            px = i
            py = j
        cnt += 1
        #왼쪽 위쪽 값 더해서 지금 좌표에 더하기
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
if k == 0:
    print(dp[n][m])
else:
    print(dp[px][py] * dp[n - px + 1][m - py + 1])
'''

'''
n*m배열에 1부터 n*m까지의 번호들로 가득찬다
n m k가 주어지며
k가 0일때는 없다는 거고
k가 1이상 n*m이하의 수 일 경우
k숫자를 가진 좌표를 꼭 지나쳐서 n*m위치에 도달해야한다

해결방법
0,0인 1에서 출발해서
?,?인 k위치까지의 DFS로 찾은 길 개수와
?,? k위치에서 n,m인 n*m까지의 DFS 길 개수와
곱해주면 된다
'''

def DFS(start_row, start_col, end_row, end_col):
    #오른쪽, 아래밖에 못가므로 visited는 굳이 안만들어도 될 듯 하다
    #visited=[]
    #우, 하
    dr = [0,1]
    dc = [1,0]
    stack = []
    stack.append([start_row,start_col])
    cnt = 0
    while stack :
        #좌표를 받음
        xy = stack.pop()
        #우 하 순서로 검색
        for i in range(2):
            #탐색 좌표 기입
            row = xy[0] + dr[i]
            col = xy[1] + dc[i]
            #탐색 좌표가 범위 내에 있다면
            if (row <= end_row) and (col <= end_col) :
                #탐색좌표가 마지막 지점과 같다면
                if (row == end_row) and (col == end_col) :
                    #경로 개수 증가
                    cnt += 1
                    break
                else :
                    stack.append([row,col])
    return cnt


n, m, k = map(int, input().split())

#꼭 지나가야할 좌표(타겟)가 없을 경우 마지막 점을 목표로 바꿔준다
if k == 0 :
    k = n*m

trow = 0
tcol = 0

board = []
num = 1
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(num)
        #타겟 좌표 저장
        if num == k :
            trow = i
            tcol = j
        num += 1
    board.append(temp)

#타겟 좌표가 없을 경우
#그냥 첫지점부터 마지막 지점까지 DFS 돌리기
if k == n*m :
    result = DFS(0, 0, n-1, m-1)
    
#타겟 좌표가 있을 경우
#첫 지점부터 타겟까지 DFS * 타겟부터 마지막 지점까지 DFS
else :
    s_to_t = DFS(0, 0, trow, tcol)
    t_to_e = DFS(trow, tcol, n-1, m-1)
    result = s_to_t*t_to_e

print(result)