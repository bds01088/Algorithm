'''
1번부터 n번까지 카드를 나눠가짐
1 가위
2 바위
3 보
i~(i+j)//2 and (i+j)//2+1~j로 분할정복하라

같은 카드일 경우 인덱스 번호가 작은 쪽을 승자로 하자
-> 같은 카드일 경우 왼쪽학생이 이기도록
1등을 찾아라

해결방법
분할하자 -> 입력받는 list길이가 1일때까지 분할
2이다 그럼? 좌 우 비교해서 이긴 놈의 인덱스를 리턴
분할하는 함수와 비교하는 함수 따로 만들기
list의 길이가 1일때 L R 비교해서 큰놈 리턴하는걸로

가위는 바위한테 짐
바위는 보한테 짐
보는 가위한테 짐
1 < 2
2 < 3
3 < 1
'''

# import sys
# sys.stdin = open('input.txt')

#인덱스를 받자
def RSP(idx_a, idx_b) :
    global tournamant_tree
    #무승부
    if tournamant_tree[idx_a] == tournamant_tree[idx_b] :
        return idx_a
    #가위
    elif tournamant_tree[idx_a] == 1 :
        if tournamant_tree[idx_b] == 2 :
            return idx_b
        elif tournamant_tree[idx_b] == 3 :
            return idx_a
    #바위
    elif tournamant_tree[idx_a] == 2 :
        if tournamant_tree[idx_b] == 3 :
            return idx_b
        elif tournamant_tree[idx_b] == 1 :
            return idx_a
    #보
    else :
        if tournamant_tree[idx_b] == 2 :
            return idx_a
        elif tournamant_tree[idx_b] == 1 :
            return idx_b


def partition(L, R):
    global tournamant_tree
    if len(tournamant_tree[L:R+1]) <= 2:
        winner = RSP(L, R)
        #winner는 인덱스 값이다
        return winner
    else :
        mid = (L+R)//2
        a = partition(L, mid)
        b = partition(mid+1, R)
        winner = RSP(a,b)
        return winner

tc = int(input())

for t in range(tc):
    n = int(input())
    tournamant_tree = list(map(int, input().split()))
    result = partition(0, n-1)
    print(f'#{t+1} {result+1}')
