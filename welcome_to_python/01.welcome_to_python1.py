import welcome_to_python_function as fc

"""
메인 메뉴
1. 회원가입
2. 로그인
3. 프로그램 종료
"""

user_id = ""
user_password = ""

while True:
    """
    <웰컴 투 파이썬!>
    1. 회원가입
    2. 로그인
    3. 프로그램 종료
    메뉴를 선택하세요 >>>
    """

    fc.print_menu("웰컴투 파이썬", ["회원가입", "로그인", "프로그램 종료"])
    user_input = input()

    if user_input == "1":
        user_id, user_password = fc.signup()
   

    
    elif user_input == "2":
        if user_id and user_password:     # 정상적으로 가입이 된 상태
            isLogged = fc.signin(user_id, user_password)
            if isLogged:
                user_id, user_password = fc.mypage(user_id, user_password)
        else:                             # 비정상적인 상태
            print("회원가입을 진행해주세요.")
    


    elif user_input == "3":
        break
    else: 
        print("메뉴를 다시 선택하세요\n")



print("==== 프로그램 종료 ====")

