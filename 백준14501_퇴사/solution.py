'''
n이 주어지고
1일부터 n일까지 일하고
n+1에 퇴사한다
각 일별로
t, p값이 주어지는데
t는 걸리는 일 수
p는 가격이다
최대가격을 구하자

DFS해서 완전탐색 해야할듯
일할때 안할때 이렇게 구분해서
하도록 하자
'''

import sys
sys.stdin = open('input.txt')

def DFS(days, s):
    global ans

    if days == n :
        if ans < s:
            ans = s
        return

    else :
        if days+arr[days][0] <= n :
            DFS(days+arr[days][0], s+arr[days][1])
            DFS(days + 1, s)
        #다음위치가 n을 넘어간다면
        else :
            #마지막 위치면
            if days == n-1 :
                if ans < s:
                    ans = s
                return
            #마지막 위치가 아니면
            else :
                DFS(days+1, s)
tc = int(input())
for t in range(tc):
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    ans = 0
    DFS(0, 0)

    print(ans)