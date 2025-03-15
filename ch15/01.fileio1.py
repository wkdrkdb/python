# 텍스트 파일 생성하기
file = open('./data/hello.txt', 'wt', encoding='utf-8')

# '안녕하세요', '반갑습니다'
file.write('안녕하세요.')
file.write('반갑습니다.')

# 파일 닫기
file.close()

print("hello.txt 파일이 생성되었습니다.")

#---------------------------------------------------------------------

# 새로운 내용 작성(추가)
file = open('./data/hello.txt', 'at', encoding='utf-8')
file.write('제 이름은 옥순입니다.')
file.close()

print("hello.txt 내용이 추가되었습니다.")


#---------------------------------------------------------------------

# 현재 위치는 pyhon39입니다 상대경로를 사용해서 파일을 생성하세요.
# 1. folder1 하위에 apple.txt 파일 생성하세요.
# 2. folder2 하위에 orange.txt 파일 생성하세요.
# 3. 파일의 내용은 둘다 동일하게 'hello world!'를 작성하세요.

file = open('./folder1/apple.txt', 'wt', encoding='utf-8')
file.write('hello world!')
file.close()

file = open('./folder2/orange.txt', 'wt', encoding='utf-8')
file.write('hello world!')
file.close()


