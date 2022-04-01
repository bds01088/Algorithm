'''
직원 번호는 1~n
작업 번호도 1~n
i번직원이 j번 작업을 하면 성공할 확률이 p(i,j)다
주어진 일이 모두 성공할 확률의 최대값을 구하자
'''

import sys
sys.stdin = open("input.txt")

def DFS(job_num, success_percent):
    global ans, visit
    #곱해지면 곱해질수록 작아진다
    #소수점값이기 때문에
    #1보다 커야 곱할수록 커지기 때문
    if success_percent < ans :
        return
    if job_num == n :
        if success_percent > ans :
            ans = success_percent
        return
    else :
        for i in range(n):
            if visit[i] == 0 :
                visit[i] = 1
                DFS(job_num+1, success_percent*board[job_num][i])
                visit[i] = 0


tc = int(input())

for t in range(tc):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(lambda x:float(x)/100, input().split())))

    ans = 0.000000000000001
    visit = [0 for _ in range(n)]
    DFS(0,1)
    print(f'#{t+1} {ans*100:.6f}')