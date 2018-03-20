# 2018-03-20 함수

'''
매개변수 - 함수에 입력으로 넣을 값
반환값 - 함수에 입력으로 넣을 값
로직 - 함수의 처리 내용
설명 - 함수를 설명하는 문자열
'''
value = 0
def sum(a, b):
    value = a + b
    return value
# def - 함수 선언을 위한 키워드
# return - 반환값을 위함
'''
함수에서 매개변수가 없으면 매개변수 부분은 비우고 ()만 표시할 수 있다
결과값이 없으면 return문이 없어도 된다
함수의 이름을 만들때 신중치 않으면 기존에 만들어진 함수가 있을 수 있다
기존에 사용하던 이름과 동일한 이름으로 함수를 정의하면 새로 정의된
함수의 이름이 기존의 이름을 갱신해 버린다
'''

# 기본 매개변수를 설정할 때는 반드시 뒷쪽에 있는 매개변수를 먼저 설정해야 한다

def print_args(p1,p2 = "p2", p3 = "p3"):
    print(p1,p2,p3)
'''
print_args()                            에러발생
print_args("p1")                        p1 p2 p3
print_args("p1", "new p2")              p1 new p2 p3
print_args("p1", "new p2", "new p3")    p1 new p2 new p3
print_args("p1", p3 = "new p3")         p1 p2 new p3

매개변수를 출력하는 함수다
p1만 매개변수에 해당하는 값을 반드시 입력받아야 한다
위에서는 이름 지정 매개변수를 통해 원하는 매개변수를 직접 지정했다
'''

# 함수에서 명시적으로 정의하지 않는 매개변수 처리 방법

def add(*args):
    total = 0
    for i in args:
        total +=i
    return total

add(1,2)                     #6
add(1,2,3,4,5,6,7,8,9,10)   #55

'''
위의 add함수는 매개변수로 입력된 숫자의 합을 구한다
입력되는 수는 그 갯수를 알 수 없다
이러한 경우에 args를 통해 해당 매개변수들을 튜플로 만들어 *args에 대입한다
굳이 args가 아니더라도 *이 있으면 튜플로 해당 변수들을 받겠다는 뜻이기 때문에
*을 붙이고 매개변수를 설정해 준다
'''

# 이름 지정 매개변수를 사용하면 매개변수들을 딕셔너리로 만들어 함수의 매개변수로 담을 수 있다

def print_args(**kwlist):
    print(kwlist)
print_args(p1 = "1", p2 = "4", p3 = 500)
# {'p1': '1', 'p2': '4', 'p3': 500}
