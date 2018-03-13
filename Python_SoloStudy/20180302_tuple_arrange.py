# 2018-03-02 자료 저장 방법

# 튜플은 리스트처럼 사용할 수 있지만 변경이 불가능하다
# 튜플은 오직 읽기만 가능 - 리턴값이 복수인 경우에 사용
# 쓰기와 관련된 API는 사용 불가

# 튜플 생성 방법
tuple1 = (1,2,3,4,5,6)
tuple2 = tuple([1,2,3,4,5,6])
tuple3 = tuple(range(0,10))
tuple4 = tuple()

temp_list = (1,3,45,7,9,11,13,15,17,19)
temp_list2 = (2,4,6,8,10,12,14,16,18)

2 in temp_list#2가 temp_list에 있는지 확인
2 not in temp_list#2가 temp_list에 없는지 확인

all_list = temp_list + temp_list2
#튜플은 sort불가능

temp_list2 * 2
2*temp_list2
# temp_list2가 두개 붙어 있는 튜플 생성

temp_list2[0]
temp_list2[0:5]
temp_list2[0:5:2]

len(temp_list2)#temp_list2의 길이
min(temp_list2)#temp_list2의 가장 작은 수
max(temp_list2)#temp_list2의 가장 큰 수

temp_list2.index(6)#temp_list2에서 6이 가지는 인덱스
temp_list2.count(4)#temp_list2에서 4인 요소의 갯수

# range함수
# range함수는 range객체를 생성한다
# range객체는 특정 범위의 정수를 표현한다

num_list = list(range(10))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list = list(range(1,11))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list = list(range(0,30,5))#[0, 5, 10, 15, 20, 25]
# 0~29의 정수 중 5씩 증가
num_list = list(range(0,-11,-1))#[0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

