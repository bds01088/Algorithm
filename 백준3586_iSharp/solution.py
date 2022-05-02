'''
변수 선언문을 받고
정리된 선언문을 내주자
변수 타입과 변수 이름은 공백으로 구분하고
변수이름과 변수이름 사이에는 컴마공백으로 구분된다
세미콜론이 끝에 온다

출력은 각 변수마다 한줄에 하나씩만 선언해주고
해당 변수의 추가변수형은 맨뒤에서 부터 차례대로 변수선언부분에 붙여준다

변수형과 변수명은 알파벳 소문자 대문자로만 이루어져있다

일단은 공백을 기준으로 나눠서 리스트를 만들면
맨첫번째는 변수형이 담기고
그 뒤로는 변수명이 올텐데
각 변수명의 맨 마지막은 콤마(,)거나 세미콜론(;)일 것이니 버려주자

'''
import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(tc):
    whole = list(input().split(' '))
    print(f'#{t+1}')
    varT = whole[0]
    varnames = []
    for i in range(1, len(whole)):
        varnames.append(whole[i][0:len(whole[i])-1])

    for var in varnames:
        temp = varT
        i = len(var)-1
        while not var[i].isalpha() :
            if var[i] == ']' :
                i -= 1
                temp += '[]'
            else :
                temp += var[i]
            i -= 1

        print(f'{temp} {var[:i+1]};')
