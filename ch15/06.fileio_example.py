# 파일 입출력 기본 - 실습문제(금칙어 필터링 프로그램)

# 금칙어 목록
filter_words = ['바보', '멍청이']

# 파일 열기 
with open('./금지어.txt', 'rt', encoding='utf-8') as file:
    # 파일 내용 읽기 
    content = file.read()
    print(type(content), content)

    # 금칙어 필터링 
    for word in filter_words:
        content = content.replace(word, '*' * len(word))

    # 필터링된 내용 출력
    print("< 필터링된 내용 >")
    print(content)

