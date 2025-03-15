# with 문

with open('./hello.txt', 'at', encoding='utf-8') as file:
    file.write('처음 뵙겠습니다.\n')
    print("hello.txt 파일에 새로운 내용이 작성되었습니다.")

import sys 

with open('./hello.txt', 'rt', encoding='utf-8') as file:
    # 기본적인 읽기 방법
    content = file.read()
    print(content)

    # sys 모듈 사용하기
    sys.stdout.writelines(content)