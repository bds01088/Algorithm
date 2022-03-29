'''
0시부터 다음날 0시 이전까지 최대한 많은 화물을 싣고 내리도록 하면
화물차가 몇대가 이용하는지 출력
5시에 끝나면 5시부터 시작가능

정렬된 리스트에서
맨 앞의 값에서
시작과 끝 시간 숫자 사이의 수를 시작시간으로 가지고 있는 것을 보고
그것들 중 끝 시간이 가장 작고, 맨 앞의 값의 끝 시간보다 일찍 끝나면
그걸 선택하자
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(tc):
    n = int(input())
    time_table = []
    for i in range(n):
        time_table.append(list(map(int, input().split())))
    #끝나는 시간, 시작 시간 순으로 정리
    time_table.sort(key=lambda x:[x[1], x[0]])
    #print(time_table)
    user = [time_table[0]]

    for i in range(1, n):
        #끝나는 시간, 시작 시간 순으로 정리하였기 때문에
        #이전 끝나는 시간보다 시작 시간이 큰 것들 중에
        #끝나는 시간이 가장 작은 값이 먼저 오기 때문에
        #그냥 바로 추가해주면 된다
        if user[-1][1] <= time_table[i][0] :
            user.append(time_table[i])
    print(f'#{t+1} {len(user)}')


    '''
    시간초과뜸
    user = []
    i = 0
    while i < n :
        temp = time_table[i]
        p = i
        for j in range(i+1, n):
            if time_table[i][1] <= time_table[j][1] :
                break
            elif time_table[i][0] <= time_table[j][0] and time_table[i][1] > time_table[j][1] :
                if temp[1] > time_table[j][1] :
                    temp = time_table[j]
                    p = j
        i = p
        user.append(temp)

        if i == n-1 :
            break

        #다음 화물차 시간 찾기
        for j in range(i+1, n):
            if time_table[i][1] <= time_table[j][0] :
                i = j
                break
    print(f'#{t+1} {len(user)}')
    '''
