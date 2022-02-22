'''
가로세로 길이가 10,20 / 20,20 인 종이가 있다
바닥에는 20,x가 주어지며 (x는 10의 배수)
바닥을 채우는 방법이 몇개 있는지 파악하라

입력
tc
x

해결방법

'''
import sys
sys.stdin = open("input.txt")

tc = int(input())

for t in range(tc):
    #10단위
    n = int(input())//10
    memo = [1,3]

    for i in range(2, n):
        # 점화식 그림 참고하자
        memo.append(memo[i-1] + memo[i-2]*2)
    print(f'#{t+1} {memo[-1]}')
