origin_password = "aaa123"
input_password = input("비밀번호를 입력해주세요 >>> ")

if input_password == "":                    # 비밀번호를 입력하지 않았을 때     
    print("비밀번호를 입력해주세요.")
elif input_password == origin_password:     # 비밀번호가 일치할 때 
    print("비밀번호가 일치합니다!")       
else:                                       # 비밀번호가 일치하지 않을 때 
    print("비밀번호가 불일치합니다!")       
