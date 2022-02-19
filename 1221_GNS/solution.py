import sys
sys.stdin = open("input.txt")

_ = int(input())

for _ in range(10) :
    t, l = input().split()
    arr = list(input().split())
    #비교대상이 제한적이니 그냥 리스트로 작성
    comp = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    temp = []
    #받은 배열들을 숫자로 변환하기 위해 받은 문자를 comp의 인덱스값을 temp에 저장
    for i in arr :
        temp.append(comp.index(i))

    #버블정렬
    for i in range(len(temp)-1, 0, -1):
        for j in range(0, i):
            if temp[j] > temp[j+1] :
                temp[j], temp[j+1] = temp[j+1], temp[j]

    #정렬된 값을 다시 문자로 출력하기 위해
    for i, num in enumerate(temp) :
        #temp[i]위치에 num을 인덱스로 가지는 문자인 comp[num] 넣어주기
        temp[i] = comp[num]
    print(t)
    for a in temp :
        print(a, end=' ')

