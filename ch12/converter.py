# 대문자 변수는 상수이다.
MILES = 0.621371
POUND = 0.00220462

def kilometer_to_miles(kilometer):
    return kilometer * MILES

def gram_to_pounds(gram):
    return gram * POUND

print(kilometer_to_miles(10))