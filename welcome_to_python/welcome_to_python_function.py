def print_menu(title: str, menus: list):    
    """
    메뉴를 출력하는 함수 
    """
    print(f"<{title}>")
    for index, menu in enumerate(menus, start=1):
        print(f"{index}.{menu}")
    print("메뉴를 선택하세요 >>> ", end=" ")


def signup() -> tuple: 
    """
    회원가입 처리를 하는 함수
    """
    user_id  = input("아이디를 입력하세요 >>> ")
    user_password = input("비밀번호를 입력하세요 >>> ")
    # 아이디가 이메일 형식인지 유효성 체크하기  
    if ("@" in user_id) and user_password:
        print("회원가입이 완료되었습니다!")
        return user_id, user_password
    else:
        print(f"아이디와 비밀번호를 확인해주세요. (ID: {user_id}, PW: {user_password})")    
        return "", ""
    

def signin(user_id:str, user_password:str) -> bool:
    """
    로그인 처리하는 함수
    """
    input_id = input("아이디를 입력하세요 >>> ")
    input_password = input("비밀번호를 입력하세요 >>> ")
    if user_id == input_id and user_password == input_password:
        print("로그인 되었습니다!")
        return True
    else:
        print("아이디 또는 비밀번호를 확인해주세요.")
        return False  


def mypage(user_id: str, user_password: str) -> tuple:
    """
    마이페이지 실행하는 함수
    """
    while True:
        print_menu("마이페이지", ["회원정보", "회원탈퇴", "홈으로"])
        user_input = input()

        if user_input == "1":
            print(f"회원님의 아이디: {user_id}, 비밀번호: {user_password}입니다.")
        elif user_input == "2":
            print("회원탈퇴가 완료되었습니다!")
            return "", ""
        elif user_input == "3":
            break
        else:
            print("메뉴를 다시 선택해주세요.\n")      
    return user_id, user_password       