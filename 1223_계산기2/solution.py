'''
“3+4+5*6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"34+56*+7+"
변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
총 10개의 테스트 케이스가 주어진다.

해결방법
일단 받고
for문 돌아서 +나 *가 아니면
비연산자 스택에 넣고
* +면 팝 후 푸시
+ *면 그냥 스택 
* *면 팝 후 푸시
+ +면 팝 후 푸시
즉 +는 우선순위 2
*은 우선순위 1
이므로 동률이거나 우선순위가 이전 것보다 크다면 팝하고 푸시
이전 것보다 우선순위가 작다면 그냥 스택
'''

import sys
sys.stdin = open("input.txt")

class Stack :
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [None] * size
    
    def pop(self) :
        self.top -= 1
        return self.arr[self.top+1]

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def isEmpty(self):
        if self.top == -1 :
            return True
        else :
            return False

order = {'+' : 2,
         '*' : 1}


for t in range(10):
    length = int(input())
    s = input()
    post = ''
    stack = Stack(length)
    for x in s :
        #연산자 일 경우
        if x in order :
            #비어있다면 추가
            if stack.isEmpty():
                stack.push(x)
            #안비어있다면
            #현재 탑에 존재하는 연산자와 같다면
            elif order[stack.arr[stack.top]] <= order[x]:
                #모두 팝해주기
                while stack.top != -1 and order[stack.arr[stack.top]] <= order[x]:
                    post += stack.pop()
                stack.push(x)
            else :
                stack.push(x)
        else :
            post += x
    #후치수식 만들기 완료
    while stack.top != -1:
        post += stack.pop()

    #계산하기
    new_stack = Stack(len(post))
    for x in post :
        #숫자면
        if x not in order :
            new_stack.push(int(x))
        #연산자면
        else :
            #스택에 들어간 가장 최근의 2개 숫자를 뽑아온다
            if x == '+' :
                a = new_stack.pop()
                b = new_stack.pop()
                c = b+a
                new_stack.push(c)
            else :
                a = new_stack.pop()
                b = new_stack.pop()
                c = b*a
                new_stack.push(c)
    print(f'#{t+1} {new_stack.pop()}')