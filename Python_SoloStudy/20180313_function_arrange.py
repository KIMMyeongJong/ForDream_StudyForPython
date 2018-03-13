# 2018-03-13 자료 저장 방법

# 매개변수 : 함수에 입력으로 넣을 값
# 로직 : 함수의 처리 방법
# 반환값 : 함수의 결과값

# 일반 함수
def add(x,y):
    return x+y

add(1,3)
#add(1)에러 발생

# 매개변수의 갯수를 알 수 없을 때

def add(*args):
    total = 0
    for i in args:
        total +=i
    return total
add(1,2)#3
add(1,2,3,4,5,6,7,8,9)#45

# *은 튜플로 여분의 매개변수를 받겠다고 지정하는 것

def print_args(**kwlist):
    print(kwlist)
    
print_args(p1 = "1",p2 = "2", p3 = "3")

# 함수에 선언되지 않은 이름 지정 매개변수를 사용하면 매개변수들을 딕셔너리로 만들어서 함수의 매개변수로 받을 수 있다

####함수 호출 방법###
def add(*args):
    total = 0
    for i in args:
        total +=i
    return total

vals = [1,2]
add(*vals)     #3

vals = (1,2,3,4,5,6,7,8,9,10)
add(*vals)     #55

###함수의 설명 방법###
def myfunc():
    """문서 설명
    
    이 함수는 아무 일도 하지 않는 함수로 함수의 docstring을 설명하기 위한 함수이다
    
    파라미터 : 없음
    리턴 : 없음
    """
    pass
myfunc.__doc__
help(myfunc)

