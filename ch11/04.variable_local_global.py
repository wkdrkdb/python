"""
지역변수(Local Variable)
    - 함수 내부에서 선언된 변수로, 해당 함수 안에서만 사용가능.
    - 함수가 종료되면 해당 변수는 소멸된다.

전역변수(Global Variable)
    - 함수 외부에서 선언된 변수로, 프로그램 전체에서 사용가능.
    - 함수 내부에서도 사용할 수 있지만, 함수 내부에서 전역변수를 변경하려면
      "global" 키워드를 사용해야 한다.
"""

# 전역변수 선언 
gVar = "전역"

def globalAndLocal():
    # 지역변수 선언
    lVar = "지역"

    print(f"{gVar}변수입니다.")
    print(f"{lVar}변수입니다.")



def globalAndLocal2():
    # 다른 함수의 지역변수는 공유되지 않음 
    lVar2 = "지역2"         # 새로운 lVar 지역변수 

    print(f"{gVar}변수입니다.")
    print(f"{lVar2}변수입니다.")
    


# 함수 호출
globalAndLocal()    
globalAndLocal2()    


def globalAndLocal3():
    lVar = "지역"

    gVar = "변경된 전역이 아닌 새로운 지역"  

    print(f"{gVar}변수입니다.")         # 변경된 전역이 아닌 새로운 지역변수입니다.   -> 함수 안에서는 이름이 같은 경우 지역변수를 우선 호출
    print(f"{lVar}변수입니다.")


print("==========================================================================")

globalAndLocal3()

print(f"gVar : {gVar}")  # 전역 



def globalAndLocal4():
    lVar = "지역"

    global gVar 
    gVar = "전역4"  

    print(f"{gVar}변수입니다.")        
    print(f"{lVar}변수입니다.")

print("==========================================================================")

globalAndLocal4()

print(f"gVar : {gVar}")  # 전역4