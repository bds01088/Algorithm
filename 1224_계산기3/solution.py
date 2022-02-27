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
order = {'+' : 2, '*' : 1, '(' : 0, ')' : 0}

for _ in range(10):
    n = int(input())
    s = input()
    stack = Stack(n)
    postfix = ''
    for x in s :
        if x in order :
            if stack.isEmpty() :
                stack.push(x)
                pass
        else :
            postfix += x


