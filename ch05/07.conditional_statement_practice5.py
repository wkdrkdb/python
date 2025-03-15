# 문자열의 길이를 구하는 함수 len()
message = "Hello World!"
print(len(message))         # 12

id = input("사용하실 ID를 입력해주세요 >>> ")
password = input("사용하실 PASSWORD를 입력해주세요 >>> ")

if len(id) <= 10:
    if len(password) <= 10:
        print("회원가입을 성공하셨습니다.")
    else:
        print("비밀번호가 10자리를 초과했습니다.")
else:
    print("아이디가 10자리를 초과했습니다.")            

