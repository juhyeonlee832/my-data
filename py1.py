# 함수 선언
def add10_20(num1, num2):
    sum=num1+num2
    return sum

# 함수 호출
result  = add10_20(1,99)


# [1] 100 여부 확인
if result == 100 :
    print("100 입니다")

elif result == 200 :
    print("200 입니다")

else :
    print("100 200이 아님")

# [2] 0 보다 큰지 확인
if result > 0:
    print("0보다 큽니다")


fruits = ['사과', '바나나', '수박']

for i in range(len(fruits)) :
    print(fruits[i])

for f in fruits :
    print(f)


def process() :
    a = 10
    try :
        b = 10/0
    except:
        print("에러발생")
    

process()

class Student :
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

    def hello(self) :
        print(self.name)

man = Student("정민", 35)



