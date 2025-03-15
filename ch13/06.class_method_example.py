class Student:

    students = []


    # 생성자
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

        # 학생 객체가 생성되면 리스트에 객체 추가 
        Student.students.append(self)

    # 학생의 총점을 구하는 메소드
    def get_sum(self):
        return self.korean + self.math + self.english 

    # 학생의 평균을 구하는 메소드
    def get_average(self):
        return self.get_sum() / 3 
    

    # 클래스 메소드
    @classmethod
    def print_all(cls):
        print("=====학생목록=====")
        print("이름", "총점", "평균", sep="\t")
        for student in cls.students:    # Student.students
            print(str(student))
        print("======================")

    # 학생의 정보를 출력하는 메소드
    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"        
    
Student("영철", 90, 80, 10)    
Student("영수", 11, 67, 49)    
Student("순자", 100, 92, 32)    
Student("현숙", 32, 50, 66)    
Student("영자", 58, 29, 44)    

print(Student.students)
print()
Student.print_all()