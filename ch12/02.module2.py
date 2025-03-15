"""
모듈 사용법
    from 모듈명 import 함수
    from 모듈명 import 함수1, 함수2
    from 모듈명 import *       
"""

from converter import kilometer_to_miles, gram_to_pounds

miles = kilometer_to_miles(150)
print(f"150km = {miles}miles")

pounds = gram_to_pounds(1000)
print(f"1000gram = {pounds}pounds")


