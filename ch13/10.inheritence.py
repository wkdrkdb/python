# 상속 
#   핵심적인 속성과 메소드를 가지고 있는 부모 클래스를 정의하고, 
#   확장이 필요한 속성과 메소드가 존재하면 자식 클래스에 추가로 구현합니다.


# 부모 클래스
class Parent:
    # 부모 클래스의 생성자
    def __init__(self):
        self.value = "Parent"
        print("부모 클래스의 생성자가 호출되었습니다.")

    # 부모 클래스의 메소드
    def test_method(self):
        print("Parent의 test()메소드가 실행되었습니다.")
        print(f"부모 클래스의 인스턴스 변수 : {self.value}")     


# 자식 클래스
class Child(Parent):
    # 자식 클래스의 생성자
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출 
        print("자식 클래스의 생성자가 호출되었습니다.")

    def test_method2(self):
        print("자식 클래스의 test 메소드입니다.")    

class Child2(Parent):
    def __init__(self):
        pass

parent = Parent()        
print(parent.value)
parent.test_method()

child = Child()
print(child.value)
child.test_method()
child.test_method2()
