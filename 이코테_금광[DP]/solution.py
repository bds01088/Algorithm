t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    board = []
    for i in range(n):
        tmp = arr[i*m:i*m+m]
        board.append(tmp)
    
    for i in range(1, m):
        for j in range(n):
            if j == 0 :
                board[j][i] = max(board[j][i]+board[j][i-1], board[j][i]+board[j+1][i-1])
            elif j == n-1 :
                board[j][i] = max(board[j][i]+board[j][i-1], board[j][i]+board[j-1][i-1])
            else :
                board[j][i] = max(board[j][i]+board[j][i-1], board[j][i]+board[j-1][i-1], board[j][i]+board[j+1][i-1])

    mmax = 0
    for i in range(n):
        if board[i][-1] > mmax :
            mmax = board[i][-1]
    print(mmax)