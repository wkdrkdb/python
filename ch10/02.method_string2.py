# join() 메소드
s = "-".join("python")
print(s)                    # p-y-t-h-o-n

s = "+".join(['a', 'b', 'c', 'd', 'e'])
print(s)                    # a+b+c+d+e

s = "".join(['a', 'b', 'c', 'd', 'e'])
print(s)                    # abcde


# split() 메소드
s = "Life is to short"
result = s.split()
print(result)               # ['Life', 'is', 'to', 'short']     

s = '010-1234-5678'
result = s.split("-")
print(result)               # ['010', '1234', '5678']

print(f"{result[0]}-****-{result[2]}")

data = "프로그래머|25|서울"
result = data.split('|')
print(result)               # ['프로그래머', '25', '서울']

print(f"직업: {result[0]}") # 직업: 프로그래머
print(f"나이: {result[1]}") # 나이: 25
print(f"주소: {result[2]}") # 주소: 서울


# replace() 메소드 - 문자열 치환
s = "life is too short"
result = s.replace("short", "long")
print(result)              # life is too long

# strip(), lstrip(), rstrip() 공백제거 메소드 
s = "     apple"
result = s.lstrip()    # 왼쪽 공백 제거 
print(result)

s = "apple     "
result = s.rstrip()    # 오른쪽 공백 제거
print(result)

s = "     a p p l e     "
result = s.strip()     # 양쪽 공백 제거 
print(result)          # a p p l e


s = "     a p p l e     "
result = s.replace(" ", "")
print(result)          # apple
