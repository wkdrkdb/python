# 학생 클래스를 생성
class Student:
    # 생성자
    def __init__(self, name):
        self.name = name
    # 메소드
    def study(self):
        print("공부하기")


# 선생님 클래스를 생성
class Teacher:
    # 생성자
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    # 메소드
    def teach(self):
        print(f"{self.subject} 가르치기")


# Student 객체 생성
student = Student()

# isinstance() 함수를 사용해서 특정 클래스의 객체인지를 확인 
isStudent = isinstance(student, Student)
print(isStudent)    # True

isStudent = isinstance(student, Teacher)
print(isStudent)    # False

# type() 함수를 사용해서 특정 클래스의 객체인지를 확인
#   상속이 없는 경우에는 type() 함수와 동등연산자를 사용하여 판별이 가능함
#   상속이 이루어지는 경우 isinstance() 함수와 다른 결과를 출력하게 됩니다
#   따라서 객체의 타입을 확인할 때는 isinstance() 함수를 사용해야 합니다   
print(type(student) == Student)     # True
print(type(student) == Teacher)     # False

# 학생과 선생님 객체를 생성해서 리스트에 담기
classroom_a  = [Student("영수"), Student("현숙"), Teacher("데프콘", "랩")]

# isinstance() 함수를 사용해서 객체의 클래스를 확인하고, 각 객체에 맞는 메소드 호출
for person in classroom_a:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()    