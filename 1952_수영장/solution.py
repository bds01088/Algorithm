'''
수영장의 비용을 최소화 하라
1일권, 1달권, 3달권, 1년권의 가격이 주어지고
1월부터 12월까지 수영장을 가는 횟수가 주어진다

DFS를 통해 완전탐색을 실행하고
그중 최소값을 리턴하자
가지치기는 무조건 완전탐색을 성공한 뒤에만 시도하자
'''

import sys
sys.stdin = open('1952_수영장/input.txt')


'''
그리디 하게 그냥 다 찾아보는거다
일일권을 모두 쓸 경우,
한달권을 모두 쓸 경우,
3개월권을 모두 쓰는 경우,
1년권을 쓰는 경우,
해당 월에서 1일권을 한개쓰고 동시에 한달권을 쓰고 그런건 없다
결국 해당 월에 대하여 분기점이 4가지가 생기는 것이다
해당월(즉, 인덱스)에서 1일권과 1달권은 다음달을 탐색해야하는 분기점이고
3달권은 3달 뒤를 탐색해야하는 분기점이고
1년권은 12월말까지 탐색하는 분기점이라는 소리다

이 문제에서는 1년에 대한 내용이기 때문에
해당 월에서 추가된 값이 12를 넘어가면 리턴을 해야한다
예를 들어 1월달인 경우
1일권과 1달권은 다음인덱스인 2월달을 찾아가고
3달권은 4월달 인덱스를
1년권은 13달 인덱스를 찾아간다
1년권의 같은 경우 벌써 12를 넘었기때문에 리턴을 해준다
비용 자체는 최소 비용을 찾아야하므로
글로벌 변수로 놓고 하자
'''
def DFS(start_month, cost):
    global ans, last_month
    if start_month > last_month :
        if ans > cost :
            ans = cost
            return
    else :
        #가지치기1
        #12월까지 가기도 전에 ans보다 커지면 그냥 리턴
        if ans < cost :
            return
        
        if plan[start_month] != 0 :
            #가지치기2
            #일일권과 한달권은 결국 달을 1추가하기 때문에 미리 계산해서 넘겨주면 횟수를 줄일수있다
            if plan[start_month]*day <= month :
                temp_cost = cost + plan[start_month]*day
            else :
                temp_cost = cost + month
            DFS(start_month+1, temp_cost)
            # #일일권 사용
            # temp_cost = cost + plan[start_month]*day
            # DFS(start_month+1, temp_cost)
            # #한달권 사용
            # temp_cost = cost + month
            # DFS(start_month+1, temp_cost)
            #세달권 사용
            temp_cost = cost + quarter
            DFS(start_month+3, temp_cost)
            #1년권 사용
            temp_cost = cost + year
            DFS(start_month+12, temp_cost)
        else :
            DFS(start_month+1, cost)


tc = int(input())

for t in range(tc):
    day, month, quarter, year = map(int, input().split())
    plan = [0]
    plan.extend(list(map(int, input().split())))
    #print(plan)
    
    #가지치기3
    #12월을 넘어가는게 아니라
    #입력받은 plan에서 비용이 생기는 마지막 월을 기준으로 하면 함수 호출이 더 적어지지 않을까?
    i = 12
    while plan[i] == 0 :
        i -= 1
    last_month = i

    '''
    DP 풀이방식
    dp = [0]*13
    for i in range(1, 13):
        #누적 리스트 dp를 작성한다
        #dp[0]은 0이므로 상관없음
        #이전 달의 누적비용에서 이번달 일일권비용을 더해주고
        mmin = dp[i-1]+plan[i]*day
        #이전 달의 누적비용에서 이번달 한달권 비용을 더한값과
        #일일권 비용을 더한 값을 비교하여 최소값 갱신
        mmin = min(mmin, dp[i-1]+month)
        #달의 수가 3월 이상일 경우
        #세달권 사용가능하니까
        if i >= 3:
            #4개월 전의 누적비용에서 세달권 비용을 추가한 값을
            #더해서 최소 비교해준다
            #즉 1월달에서 세달권을 끊은 비용과
            #1, 2, 3월달에서 일일이나 한달권으로 구한 누적비용을 비교함
            mmin = min(mmin, dp[i-3]+quarter)
        #위 세달권과 동일함
        if i >= 12:
            mmin = min(mmin, dp[i-12]+year)
    print(mmin)
    '''

    #모든 종류의 이용권 요금은 3천이하의 정수이고
    #각 달의 이용계획은 각 달의 마지막 일자보다 크지않으므로
    #3천*30*12 정도면 충분할듯?
    #대충 90만
    ans = 900000
    DFS(1, 0)
    print(f'#{t+1} {ans}')