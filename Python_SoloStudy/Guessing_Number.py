from random import *

value = randint(1,100)
count = 5
def compare(num):

    if num>value:
        print("-입력하신 값이 더 높습니다-")
    elif num<value:
        print("*답이 더 높습니다*")
    else :
        print("정답을 맞추셨습니다")
        print("총 시도 횟수 : " + str(5-count))
    if count==0:
        print("답을 맞추지 못하였습니다")
        print("답 : " + str(value))

while count>0:
    answer = int(input("값을 입력해 주세여"))
    count = count - 1
    compare(answer)
    print("남은 횟수 : " + str(count))