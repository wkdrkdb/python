class Test:
    # 생성자
    def __init__(self, name):
        self.name = name
        print(f"{self.name}이 생성되었습니다.")

    # 소멸자
    def __del__(self):
        print(f"{self.name}이 제거되었습니다")


Test("A")
Test("B")
Test("C")

