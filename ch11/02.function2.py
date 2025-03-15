"""
함수는 다양한 입력값(매개변수)를 받을 수 있으며,
입력값을 바탕으로 작업을 수행할 수 있다.

매개변수와(Parameter)와 인자(Argument)의 차이
    - 매개변수 : 함수 정의 시 함수가 입력받는 변수.
    - 인자 : 함수 호출 시 실제로 함수에 전달되는 값. 
"""

# 매개변수 있음, 리턴값 없음
def introduce(name, age):   # name = "홍길동", age = 25
    print(f"제 이름은 {name}이고, 나이는 {age}살입니다.")

introduce("킬릭진", 25)     # 제 이름은 킬릭진이고, 나이는 25살입니다. 


# 가변 매개변수 함수 - 여러개의 인자를 받을 수 있는 함수 
def show(*args):        # args는 가변 매개변수로, 함수가 받을 인자의 개수가 정해지지 않음 
    
    print(type(args))   # args는 튜플로 전달됨 

    for item in args:
        print(item)

show("Python")        
show("Python", "java", "C++") 

