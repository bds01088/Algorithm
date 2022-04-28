'''
패턴은 알파벳 소문자 여러 개와 별표(*) 하나로 이루어진 문자열
별표는 문자열의 시작과 끝에 있지 않다.
총 N개의 줄에 걸쳐서,
입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA",
일치하지 않으면 "NE"를 출력한다.

3
a*d
abcd
anestonestod
facebook
'''

n = int(input())
pattern = input()

front = ''
rear = ''
for i in range(len(pattern)):
    if pattern[i] == '*':
        rear = pattern[i+1:]
        break
    front += pattern[i]

for i in range(n):
    s = input()
    if len(s) < len(front)+len(rear):
        print('NE')
        continue
    if s[:len(front)] == front :
        if s[len(s)-len(rear):] == rear:
            print('DA')
        else :
            print('NE')
    else :
        print('NE')




