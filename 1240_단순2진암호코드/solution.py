'''
입력받는 2차원 배열 안에
암호코드가 숨어있다
암호코드는 10진법으로 8자리로 이루어져있고
주어지는것은 2진법으로 주어진다
2진법을 10진법으로 바꾼 뒤
홀수자리의합*3 + 짝수자리 합 + 검증코드 가 10의 배수가 되어야 한다
검증코드는 8자리중 가장 마지막 숫자이다

인증된 검증코드면 각 자리의 수의 합을 출력하고
아닐 경우 0을 출력한다

패스워드는 1로 끝이 나기에 코드가 들어있는 리스트를 뽑은뒤
뒤에서부터 1인 것을 찾아다니면 된다
암호가 연속해서 들어오는 것이 아니므로 8씩 스킵하면 안될 것 같다
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}


for t in range(tc):
    #row, col
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(input()))
    for i in range(n):
        if '1' in board[i] :
            arr = board[i]
            break
    for i in range(m-1, -1, -1):
        if '1' == arr[i] :
            start = i
            break

    temp = ''
    for x in arr :
        temp = temp+x
    arr = temp

    code = [0 for _ in range(9)]
    idx = 8
    while idx != 0 :
        if arr[start-6:start+1] in password:
            code[idx] = password[arr[start-6:start+1]]
            idx -= 1
            start -= 7
        else :
            start -= 1
    s = 0
    for i in range(1, 9):
        #홀수
        if i%2 == 1 :
            s += code[i]*3
        else :
            s += code[i]
    if s%10 == 0 :
        print(f'#{t+1} {sum(code)}')
    else :
        print(f'#{t+1} 0')