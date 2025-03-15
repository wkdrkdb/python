class Student:
    # 클래스 변수 선언
    student_count = 0
    classroom = "A반"

    def __init__(self, name):   #  def __init__(self, name, age):
        
#       if age < 20:
#           print("미성년자는 객체 생성이 불가능합니다")        # 생성자를 활용하는 다양한 방법 
        
        # 인스턴스 변수 선언
        self.name = name

        # 클래스 변수를 사용하여 학생 수 카운트
        Student.student_count += 1

        # 클래스 변수로 학생 수 출력
        print(f"{Student.student_count}번째 학생 {self.name}이 생성되었습니다.")


a = Student("영철")        
b = Student("영수")        
c = Student("순자")        
d = Student("현숙")        
e = Student("영자")        
# Student("영철", 15)

print()

# 클래스 변수로 학생 수 출력 
print(Student.student_count)
print(Student.classroom)