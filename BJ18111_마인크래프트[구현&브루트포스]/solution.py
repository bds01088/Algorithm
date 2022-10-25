'''
땅이 모두 같은 높이여야함
캐는데 2초
놓는데 1초 걸림
최소의 시간으로 모든 땅을 고르게 만들자

주어지는 땅에서
최소값과 최대값 사이의 높이를 모두 백트래킹?으로 돌려보자

멈추는 조건으로 기존 ans보다 커지거나,
해당 기준으로 인벤토리값+제거하는 블럭의 수가 채워야하는 블럭수보다 적을 경우
리턴하는걸로 하자
'''


import sys
input = sys.stdin.readline

def FindAns(height):
    global n, m, b, ans, ans_height
    t = 0
    extra = b
    need = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > height :
                t += (board[i][j]-height)*2
                extra += board[i][j]-height
            elif board[i][j] < height :
                t += height-board[i][j]
                need += height-board[i][j]
            if t > ans :
                return
    if extra < need :
        return

    if t < ans :
        ans = t
        ans_height = height
    elif t == ans :
        if ans_height < height :
            ans_height = height
    return


n, m, b = map(int, input().strip().split())

board = []

mmax = 0
mmin = 300

for i in range(n):
    tmp = list(map(int, input().strip().split()))
    board.append(tmp)
    if max(tmp) > mmax :
        mmax = max(tmp)
    if min(tmp) < mmin :
        mmin = min(tmp)
    

ans = 99999999999
ans_height = 0

for h in range(mmax, mmin-1, -1):
    FindAns(h)
# for h in range(256, -1, -1):
#     FindAns(h)
print(ans, ans_height)