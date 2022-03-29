'''
0~9까지의 카드 4세트를 섞어 사용한다
연속한 숫자 3개이상이면 run
같은 숫자 3개이상이면 triple
1p과 2p가 순서대로 한장씩 가져가는데
6장 채우기전에 메이드 되면 승자임
무승부일 경우 0을 출력
동시에 날 경우
1p가 이김
'''

import sys
sys.stdin = open('input.txt')

def made(x, list):
    # triple 검사
    if list[x] == 3:
        return 1
    # run 검사
    if 1 < x < 8:
        if (list[x - 2] >= 1 and list[x - 1] >= 1) \
                or (list[x - 1] >= 1 and list[x + 1] >= 1) \
                or (list[x + 1] >= 1 and list[x + 2] >= 1):
            return 1
    elif x == 2 or x == 8:
        if (list[x - 1] >= 1 and list[x + 1] >= 1) \
                or (list[x + 1] >= 1 and list[x + 2] >= 1):
            return 1

    elif x == 0:
        if list[x + 1] >= 1 and list[x + 2] >= 1:
            return 1
    else:
        if list[x - 2] >= 1 and list[x - 1] >= 1:
            return 1
    return 0

tc = int(input())

for t in range(tc):
    card_list = list(map(int, input().split()))
    p1_list = [0 for _ in range(10)]
    p2_list = [0 for _ in range(10)]
    p1_flag = 0
    p2_flag = 0

    for i in range(12):
        x = card_list[i]
        if i%2 == 0 :
            p1_list[x] += 1
            if sum(p1_list) >= 3:
                p1_flag = made(x, p1_list)
                if p1_flag == 1 :
                    break
        else :
            p2_list[x] += 1
            if sum(p2_list) >= 3:
                p2_flag = made(x, p2_list)
                if p2_flag == 1 :
                    break
    if p1_flag == 1 :
        print(f'#{t+1} 1')
    elif p2_flag == 1 :
        print(f'#{t + 1} 2')
    elif p1_flag == p2_flag :
        print(f'#{t + 1} 0')