origin_id = "tester"
origin_password = "1234"

input_id = input("사용하실 ID를 입력해주세요 >>> ")
input_password = input("사용하실 PASSWORD를 입력해주세요 >>> ")

if input_id == origin_id:
    if input_password == origin_password:
        print("로그인에 성공하셨습니다")
    else:
        print("비밀번호를 확인해주세요.")
else:
    print("아이디를 확인해주세요")            