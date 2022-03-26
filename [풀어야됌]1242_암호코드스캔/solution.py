'''
일단은
16진수로 되어있는 코드만 발굴해오는 걸 하자
코드 내부에도 0이 포함되어 있는 경우가 있으니
0이 5개 연속으로 나오면 코드가 끝난 것으로 파악하고
한줄에 두개의 코드가 있을 수도 있으므로
처음부터 끝까지 다돌아야한다
'''
import sys
sys.stdin = open('iinput.txt')

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
    #0은 2진수로 변환해도 0이다
    #code에 들어있는 모든 것을 하나씩 2진수로 변환하자
    #0을 기준으로 뭐 끊긴다거나 그런건 다 다르기 때문에 절대 못한다
    #또한 여러 암호코드가 한줄에 겹쳐서 나오는 경우도 같이 포함하고 있기 때문에
    #중복 코드를 또 제거해주어야 할 것이다

    #16진수 2진수로 변환
    code_2 = []
    for x in code :
        temp = ''
        for element in x :
            #4자리로 고정시켜서 변환해야한다
            te = bin(int(element, 16)).replace('0b', '')
            while len(te) < 4 :
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
        code_list = []
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

                for q in range(3):
                    odd += str(odd_list[q] // min(odd_list))

                if odd in password:
                    resolve[resolve_num] = password[odd]
                    resolve_num -= 1
                #8개로 이루어진 코드 완성 시
                if resolve_num == 0 :
                    if resolve not in code_list :
                        code_list.append(resolve)
                    resolve = [0 for _ in range(9)]
                    resolve_num = 8

            else :
                i -= 1
        s = 0
        for ccc in code_list:
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

