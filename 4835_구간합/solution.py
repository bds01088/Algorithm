'''
문제
n개의 정수가 들어있는 배열에서
이웃한 m개의 합을 구해서
m개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 구하라

입력
테스트케이스 개수
정수의개수 이웃합의넓이
n개의 정수들

출력
#테스트케이스 결과값

해결방법
for문으로 0부터 돌리되 m을 추가한 길이만큼 다 더한 값을
새로운 리스트에 저장하는 걸로 하자
주의할 점으로 끝부분에는 인덱스 에러가 나지 않도록 하자
n-m인덱스를 가지도록 하면 될 듯 하다
'''

import sys
sys.stdin = open('input.txt')

def multi_sum(n, m, li) :
    #max min 구하기가 애매해서 정렬후 제일 앞쪽과 뒤쪽을 빼주는 것으로 하자
    sum_list = []
    for i in range(n-m+1) :
        sum = 0
        for j in range(i, i+m) :
            sum += li[j]
        sum_list.append(sum)

    #합계 리스트를 버블정렬하자
    for i in range(len(sum_list), 0, -1) :
        for j in range(0, i-1) :
            if sum_list[j] > sum_list[j+1] :
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]
    return sum_list[-1]-sum_list[0]

tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    result = multi_sum(n, m, li)
    print(f'#{t+1} {result}')