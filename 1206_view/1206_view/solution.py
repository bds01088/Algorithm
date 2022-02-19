'''
문제
양쪽으로 거리2만큼의 빈공간이 있어야 조망권이 확보된다.
확보되는 조망권의 수를 구하기
가로길이 1000이하, 각 빌딩 높이 최대 255
맨왼쪽과 맨오른쪽은 거리2 동안 아무것도 없다.

입력
10개의 테스트케이스가 주어지며,
개수가 주어지고 그 다음 개수만큼의 숫자들이 들어온다.

출력
#테스트케이스넘버 조망권수
ex) #1 691

해결 방법
3번째부터, n-2번째까지만 해보면된다.
또 좌우 길이2만큼 비교했을때 음수가 한군데라도 나오면 조망권 확보 실패이므로 스킵해도된다.
조망권을 가진다 -> 그 이후 거리2만큼은 조망권을 반드시 못가진다.
다만 마지막부분은? 아마 상관없을 것 같다
그럼 3번째부터 조사를하되 조망권을 가지면 거리2를 넘기는것으로 하자
그럼 인덱스를 조절할 수 있어야하는데.. for문보단 while문이 더 나을 것 같다
'''
import sys
sys.stdin = open('input.txt')


def sight(n, buildings) :
    cnt = 0
    i = 2
    while i < n-2:
        #그냥 다 비교하는게 코드 짜기에 더 쉽지 않을까?
        #i-2, i-1, i+1, i+2 값을 리스트로 만들고 for문으로 돌려서 계속 비교하고
        #그 사이에 음수 또는 0이 나온다면 바로 스킵하는 것으로 만들까?
        #비교 대상 리스트화
        sides = [i-2, i-1, i+1, i+2]
        '''
        #추가할 것
        #sides에서 가장 큰 값만 찾아서 그것만 비교하면 더 간단해진다
        '''
        #빌딩의 최대 길이는 255이므로 그것보다 크게 설정한다
        max_view = 256
        #x = buildings[i] 현재 검사하고 있는 값을 디버깅할때 확인하기 위해 추가함
        for j in sides :
            #비교대상군의 빌딩의 높이가 검사값보다 크다면
            if (buildings[i] - buildings[j]) <= 0 :
                #다음값으로 바로 비교하기 위해 i를 1만 증가시키고
                i += 1
                #max_view값을 초기화해준다
                max_view = 256
                break
            else :
                #조망권이 확보가 된다면
                # 4개의 비교군과 비교했을때 제일 작은 값이 실제로 확보되는 조망권 크기이므로
                if (buildings[i] - buildings[j]) < max_view :
                    max_view = buildings[i] - buildings[j]
        #for문이 완료된 뒤에 break문으로 나왔는지 실제 조망권이 확보되었는지 비교는 max_view가 초기 값인지로 확인한다
        if max_view != 256 :
            cnt += max_view
            #조망권이 확보된 빌딩의 좌우 2칸내의 빌딩은 조망권이 확보가 불가능하기 때문에 3번째 뒤 빌딩으로 바로 이동한다
            i += 3
    return cnt


for test_case in range(10):
    case_len = int(input())
    case = list(map(int, input().split()))
    result = sight(case_len, case)
    print(f'#{test_case+1} {result}')

