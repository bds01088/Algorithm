'''
2진수와 3진수가 주어지고
각각 한자리가 틀려있다
두 진수를 한자리씩 바꾸어
표현한 값이 같을 경우를 찾아야한다

브루트 포스로
이진수의 리스트의 값들을 조정한 뒤 10진수로 변경한 것을 리스트로 저장하고
삼진수의 리스트의 값들을 조정한 뒤 10진수로 변경한 것을 리스트로 저장하면
같은 값이 떴을때를 파악할 수 있을 것이다

1
1010
212

#1 14
'''

tc = int(input())

for t in range(tc):
    bb = list(input())
    tt = list(input())

    b_list = []
    t_list = []
    for i in range(len(bb)):
        temp = bb[:]
        ten = ''
        if temp[i] == '0':
            temp[i] = '1'
            for j in temp:
                ten += j
        else :
            temp[i] = '0'
            for j in temp:
                ten += j
        b_list.append(int(ten,base=2))

    for i in range(len(tt)):
        for j in range(3):
            temp = tt[:]
            if temp[i] == '0' :
                temp[i] = '1'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))
                temp[i] = '2'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))
            elif temp[i] == '1' :
                temp[i] = '2'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))
                temp[i] = '0'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))
            else :
                temp[i] = '0'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))
                temp[i] = '1'
                ten = ''
                for p in temp :
                    ten += p
                t_list.append(int(ten,base=3))

    # print(b_list)
    # print(t_list)
    result = set(b_list)&set(t_list)

    print(f'#{t+1} ', end='')
    print(*result)