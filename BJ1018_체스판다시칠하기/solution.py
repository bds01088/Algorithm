def find2(srow, scol) :
    global ans
    cnt = 1
    for i in range(srow, srow+8):
        before = board[i][scol]
        if i != srow :
            if firstbefore == board[i][scol] :
                cnt += 1
                if board[i][scol] == "B":
                    before = "W"
                    firstbefore = "W"
                else :
                    before = "B"
                    firstbefore = "B"
                if cnt > ans :
                    return
            else :
                firstbefore = board[i][scol]
        else :
            if board[i][scol] == "B":
               firstbefore = "W"
               before = "W"
            else :
                before = "B"
                firstbefore = "B"




        for j in range(scol+1, scol+8):
            if before == board[i][j] :
                cnt += 1
                if before == "B":
                    before = "W"
                else :
                    before = "B"
                if cnt > ans :
                    return
            else :
                before = board[i][j]
        if cnt > ans :
            return
    ans = cnt


def find1(srow, scol) :
    global ans
    cnt = 0
    firstbefore = board[srow][scol]
    for i in range(srow, srow+8):
        before = board[i][scol]
        if i != srow :
            if firstbefore == board[i][scol] :
                cnt += 1
                if board[i][scol] == "B":
                    before = "W"
                    firstbefore = "W"
                else :
                    before = "B"
                    firstbefore = "B"
                if cnt > ans :
                    return
            else :
                firstbefore = board[i][scol]
        for j in range(scol+1, scol+8):
            if before == board[i][j] :
                cnt += 1
                if before == "B":
                    before = "W"
                else :
                    before = "B"
                if cnt > ans :
                    return
            else :
                before = board[i][j]
        if cnt > ans :
            return
    ans = cnt
        



n, m = map(int, input().split())

board = []
ans = 99999999

for i in range(n):
    board.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        find1(i, j)
        find2(i, j)

print(ans)