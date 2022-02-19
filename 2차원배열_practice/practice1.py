'''
5X5 2차원 배열에 무작위 25개의 숫자로 초기화 후
각 요소에 대해 이웃한 4방위 요소와 차이의 절대값의 합을 구하시오
벽에 있는 요소는 이웃 요소가 없을 수도 있으니 유의
'''
import sys
sys.stdin = open('practice1_input.txt')

tc = int(input())
for t in range(1, tc+1) :
    s = int(input())
    m = [list(map(int, input().split())) for _ in range(s)]
    di = [0, 0, -1, +1] #상하
    dj = [-1, 1, 0, 0] #좌우
    total_sum = 0
    for i in range(s) :
        for j in range(s) :
            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]
                if 0 <= ni < s and 0 <= nj < s :
                    total_sum += abs(m[i][j]-m[ni][nj])
    print(f'#{t} {total_sum}')