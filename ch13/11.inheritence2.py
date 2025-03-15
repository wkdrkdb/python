# 부모 클래스 
class Person:
    # 부모 클래스 생성자에는 이름, 나이, 성별을 저장하는 변수
    def __init__(self, name, age, gender):
        self.name = name        
        self.age = age
        self.gender = gender

    # introduce 메소드
    def introduce(self):
        return f"안녕하세요. 제 이름은 {self.name}입니다. 저는 {self.age}살 입니다."

    # str 메소드
    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"


# 자식 클래스(1)
class Student(Person):
    # 학생 클래스 생성자에는 이름, 나이, 성별, 국어, 수학, 영어 점수를 저장하는 변수
    def __init__(self, name, age, gender, korean, math, english):
        super().__init__(name, age, gender)
        self.korean = korean
        self.math = math
        self.english = english

    def introduce(self):
        return " - 저는 학생입니다. 특기는 공부하기 입니다."    

    # 부모 클래스의  __str__() 오버라이딩
    def __str__(self):
        return f"{super().__str__()}, {self.korean}, {self.math}, {self.english}"
     

# 자식 클래스(2)
class Teacher(Person):
    # 선생님 클래스 생성자에는 이름, 나이, 성별, 과목, 경력
    def __init__(self, name, age, gender, subject, experience):
        super().__init__(name, age, gender)
        self.subject = subject
        self.experience = experience

    # 오버라이드(1)
    def __str__(self):
        return f"{super().__str__()}, {self.subject}, {self.experience}"
    
    # 오버라이드(2)
    def introduce(self):
        return f"{super().introduce()} -저는 선생님입니다. 특기는 수업하기 입니다."

student = Student("가유", 18, "남자", 100, 97, 95)
print(student)
print(student.introduce())

teacher = Teacher("영수", 40, "남자", "컴퓨터", 5)
print(teacher)
print(teacher.introduce())

# -------------------------------------------------------
print()

# type() + == 로 객체 비교
print(type(student) == Student) # True
print(type(student) == Person) # False

print()

# isinstance() 로 객체 비교
print(isinstance(student, Student)) # True
print(isinstance(student, Person)) # True