'''
백트래킹을 이용하여
{1,2,3,4,5,6,7,8,9,10}의 powerset 중
원소의 합이 10인 부분집합을 구하시오
'''

def backtracking(l, now_i, bit, total) :
    #가지치기
    if total > 10:
        return
    #현재idx가 총길이에 도달했다 -> 1부터 10까지 모든 수를 넣을것인가 말것인가 결정을 끝냈다
    if now_i == len(l) :
        if total != 10 :
            return
        for i in range(len(l)):
            #넣어졌다고 bit리스트에서 1로 표기된 idx라면
            if bit[i]:
                #원소가 담긴 l리스트에서 그 idx위치의 값을 출력한다
                print(l[i], end=' ')
        print()
    #아직 10까지 순환을 못했으면
    else :
        #넣느냐 마느냐 두가지 뿐이기 때문에 2개의 상황만 함
        for i in range(2):
            #현재idx의 요소를 넣을지 말지를 정해야하는데
            bit[now_i] = i
            #for문을 돌면서 0이면 안들어가고 1이면 들어가니 1일때 넣어주는 if문
            if bit[now_i] :
                backtracking(l, now_i + 1, bit, total + l[now_i])
            #현재요소의 bit리스트의 값이 0이면 안들어가는거라는 if문
            else :
                backtracking(l, now_i + 1, bit, total)

#1~10까지 원소가 담긴 리스트
l = list(range(1,11))
#원소가 쓰였는지 안쓰였는지 체크하는 리스트
bit = [0]*len(l)
#원소의 합
total = 0

backtracking(l, 0, bit, total)