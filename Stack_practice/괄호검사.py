'''
stack class를 구현하고
구현한 stack을 이용하여 괄호검사를 하자
괄호의 짝이 올바르다면 1을
아니라면 -1을 출력한다
'''
import sys
sys.stdin = open("Parenthesis_input.txt")

class Stack :
    def __init__(self, size):
        self.size = size
        self.arr = [None]*size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else :
            return False

    def is_full(self):
        if self.top == self.size-1:
            return True
        else :
            return False

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        self.top -= 1
        return self.arr[self.top+1]

    def peek(self):
        return self.arr[self.top]

    def bottom(self):
        return self.arr[0]

def Parenthesis_Correct(stack, str):
    result = 0
    for x in str:
        #빈 스택에 x가 )이면 잘못됐으니 -1
        if stack.is_empty() == True and x == ')':
            result = -1
            return result
        elif x == ')':
            stack.pop()
        #x가 (면 스택에 저장
        else:
            stack.push(x)
    if stack.is_empty() == False:
        result = -1
    else :
        result = 1
    return result

tc = int(input())

for t in range(tc):
    str = input()
    stack = Stack(len(str))
    result = Parenthesis_Correct(stack, str)
    print(f'#{t+1} {result}')
