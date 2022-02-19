'''
문제
다음 100X100의 2차원 배열이 주어질 때
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라

입력
10개의 테스트 케이스
케이스넘버
공백을 간격으로 정수가 들어옴

출력
#케이스넘버 결과값
'''

import sys
sys.stdin = open('input.txt')

def matrix_max(arr) :
    cross1 = []
    cross2 = []
    max = 0
    for i in range(100) :
        xmax = 0
        ymax = 0
        for j in range(100) :
            xmax += arr[i][j]
            ymax += arr[j][i]
            #대각선은 1개씩밖에없으니까 1번만 구한다
            #좌상우하 대각선
            if i == j :
                cross1.append(arr[i][j])
            #좌하우상 대각선
            if i+j == 99 :
                cross2.append((arr[i][j]))
        #x축y축 두개 동시에 비교해도 결국 최대값만 찾는 것이기 때문에 상관없다
        if xmax > max :
            max = xmax
        if ymax > max :
            max = ymax

    if sum(cross1) > max :
        max = sum(cross1)

    if sum(cross2) > max :
        max = sum(cross2)
    return max


for _ in range(10) :
    tn = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = matrix_max(arr)
    print(f'#{tn} {result}')