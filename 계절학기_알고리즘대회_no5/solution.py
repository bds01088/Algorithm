'''
학생수 n 이 들어오고
답지가 맨 처음 들어온다
그 뒤 n개의 ox가 들어오는데
시험결과로 답지를 만들때 최소한의 인원 수를 출력하라

5
OXOOX
OOXXX
XXOXX
XXXOX
OOOXX
XOXOX
일 경우
OXOOX를 아래 입력값으로 만들어야한다
3번째 XXXOX와 4번째 OOOXX를 합치면
OXOOX를 만들수 있으니 최소 인원은 2이다

특정 2차원 배열을 만들어서
선택한 시험결과값을 하나의 인덱스마다 합쳐놓은 값을 넣는다
답지를 순회하면서 해당 인덱스에 그 값이 존재하는지 확인하면 되지않을까?
------------------------------------------------

'''
import copy

def iscorrect(ele):
    # ele 리스트에 target을 구성한 값들이 각 인덱스에 모두 들어있으면 만들 수 있다는 거니까
    correct = 0
    for i in range(len(target)):
        if target[i] in ele[i]:
            correct += 1
    # 모두 있으면 correct가 target 길이랑 같아지니까
    if correct == len(target):
        return True
    else :
        return False


def dosomething(ele, m):
    global answer, visit, target, arr

    #현재 합친 개수 m이 이미 나온 답보다 크면 할 필요가 없다
    if m >= answer :
        return

    if iscorrect(ele):
        answer = m
        return

    #visit가 1이 아닌 것들과 합쳐야 함
    for i in range(n):
        if visit[i] != 1 :
            next_ele = copy.deepcopy(ele)
            for j in range(len(ele)):
                next_ele[j].extend(arr[i][j])
            visit[i] = 1
            dosomething(next_ele, m+1)
            visit[i] = 0

for t in range(5):
    n = int(input())
    target = input()
    arr = []
    visit = [0]*n
    for i in range(n):
        arr.append(list(map(list, list(input().strip()))))
    if t == 49 :
        pass
    else :
        empty = input()

    answer = 99999

    for i in range(n) :
        #합치는데 가장 베이스가 되는 곳은 visit를 영구히 1로 해준다
        visit[i] = 1
        dosomething(arr[i], 1)

    if answer == 99999 :
        print("-1")
    else :
        print(answer)
