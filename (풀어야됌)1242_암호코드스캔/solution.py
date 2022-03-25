'''
일단은
16진수로 되어있는 코드만 발굴해오는 걸 하자
코드 내부에도 0이 포함되어 있는 경우가 있으니
0이 5개 연속으로 나오면 코드가 끝난 것으로 파악하고
한줄에 두개의 코드가 있을 수도 있으므로
처음부터 끝까지 다돌아야한다
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

    #암호가 있는 열 추출
    for i in range(row) :
        board.append(list(input()))
        #암호가 없는 코드는 0*col과 동일할 것이고
        #중복해서 암호가 나오는 특성상 not in 을 사용해주었다.
        if board[i] != ['0']*col and  board[i] not in code:
            code.append(board[i])
    #print(code)
    #암호 추출
    #code에는 현재 한 row가 들어가있기 때문에
    #0을 제거한 암호코드만을 추출해야한다
    code_16 = []
    for i in range(len(code)):
        j = col-1
        #여기서 가장 큰 문제
        #테스트케이스 암호들을 보면 최대 0이 3개까지 연속으로 암호에 포함되어있는 것이 있다.
        #그래서 암호를 찾는 while문에서 중간에 끼여있는 0을 발견시 j 인덱스 값을 직접 0의 개수만큼 빼주도록 하려고한다
        #그러다보니 또 생기는 문제점은 인덱스 에러가 발생할 수 있다는점이고
        #암호가 왼쪽에서 1~3칸정도만 떨어져있으면 처리가 안된다?는 점이 있다

        #간격이 00으로 있을때도 있고 000으로 있을때도 있다
        #0이 몇개인가 는 의미가 없다는 뜻인거같다
        #암호가 있는건 맨처음 나타났을때 위쪽 행이 0인걸로 파악해야하고
        #끝나는건 어떻게 파악하지?
        while j > 0 :
            if code[i][j] != '0' :
                temp = ''
                #암호중간에 0이 끼여있으므로 while문으로 따로 돌아주고
                while code[i][j] != '0':
                    temp = code[i][j] + temp
                    #그다음수가 0일때
                    if j-1 >= 0 and code[i][j-1] == '0':
                        # 0이 연속 2개일때
                        if j-2 >= 0 and code[i][j-2] == '0':
                            #0이 연속 3개일때
                            if j-3 >= 0 and code[i][j-3] == '0':
                                #0이 연속4개면 break
                                if j-4 >= 0 and code[i][j-4] == '0':
                                    j = j-5
                                    break
                                #0이 3개면
                                elif j == 3 :
                                    j = j-3
                                else :
                                    temp = '000'+temp
                                    j = j-4

                            #0이 2개면
                            elif j == 2:
                                j = j-2
                            else :
                                temp = '00'+temp
                                j = j-3

                        #0이 1개면
                        elif j == 1 :
                            j = j-1
                        else :
                            temp = '0'+temp
                            j = j-2
                    elif j == 1:
                        j = j-1
                    else :
                        j = j-1

                if temp not in code_16 :
                    code_16.append(temp)
            else :
                j -= 1

    #print(code_16)
    #16진수 2진수로 변환
    code_2 = []
    for x in code_16 :
        temp = ''
        for element in x :
            te = bin(int(element, 16)).replace('0b', '')
            while len(te) < 4:
                te = '0'+te
            temp += te
        code_2.append(temp)
    #print(code_2)

    #변화된 값을 뒤에서부터 1인지점 찾고
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
    for pnum, p in enumerate(code_2) :
        resolve = [0 for _ in range(9)]
        resolve_num = 8
        i = len(p)-1
        while i > 0:
            odd_list = [0] * 3
            odd = ''
            #시작점을 찾아야하는데
            #그냥 -1씩 해주면서 최초 시작점을 찾고
            #시작점을 찾으면 그 if문 안에서 카운팅을 하고
            #임시 리스트에 1,0,1의 개수를 넣은뒤
            #최소값으로 나누어 비율을 구하고
            #비율을 str로 변형하여
            #password값에서 일치하는값을 찾아
            #resolve리스트에 넣자
            if p[i] == '1':
                cnt = 0
                while i >= 0 and p[i] == '1':
                    cnt += 1
                    i -= 1
                odd_list[2] = cnt
                cnt = 0
                while i >= 0 and p[i] == '0':
                    cnt += 1
                    i -= 1
                odd_list[1] = cnt
                cnt = 0
                while i >= 0 and p[i] == '1':
                    cnt += 1
                    i -= 1
                odd_list[0] = cnt

                #위의 code에서 암호를 추출하는 점에서 문제가 생겨서 그런지
                #odd_list에 0이 추가되는 경우가 존재하게 되었고
                #이에따라 zerodivisionerror가 뜨게되면서
                #결과값도 차이가 나게 되었다.
                for q in range(3):
                    odd += str(odd_list[q] // min(odd_list))
                    # try :
                    #     odd += str(odd_list[q]//min(odd_list))
                    # except ZeroDivisionError :
                    #     asdf = 1
                if odd in password:
                    try :
                        resolve[resolve_num] = password[odd]
                        resolve_num -= 1
                    except :
                        asadf= 1
            else :
                i -= 1
        s = 0
        for l in range(1, 9):
            # 홀수
            if l % 2 == 1:
                s += resolve[l] * 3
            else:
                s += resolve[l]
        if s % 10 == 0:
            ans += sum(resolve)
        else:
            ans += 0
    print(f'#{t+1} {ans}')









