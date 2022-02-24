'''
숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.
'''
#import sys
#sys.stdin = open("input.txt")

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


tc = int(input())

oper = ['+', '*', '-', '/']

for t in range(tc):
    s = list(input().split())
    stack = Stack(len(s))
    result = 0
    flag = 0
    for x in s :
        #연산자이고 스택에 2개이상있을경우
        if x in oper and stack.top > 0:
            a = stack.pop()
            b = stack.pop()
            if x == '+' :
                c = b+a
                stack.push(c)
            elif x == '-':
                c = b-a
                stack.push(c)
            elif x == '*':
                c = b*a
                stack.push(c)
            else :
                c = b//a
                stack.push(c)
        #연산할 숫자가 스택안에 2개이상 없을시 에러
        elif x in oper and stack.top <= 0 :
            flag = 1
            break
        #끝이면 팝
        elif x == '.' :
            #스택내에 숫자가 하나만 있어야하는데 여러개있으면 계산이 다 안된거임
            if stack.top != 0 :
                flag = 1
            else :
                result = stack.pop()
        #숫자면 푸시
        else :
            stack.push(int(x))
    
    #출력
    if flag :
        print(f'#{t+1} error')
    else :
        print(f'#{t+1} {result}')
