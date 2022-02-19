'''
다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.

    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
ex )
5
1 1 3 1 2
ans = 5
최대값을 구하고
최대값 이전까지 구매하면 cnt+1하고 바로 최대값과의 차이를 sum에 더해준다
시간이 지난 곳들은 0으로 초기화시켜주고
최대값의 인덱스가 현재 인덱스와 같다면 0으로 초기화하고 최대값 다시찾기
'''

import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    n = int(input())
    price_list = list(map(int, input().split()))
    max_idx = price_list.index(max(price_list))
    sum = 0
    for idx, p in enumerate(price_list) :
        if idx < max_idx and p < price_list[max_idx]:
            sum += price_list[max_idx]-p
            price_list[idx] = 0
        elif idx == max_idx :
            price_list[idx] = 0
            #새로운 최대값 구하기
            max_idx = price_list.index(max(price_list))

    print(f'#{t+1} {sum}')
