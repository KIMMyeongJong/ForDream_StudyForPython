# 2018-03-27 데이터 저장

from pprint import pprint
import pickle

'''
dump()함수는 매개변수로 입력한 객체를 직렬화해서 파일에 저장한다
이 데이터들은 pickle.load()함수를 통해 다시 복원된다.
두 함수는 파일을 대상으로 한다.
pickle은 데이터 저장을 위해 바이너리를 사용하고 있다

pickle.dumps - 객체
pickle.loads - 바이트 객체
바로 파일에 직접 저장하거나 읽는 것이 아니라 바이트 객체로 변환
데이터를 파일이 아닌 다른 곳으로 보내거나 다른 형태로 이용하기 위해
임시로 쓰는 경우에 자주 사용
'''

person1 = {
    'name':'김명종',
    '나이':'26',
    '지역':'한국'
    
}

person2 = {
    'name':'니시노 나나세',
    '나이':'25',
    '지역':'일본'
}

people = [person1,person2]
# 데이터를 리스트로 만들기

# 데이터 저장
with open('people.pickle','wb')as f:
    pickle.dump(people,f)
    
# 저장된 데이터를 읽는다
with open('people.pickle','rb')as f:
    loaded_people = pickle.load(f)
    
pprint(loaded_people)

'''
pickle은 임의 타입도 저장하고 로드 가능
__XXX__메소드는 사용자가 직접 호출하기 보다 특별한 경우에 호출된다
'''

class Book:
    '''책 정보들을 파일이 저장하는 클래스'''
    def __init__(self,category):
        self.category = category
        self.books = []
        
    def addBook(self,book_title):
        if book_title not in self.books:
            self.books.append(book_title)
            
    def getBooks(self):
        return self.books
    
    def __getstate__(self):
        state = self.__dict__.copy()
#         필요 없는 데이터를 삭제 가능
        return state
    
    def __setstate__ (self,state):
        self.__dict__.update(state)
        
if __name__ == '__main__':
    
#     book객체 생성
    book = Book("my Book")
    book.addBook('book2')
    book.addBook('book3')
    book.addBook('book4')
    book.addBook('book5')
    book.addBook('book6')
    book.addBook('book8')
    book.addBook('book7')
    print(book.getBooks)

    pickled_data = pickle.dumps(book)
    
    new_book = pickle.loads(pickled_data)
    print('-----------------------------------------------------')
    print(book.getBooks())