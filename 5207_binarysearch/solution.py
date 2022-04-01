'''
서로다른 n개의 정수가 주어지면
정렬한 다음 리스트a에 저장한다
리스트b에 저장된 m개의 정수에 대해
a에 저장되어있는 수인지 이진탐색한다

이진탐색하는데 있어서
2번이상의 탐색을 하는데 있어서
한방향으로 연속2번 가야한다면 조건에 맞지않아서 답이 증가하지않는다
첫번째 오른쪽에 있고, 두번째 m일 경우 조건만족이다

'''

import sys
sys.stdin = open('input.txt')

def binsearch(x, left, right):
    global ans, LorR
    # if x not in a_list :
    #     return
    if LorR == [0,2] or LorR == [2,0] :
        return
    else :
        mid = (left+right)//2
        if a_list[mid] == x :
            ans += 1
        elif a_list[mid] > x :
            LorR[0] += 1
            LorR[1] = 0
            binsearch(x, left, mid-1)
        else :
            LorR[1] += 1
            LorR[0] = 0
            binsearch(x, mid+1, right)


tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    a_list = sorted(list(map(int ,input().split())))
    b_list = list(map(int, input().split()))

    ans = 0
    for x in b_list :
        if x in a_list :
            LorR = [0,0]
            binsearch(x, 0, len(a_list)-1)
    print(f'#{t+1} {ans}')
