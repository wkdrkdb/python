from user import User
from helpers import *

FILE_PATH = './data/user.json'


def save_user(user: User):
    """
    이 함수는 사용자 정보를 저장합니다.
    """

    # USER 객체를 JSON 형식으로 저장하는 함수
    try: 
        data = load_data_fromjson(FILE_PATH) 
    except FileNotFoundError:
        data = []

    # 사용중인 아이디인지 검사 
    for user_data in data:
        if user_data['id'] == user.id:
            print(f'{user.id}는 이미 사용중인 아이디입니다.')
            return
        
    # user 리스트에 딕셔너리로 변환된 데이터 추가    
    data.append(user.__dict__)

    # 저장
    save_data_tojson(FILE_PATH, data)
    print(f'{user.name}님의 정보가 저장되었습니다.')

# --------------------------------------------------------------------------------------------------

def login_user(id: str, password: str):
    from screen import open_mypage_window
    """
    이 함수는 사용자 정보를 조회합니다.
    """
    data = load_data_fromjson(FILE_PATH)

    for user_data in data:
        # id 와 password가 일치하는 딕셔너리 찾기
        if (id == user_data['id']) and (password == user_data['password']):
            print(f'{user_data['name']}님, 환영합니다!')
            # 마이페이지 실행 
            open_mypage_window()
            return
        
    print('사용자 정보가 일치하지 않습니다.')

# --------------------------------------------------------------------------------------------------

def delete_user(id: str, password: str):
    """
    이 함수는 사용자 정보를 삭제합니다.
    """
    data = load_data_fromjson(FILE_PATH)

    for user_data in data:
        # 매개변수로 전달받은 id와 password가 일치하는 
        # user_data를 삭제합니다.
        if (id == user_data['id']) and (password == user_data['password']):
            # 받아온 리스트에서 해당 딕셔너리 삭제
            data.remove(user_data)
            save_data_tojson(FILE_PATH, data)
            print(f'{user_data['name']}님의 정보가 삭제되었습니다.')
            return