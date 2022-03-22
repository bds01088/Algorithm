'''
화덕에는 한번에 들어갈 수 있는 개수 n이 주어지고
1부터 m번까지의 m개의 피자를 순서대로 화덕에 넣는다
치즈의 양이 주어지는데 화덕 한바퀴를 돌때 절반씩 줄어들고
0이된 피자는 빼낸다
가장 마지막에 남는 피자 번호를 출력하라

1번 위치에서만 피자를 넣거나 뺄 수 있다.

'''
import sys
sys.stdin = open('input.txt')

def last_pizza_battalion(n, pizza) :
    q = [0]*n
    pizza_num = [-1]*n
    cnt = 0
    pizza_idx = 0

    while pizza_idx < len(pizza) :
        if q[cnt%n] == 0 :
            pizza_num[cnt%n] = pizza_idx
            cheeze = pizza[pizza_idx]
            pizza_idx += 1
            q[cnt%n] = cheeze
            cnt += 1
        else :
            q[cnt%n] = q[cnt%n]//2
            if q[cnt % n] == 0:
                pizza_num[cnt % n] = pizza_idx
                cheeze = pizza[pizza_idx]
                pizza_idx += 1
                q[cnt % n] = cheeze
            cnt += 1
    #마지막 피자를 화덕에 넣은 다음
    #피자가 다 구워질때까지 돌려주자
    #최종피자의 인덱스 값을 저장하기 위한 last_pizza
    last_pizza = 0
    #q가 0으로 가득찬다면 피자가 다 구워진것
    while q != [0]*n:
        #위쪽에서 마지막피자를 넣고 cnt를 1증가시킨 후 종료되었기 때문에
        #바로 현재 cnt%n위치를 검사하면된다
        #피자가 있다면
        if q[cnt%n] != 0 :
            #한바퀴 돌고 도착한 피자이기 때문에 바로 치즈양을 줄여주고
            q[cnt%n] = q[cnt%n]//2
            #줄인 양이 그래도 0이 아니면 한바퀴 더돌아야 해서
            if q[cnt%n] != 0 :
                #최종 피자에 인덱스값을 저장해준다
                last_pizza = pizza_num[cnt%n]
        cnt += 1

    return last_pizza+1




tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))

    result = last_pizza_battalion(n, pizza)

    print(f'#{t+1} {result}')