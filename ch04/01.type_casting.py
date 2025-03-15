# 자료형 변환
# 변수의 타입 확인하는 방법
#   type() 을 사용하면 변수의 자료형을 확인할 수 있음

number_value = 1
string_value = "String"
float_value = 1.0

type(number_value)
type(string_value)
type(float_value)

print("number_value 타입 =", type(number_value))
print("string_value 타입 =", type(string_value))
print("float_value 타입 =", type(float_value))



# 정수형으로 변환하기 
#   "정수형으로 변환이 가능한 데이터"를 정수형으로 형변환하는 방법은 입력받은 데이터를 int()로 감싸줍니다.
string_value = "10"
int_value = int(string_value)
print("string_value = ", type(string_value), "int_value = ", type(int_value))

#True = 1, False = 0
bool_value = int(True)          
print("bool_value 타입 = ", type(bool_value), "bool_value 값 = ", bool_value)



# 실수형으로 변환하기
#   "실수형으로 변환이 가능한 데이터"를 실수형으로 형변환 하는 방법은 입력받은 데이터를 float()로 감싸줍니다.
float_value = float("10.0")
print(type(float_value), float_value)



# 문자형으로 변환하기 
#   입력받은 데이터를 str()로 감싸줍니다.
str_value = str(10)
print(type(str_value), str_value + "10")


