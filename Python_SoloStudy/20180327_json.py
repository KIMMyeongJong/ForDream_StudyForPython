# 2018-03-27 파이썬 객체를 JSON으로 변경

import json

person1 = {
    'name':'김명종',
    'age' : '26세',
    'from' : 'corea'
}

print(json.dumps(person1))
'''
person1의 객체정보를 JSON으로 변경한다
dumps를 사용하면 바이트 문자열로 변환된다
우리가 읽을 수 있는 문자열로 저장되기 때문에 문제 바로 확인 가능
'''

with open('test.json','w') as f:
    json.dump(person1,f)


    