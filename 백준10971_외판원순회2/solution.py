'''
n개의 도시가 주어진다
각 도시의 간선 정보가 n*n배열로 주어진다
연결이 안된곳은 0으로 표시되고
모든 도시를 방문하여 마지막에 출발한 도시로 돌아와야한다
항상 순회할 수 있는 경우만 주어진다
i -> j 랑 j -> i 랑 값이 다를 수도 있다
출발점은 정해져있지않다
가장 작은 비용을 출력하자

for문으로 n번반복하면서 시작도시를 n까지 바꾸면서 변경하고
ans를 따로 정해서
그것보다 비용이 커지면 백트래킹하도록

'''
import sys
sys.stdin = open('input.txt')

def DFS(startnode, cost):
    global ans, visit, i
    visit[startnode] = 1
    if cost >= ans :
        return
    if sum(visit) == n:
        if board[startnode][i] != 0 :
            if cost + board[startnode][i] < ans:
                ans = cost + board[startnode][i]
            else :
                return
        else :
            return

    for j in range(n):
        if board[startnode][j] != 0 and visit[j] == 0:
            visit[j] = 1
            DFS(j, cost+board[startnode][j])
            visit[j] = 0



n = int(input())

board = []
for i in range(n):
    board.append(list(map(int ,input().split())))

ans = 10000000

for i in range(n):
    visit = [0 for _ in range(n)]
    DFS(i, 0)

print(ans)