from itertools import product

def solution(users, emoticons):

    discount = [10, 20, 30, 40]

    #모든 경우의 수를 다 구해야함
    #고로 discount랑 emoticons의 카테시안 곱을 구해야함
    #할인률, 이모티콘
    cartesian = list(product(discount, repeat=len(emoticons)))

    mCnt = 0
    mAmount = 0
    for case in cartesian:
        cnt = 0
        amount = 0
        #하나의 유저 -> 이모티콘 순으로 계산해야지 이용권을 구매할지 개별구매할지 정할 수 있음
        for user in users:
            s = 0
            for i in range(len(emoticons)):
                #유저의 구매 할인률과 비교
                if user[0] <= case[i] :
                    s += emoticons[i]*((100-case[i])/100)
            if s >= user[1] :
                cnt += 1
            else :
                amount += s
        if mCnt < cnt :
            mCnt = cnt
            mAmount = amount
        elif mCnt == cnt :
            if mAmount < amount :
                mAmount = amount
    answer = [mCnt, int(mAmount)]

    return answer

# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))