# 앞의 함수로만 구현된 코드를  객체지향적으로 수정
class student:
    # 생성자
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        print("Student 클래스의 생성자가 실행됐습니다.")


    # 학생의 총점을 구하는 메소드
    def get_sum(self):
        return self.korean + self.math + self.english + self.science


    # 학생의 평균을 구하는 메소드
    def get_average(self):
        return self.get_sum() / 4   
    
    
    # 학생의 정보를 출력하는 메소드
    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"


oksoon = student("옥순", 100, 100, 100, 100)
youngchul = student("영철", 80, 80, 80, 80)


print("====================")
print(oksoon)
print(oksoon.name)
print(youngchul)

print("====================")
# 옥순/영철의 총점 구하기
res = oksoon.get_sum()
print(res)
res = youngchul.get_sum()
print(res)

# 옥순/영철 평균 구하기
res = oksoon.get_average()
print(res)
res = youngchul.get_average()
print(res)

print("====================")
# 옥순/영철 총점과 평균 구하기
res = str(oksoon)
print(res)
res = str(youngchul)
print(res)