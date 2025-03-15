"""
chr() 함수
    특정문장의 유니코드 값을 전달하면
    해당 유니코드의 값을 가진 문자로 반환  

ord() 함수
    반대로 문자를 전달하면 유니코드 값 반환 
"""

result = chr(65)
print(f"chr(65) : {result}")

result = ord("A")
print(f"ord('A') : {result}")

result = ord(" ")
print(f"ord(' ') : {result}")
