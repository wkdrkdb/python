from user import User
from auth_service import *

def sign_up(id, password, email, name):
    """
    사용자 정보를 입력받아 저장하는 함수
    """

    try:
         # 사용자 객체 생성
        user = User(id , password, email, name)

        save_user(user)

    except ValueError as exception:
        print(f"사용자 정보 저장 실패: {exception}")



def sign_in(id: str, password: str):
    """
    사용자 정보를 입력받아 인증하는 함수 
    """

    # 아이디와 비밀번호가 입력됐는지 검사
    if id and password:
        login_user(id, password)



def drop(id: str, password: str):
    """
    사용자 정보를 입력받아 삭제하는 함수 
    """
 
    if id and password:
        delete_user(id, password)



if __name__ == '__main__':
    # sign_up() 
    # sign_in()
    drop()
