'''
위에서 바라보았을때의 색종이 면적을 구하라
색종이가 입력된 순으로
그 색종이가 얼마만큼의 면적을 표시하고 있는지
입력된 순서대로 출력하라

색종이 개수가 주어지고
색종이의 왼쪽하단 좌표 x, y와 가로 세로 길이가 주어진다
'''

# import sys
# sys.stdin = open('input.txt')

n = int(input())
board = [[0]*1001 for _ in range(1001)]
for num in range(1, n+1):
    col, row, w, h = map(int, input().split())
    for i in range(row, row+h):
        for j in range(col, col+w):
            board[i][j] = num
count = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        count[board[i][j]] += 1

for i in range(1,n+1):
    print(count[i])



