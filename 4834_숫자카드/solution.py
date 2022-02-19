'''
문제
0~9 사이의 숫자가 적힌 카드가 주어진다
그 중 가장 많은 카드의 번호와 갯수를 출력하라
만약 카드 장수가 같다면 큰 번호인 카드를 출력한다

입력
테스트 케이스 개수 주어지고
카드 장 수 주어지고
카드 입력이 공백없이 주어진다

출력
#테스트케이스번호 카드번호 카드수
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

def count_card(li) :
    #카드의 수는 0~9까지이므로 인덱스가 0~9까지인 리스트를 만들어 갯수를 센다
    count = [0]*10
    for card in li :
        count[card] += 1
    max = 0
    max_idx = 0
    #뭔가 max랑 max_idx 중 하나만 써서 해결가능할 것 같기도한데 아직은 잘 모르겠다
    for idx in range(10) :
        if count[idx] > max :
            max = count[idx]
            max_idx = idx

        elif count[idx] == max :
            if idx > max_idx :
                max_idx = idx
    return max, max_idx

for i in range(tc):
    card_num = int(input())
    #공백없이 들어오는 숫자를 하나씩 때서 리스트로 만드는게 split으로 안될줄은 몰랐는데..
    #일단 문자열로 받고 for문으로 하나씩 때어내자
    '''
    ###############################
    234234234라는 값을 2 3 4 2 3 4 2 3 4로 리스트를 받으려면
    list(map(int, input()))로 받아오면 자동으로 때어져서 들어옴
    굳이 스플릿 안붙여도 됌
    ###############################
    '''
    card_list = input()
    cards = []
    #공백없이 들어오는건 그냥 빈 리스트를 하나 만들어서 추가하는걸로 함
    for j in card_list:
        #정수화
        cards += [int(j)]
    max_num, max_idx = count_card(cards)
    print(f'#{i+1} {max_idx} {max_num}')
