'''
괄호가 있는 식을 받는다
+와 * 두 연산자만 사용하며
괄호의 유효성은 항상 옳다
후치식으로 해서 계산값을 출력하자
'''

import sys
sys.stdin = open("input.txt")

class Stack :
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [None] * size

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        self.top -= 1
        return self.arr[self.top+1]

    def isEmpty(self):
        if self.top == -1 :
            return True
        else :
            return False

#순서 똑바로해야될듯
push_order = {'+' : 2, '*' : 1, '(' : 0}
pop_order = {'+' : 2, '*' : 1, '(' : 3}
#(는 들어올때 가장 낮은 가치, 안에 있을때는 3으로 한다
oper_list = ['+', '*', '(', ')']

for t in range(1,11):
    n = int(input())
    s = input()
    stack = Stack(n)
    postfix = ''
    for x in s :
        if x in oper_list :
            if stack.isEmpty() :
                #괄호는 유효할때만 들어오므로 )가 먼저 들어올일은 없음
                stack.push(x)
            elif x != ')' :
                while pop_order[stack.arr[stack.top]] <= push_order[x] and stack.top != -1:
                    postfix += stack.pop()
                stack.push(x)
            else :
                while stack.arr[stack.top] != '(' :
                    postfix += stack.pop()
                #while문이 (가 나올때까지 도는거고
                #나와서 while이 끝나면 (를 빼주는 작업을 해야됌
                stack.pop()
        else :
            postfix += x
    #postfix 완성
    new_stack = Stack(len(postfix))
    for x in postfix :
        if x == '+' :
            a = new_stack.pop()
            b = new_stack.pop()
            new_stack.push(b+a)
        elif x == '*' :
            a = new_stack.pop()
            b = new_stack.pop()
            new_stack.push(b*a)
        else :
            new_stack.push(int(x))
    print(f'#{t} {new_stack.arr[new_stack.top]}')


