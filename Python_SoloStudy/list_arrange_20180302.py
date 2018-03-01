# 2018-02-28 자료 저장 방법

#list 생성 - 리스트는 컨테이너타입
#자바의 배열과 유사한 개념

empty_list = []
empty_list = list()
#빈 리스트를 만드는 두가지 방법

full_list = [1,2,3,4]
full_list = list([1,2,3,4])
# 리스트에 데이터를 넣는 방법

alist = [1,2,3,4]
list_from_another_list = list(alist)
# 리스트 안에 리스트를 넣는 방법

# 이터레이터를 사용해 리스트 만들기
list_from_iter = list(range(0,10))
even_gen = (x for x in range(0,10) if x % 2 == 0)
list_from_ither2 = list(even_gen)
# range는 특정 범위의 숫자를 리턴하는 range객체(이터레이터)를 반환한다

# 슬라이스
# 리스트에서 원하는 형태를 가져오기 위해 사용
class_a = ["1번","2번","3번","4번","5번","6번"]
# 앞에서 2개 요소 가져오기
print(class_a[1:3])

temp_list = list()
temp_list.append('temp_value')
# temp_value라는 값을 temp_list에 추가
temp_list.insert(0,'first_temp')
# first_temp를 0번 인덱스에 추가
temp_list[1:1] = ['second_temp']#[]안에 값 바꿔보며 이해
# 두번째 위치에 second_temp값 삽입
print(temp_list)

del temp_list[0]
# 0번째 인덱스 삭제
temp_list.remove('second_temp')
# second_temp 삭제
temp_list[0:1] = []
# 첫번째 요소 삭제
print(temp_list)

# 다차원 리스트
date = [
    [0,1,2,3,4,5],
    ['a','b','c','d','e'],
    ['가','나','다','라','마']
]
# 다차원 리스트는 단순히 리스트를 아이템으로 가진다

# ***리스트 정렬***
temp_data = [15,88,35,9,47,1]
temp_data.sort()#[1, 9, 15, 35, 47, 88]
temp_data.sort(reverse = True)#[88, 47, 35, 15, 9, 1]
# sort를 사용하면 원본의 데이터가 변경된다
# 원본을 유지한 채 변경하고 싶으면 sorted를 사용하면 된다

temp_data = [15,88,35,97,47,11,7,1,6,100]
sorted_data = sorted(temp_data)#[1, 6, 7, 11, 15, 35, 47, 88, 97, 100]
reverse_sorted_data = sorted(temp_data,reverse = True)#[100, 97, 88, 47, 35, 15, 11, 7, 6, 1]

# 리스트 복사하기
a = [0,1,5,6,8]
b = a[:]
# [:]를 이용해 복사본을 만든다 - 슬라이스 이용
c = a.copy()
# copy()메소드를 이용해 복사본을 만든다
d = list(a)
# 새로운 리스트를 만들며 복사한다

# 얕은 복사와 깊은 복사
# 모든 데이터를 복사하는 것을 깊은 복사라 한다
data2 = [1,[2,3,4],5]
# 얕은 복사
s_copied = data2.copy()
# 깊은 복사
import copy
d_copied = copy.deepcopy(data2)

#원본 데이터 수정 시
data2[1][1] = 'xx'
print(s_copied)#[1, [2, 'xx', 4], 5]
print(d_copied)#[1, [2, 3, 4], 5]