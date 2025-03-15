import tkinter as tk

def create_screen(title: str):
    """
    이 함수는 화면을 생성하는 함수입니다.
    """
    GEOMETRY = "500x600" 

    root = tk.Tk()
    root.title(title)
    root.geometry(GEOMETRY)

    return root

def test():
    print("test함수가 실행되었습니다.")


def open_program_menu():
    """
    이 함수는 프로그램 메인 메뉴 화면을 실행하는 함수입니다.
    """
    program_menu = create_screen('프로그램 메뉴')

    # 회원가입 버튼 정의
    button_signup = tk.Button(
        program_menu, 
        text="회원가입",
        command=lambda: open_signup_window()
    )

    # 버튼 생성
    button_signup.pack(pady=20)

    # 로그인 버튼 정의
    button_login = tk.Button(
        program_menu,
        text="로그인",
        command=lambda: open_login_window()
    )

    # 버튼 생성
    button_login.pack(pady=20)
    program_menu.mainloop()

    return True

#=============================================================================

def open_signup_window():
    from auth_menu import sign_up
    """
    이 함수는 회원가입 화면을 출력하는 함수입니다.
    """
    signup_window = create_screen('회원가입')

    # 아이디
    label_id = tk.Label(signup_window, text='아이디를 입력하세요.') # 라벨 정의
    label_id.pack(pady=20) # 라벨 생성
    entry_id = tk.Entry(signup_window)
    entry_id.pack(pady=20) 

    # 비밀번호
    label_password = tk.Label(signup_window, text='비밀번호를 입력하세요.') # 라벨 정의
    label_password.pack(pady=20) # 라벨 생성
    entry_password = tk.Entry(signup_window)
    entry_password.pack(pady=20) 

    # 이름
    label_name = tk.Label(signup_window, text='이름을 입력하세요.') # 라벨 정의
    label_name.pack(pady=20) # 라벨 생성
    entry_name = tk.Entry(signup_window)
    entry_name.pack(pady=20) 

    # 이메일
    label_email = tk.Label(signup_window, text='이메일을 입력하세요.') # 라벨 정의
    label_email.pack(pady=20) # 라벨 생성
    entry_email = tk.Entry(signup_window)
    entry_email.pack(pady=20) 

    # 확인 버튼
    button_frame = tk.Frame(signup_window)
    button_frame.pack(pady=20)
    
    button_ok = tk.Button(
        button_frame,
        text='확인',
        command=lambda: sign_up(
            id = entry_id.get(),
            password = entry_password.get(),
            email = entry_email.get(),
            name = entry_name.get()
        )
    )
    button_ok.pack(side='left', pady=20)

    # 닫기 버튼
    button_cancel = tk.Button(
        button_frame,
        text='취소',
        command=lambda: signup_window.destroy()
    )
    button_cancel.pack(side='left', pady=20)

    signup_window.mainloop()

#=============================================================================

def open_login_window():
    from auth_menu import sign_in
    """
    이 함수는 로그인 화면을 출력하는 함수입니다.
    """
    # 로그인 화면 생성
    login_window = create_screen('로그인')

    # 아이디 입력
    label_id = tk.Label(login_window, text='아이디를 입력하세요.') # 라벨 정의
    label_id.pack(pady=20) # 라벨 생성
    entry_id = tk.Entry(login_window)
    entry_id.pack(pady=20)     

    # 비밀번호 입력
    label_password = tk.Label(login_window, text='비밀번호를 입력하세요.') # 라벨 정의
    label_password.pack(pady=20) # 라벨 생성
    entry_password = tk.Entry(login_window)
    entry_password.pack(pady=20) 

    # 확인 버튼
    button_frame = tk.Frame(login_window)
    button_frame.pack(pady=20)

    button_ok = tk.Button(
        button_frame,
        text='확인',
        command=lambda: sign_in(
            id = entry_id.get(),
            password = entry_password.get()
        )
    )
    button_ok.pack(side='left', pady=20)    

    # 닫기 버튼 
    button_cancel = tk.Button(
        button_frame,
        text='취소',
        command=lambda: login_window.destroy()
    )
    button_cancel.pack(side='left', pady=20)    

    # 화면 실행 함수 호출
    login_window.mainloop()

#=============================================================================

def open_mypage_window():
    from create_number import create_lotto_numbers

    mypage_window = create_screen('마이페이지')

    # 로또 발송버튼 (로또 번호 생성해서 이메일 발송하기)
    button_lotto = tk.Button(
        mypage_window,
        text='로또 번호 이메일 발송',
        command=lambda: create_lotto_numbers()
    )
    button_lotto.pack(pady=20)

    # 날씨 검색 버튼
    """
    geocoding_service.py 의 get_weather_search_open()
    """

    button_weather_search = tk.Button(
        mypage_window,
        text='날씨 검색',
        command=lambda: open_weather_search_window()
    )
    button_weather_search.pack(pady=20)


    # 회원탈퇴 버튼
    button_drop = tk.Button(
        mypage_window,
        text='회원 탈퇴',
        command=lambda: open_drop_window()
    )
    button_drop.pack(pady=20)

    # 닫기 버튼 
    button_cancel = tk.Button(
        mypage_window,
        text='취소',
        command=lambda: mypage_window.destroy()
    )
    button_cancel.pack(pady=20)       


    mypage_window.mainloop()

#=============================================================================

def open_drop_window():
    from auth_menu import drop

    drop_window = create_screen('회원탈퇴')

    # 아이디 입력
    label_id = tk.Label(drop_window, text='아이디를 입력하세요.') # 라벨 정의
    label_id.pack(pady=20) # 라벨 생성
    entry_id = tk.Entry(drop_window)
    entry_id.pack(pady=20)     

    # 비밀번호 입력
    label_password = tk.Label(drop_window, text='비밀번호를 입력하세요.') # 라벨 정의
    label_password.pack(pady=20) # 라벨 생성
    entry_password = tk.Entry(drop_window)
    entry_password.pack(pady=20) 

    # 확인 버튼
    button_frame = tk.Frame(drop_window)
    button_frame.pack(pady=20)

    button_ok = tk.Button(
        button_frame,
        text='확인',
        command=lambda: drop(
            id = entry_id.get(),
            password = entry_password.get()
        )
    )
    button_ok.pack(side='left', pady=20)    

    # 닫기 버튼 
    button_cancel = tk.Button(
        button_frame,
        text='취소',
        command=lambda: drop_window.destroy()
    )
    button_cancel.pack(side='left', pady=20)    

    drop_window.mainloop()


# 날씨 검색 화면
def open_weather_search_window():
    from geocoding_service import get_geocoding_data
    weather_search_window = create_screen("날씨 조회")
    label_city = tk.Label(weather_search_window, text='지역을 입력하세요.')
    label_city.pack(pady=20)
    entry_city = tk.Entry(weather_search_window)
    entry_city.pack(pady=20)

    button_frame = tk.Frame(weather_search_window)
    button_frame.pack(pady=20)

    # 확인
    button_ok = tk.Button(
        button_frame,
        text='확인',
        command=lambda: get_geocoding_data(
            entry_city.get()
            )
    )
    button_ok.pack(side='left', pady=20) 

    # 취소 
    button_cancel = tk.Button(
        button_frame,
        text='취소',
        command=lambda: weather_search_window.destroy()
    )
    button_cancel.pack(side='left', pady=20)


# 날씨 결과 화면 
def open_weather_result_window(temp: str, feels_like: str, humidity: str):
    weather_result_window = create_screen("날씨 결과")
    label_city = tk.Label(weather_result_window, text='현재 날씨 정보')
    label_city.pack(pady=20)
    label_city = tk.Label(weather_result_window, text=f'현재 온도: {temp}도 ')
    label_city.pack(pady=20)
    label_city = tk.Label(weather_result_window, text=f'체감 온도: {feels_like}도')
    label_city.pack(pady=20)
    label_city = tk.Label(weather_result_window, text=f'현재 습도: {humidity}%')
    label_city.pack(pady=20)

    button_cancel = tk.Button(
        weather_result_window,
        text='취소',
        command=lambda: weather_result_window.destroy()
    )
    button_cancel.pack(pady=20)

    weather_result_window.mainloop()

if __name__ == "__main__":
    open_program_menu() 