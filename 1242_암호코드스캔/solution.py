'''
그냥 브루트 포스로 탐색한다
입력받는 16진수를
하나도 빠짐없이 그냥 2진수 4자리로 고정시켜서
문자열로 붙이고 저장한다
거기서 뒤에서 부터 탐색해서 1인 곳을 찾으면
그 윗행에 0이 존재한다면
카운트 시작한다
행이 0인 지점에는 암호가 들어올 수 없다
윗행이 0이 존재하는 것으로 암호코드가 아래쪽에 중복되어 나타나는 걸 합 추가가 안되도록 방지할 수 있다

'''
import sys
sys.stdin = open('input.txt')

tc = int(input())

#1,0,1의 비율을 문자열로 합쳐서 키값으로 사용
password = {
    '211' : 0,
    '221' : 1,
    '122' : 2,
    '411' : 3,
    '132' : 4,
    '231' : 5,
    '114' : 6,
    '312' : 7,
    '213' : 8,
    '112' : 9
}

for t in range(tc):
    row, col = map(int, input().split())
    code = []
    board = []

    for i in range(row) :
        board.append(list(input()))

    #print(code)
    #암호 추출
    #code에는 현재 한 row가 들어가있기 때문에
    #0은 2진수로 변환해도 0이다
    #code에 들어있는 모든 것을 하나씩 2진수로 변환하자
    #0을 기준으로 뭐 끊긴다거나 그런건 다 다르기 때문에 절대 못한다


    #16진수 2진수로 변환
    code_2 = []
    for i in range(row):
        temp = ''
        for j in range(col) :
            #4자리로 고정시켜서 변환해야한다
            te = bin(int(board[i][j], 16)).replace('0b', '')
            while len(te) < 4 :
                te = '0'+te
            temp += te
        code_2.append(temp)
    #print(code_2)

    #변화된 값을 뒤에서부터 1인지점 찾고
    #그 위치의 윗행이 0일때 카운트 시작하고
    #1부터 0이 나올때까지 cnt 측정
    #0이나오면 cnt를 저장
    #그 이후 1이나올때까지 cnt 측정 저장을 반복 2회함
    #그럼 0, 1, 0, 1의 개수를 통해 비율을 구할수 있음
    #문제가 좀 이상해서
    #위에처럼 안하고
    #1, 0, 1 의 개수만 구해서 비율을 비교하면 된다
    #두번째 1의 개수카운팅이 끝나면 비율 비교하고
    #다시 1이 시작될때까지 왼쪽으로 이동하면 됌

    ans = 0
    code_list = []
    for i in range(row) :
        resolve = [0 for _ in range(9)]
        resolve_num = 8
        j = len(code_2[i])-1
        while j > 0:
            #시작점을 찾아야하는데
            #그냥 -1씩 해주면서 최초 시작점을 찾고
            #시작점을 찾으면 그 if문 안에서 카운팅을 하고
            #임시 리스트에 1,0,1의 개수를 넣은뒤
            #최소값으로 나누어 비율을 구하고
            #비율을 str로 변형하여
            #password값에서 일치하는값을 찾아
            #resolve리스트에 넣자
            if code_2[i][j] == '1' and code_2[i-1][j] == '0':
                odd_list = [0] * 3
                odd = ''

                cnt = 0
                while j >= 0 and code_2[i][j] == '1':
                    cnt += 1
                    j -= 1
                odd_list[2] = cnt

                cnt = 0
                while j >= 0 and code_2[i][j] == '0':
                    cnt += 1
                    j -= 1
                odd_list[1] = cnt

                cnt = 0
                while j >= 0 and code_2[i][j] == '1':
                    cnt += 1
                    j -= 1
                odd_list[0] = cnt

                mmin = min(odd_list)
                for q in range(3):
                    odd += str(odd_list[q] // mmin)

                if odd in password:
                    resolve[resolve_num] = password[odd]
                    resolve_num -= 1

                #8개로 이루어진 코드 완성 시
                if resolve_num == 0 :
                    code_list.append(resolve)
                    resolve = [0 for _ in range(9)]
                    resolve_num = 8

            else :
                j -= 1
    ans = 0
    for ccc in code_list:
        s = 0
        for l in range(1, 9):
            # 홀수
            if l % 2 == 1:
                s += ccc[l] * 3
            else:
                s += ccc[l]
        if s % 10 == 0:
            ans += sum(ccc)
        else:
            ans += 0
    print(f'#{t+1} {ans}')

