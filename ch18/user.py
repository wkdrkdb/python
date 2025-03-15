class User:
    def __init__(self, id: str, password: str, email: str, name: str):

        # 1. 이메일 정합성 검사
        if '@' not in email or '.' not in email:
            raise ValueError('이메일 형식이 올바르지 않습니다.')

        # 2. 비밀번호 정합성 검사(New!!)
        has_digit = False
        has_alpha = False   # 숫자 또는 문자가 포함되어 있으면 True 로 변경 

        for char in password:
            if char.isalpha():
                has_alpha = True
            if char.isdigit():
                has_digit = True

        if not has_alpha or not has_digit:
            raise ValueError('비밀번호는 영어와 숫자의 조합이어야 합니다.')            

        # 3. 아이디 정합성 검사(New!!)
        if not id:
            raise ValueError('아이디는 필수입니다.')



        self.id = id
        self.password = password
        self.email = email 
        self.name = name 
