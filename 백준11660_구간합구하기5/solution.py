'''
n, m이 주어진 다음
n*n배열이 주어지고
m개의 좌표값 x1, y1, x2, y2가 주어진다
좌상단 x1,y1좌표에서 우하단 x2,y2까지의 사각형의 합을 구하라

미완성, DP 이용하기로 하자
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for num in range(m):
    s = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            s += board[i][j]
    print(s)

