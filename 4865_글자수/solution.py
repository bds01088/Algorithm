'''
str1, str2가 주어짐
str1에 포함된 글자들이 str2에 몇개씩 들어있는지 찾고
그중 가장 많이 있는 글자개수를 출력함

'''
import sys
sys.stdin = open("input.txt")

def max_alp(str1, str2):
    dict = {}
    #str1의 원소들을 딕셔너리로 저장
    for x in str1 :
        dict[x] = 0
    #str2원소들이 딕셔너리에 있으면 +1해주고
    for x in str2:
        #없는 원소가 있으면 keyerror가 뜨니까 try except로 처리해준다
        try:
            dict[x] += 1
        except KeyError :
            continue

    result = max(dict.values())
    return result

tc = int(input())
for t in range(tc):
    str1 = input()
    str2 = input()
    result = max_alp(str1, str2)
    print(f'#{t+1} {result}')
