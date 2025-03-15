# math 모듈 가져오기
import math

class Circle:

    # 생성자
    def __init__(self, radius):
        self.__radius = radius # 인스턴스 변수

    # 원의 둘레를 구하는 메서드
    def get_circumference(self):
        return 2 * math.pi * self.__radius    
    
    # 원의 넓이를 구하는 메서드
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    # 게터와 세터
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0:
            raise ValueError("길이는 양수여야 합니다.")
        self.__radius = value


# 원의 둘레와 넓이를 구합니다. (클래스 외부)    
circle = Circle(10)
print(f"원의 둘레 == {circle.get_circumference()}")
print(f"원의 넓이 == {circle.get_area()}")

print()

# print(circle.__radius)
print(f"원의 둘레 == {circle.get_circumference()}")
print(f"원의 넓이 == {circle.get_area()}")

print(circle.get_radius())
circle.set_radius(5)
print(circle.get_radius())

