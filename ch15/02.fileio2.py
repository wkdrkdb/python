import time

try:
    # 2024-11-02.txt 형식으로 파일명 작성하는 방법
    file = open(time.strftime('%Y-%m-%d') + '.txt', 'at', encoding='utf-8')

    # 오늘의 스케쥴 입력 
    while True:
        schedule = input("오늘의 스케쥴을 입력하세요 >>> ")

        # 조건문: 사용자가 아무것도 입력하지 않으면 루프 탈출 
        if not schedule:
            break
        
        file.write(schedule + '\n')


except Exception as exception:
    print(type(exception), exception)

else:
    file.close()

print("---- 프로그램 종료 ----")

