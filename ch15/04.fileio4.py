# 뮤지컬 '황금별' 가사 중 특정 단어 카운팅하기

# (1) 파일 열기 

# (2) .readlines()로 데이터 읽기

# (3) count_star, count_king 변수 선언 + 초기화 

# (4) 반복문 사용해서 요소 순회하기 
#   (4-1) 요소에서 "왕"이라는 단어 찾기 -> count_king 1 증가
#   (4-2) 요소에서 "별"이라는 단어 찾기 -> count_star 1 증가

# print(f"왕 == {count_king}번, 별 == {count_star}번 입니다")

# (5) 파일 닫기


file = open('./황금별.txt', 'rt', encoding='utf-8')

lyrics_list = file.readlines()

count_star = 0
count_king = 0

# print(lyrics_list)

""" 방법(1)

for lyrics in lyrics_list:
    for word in lyrics:
        if word == "왕":
            count_king += 1

for lyrics in lyrics_list:
    for word in lyrics:
        if word == "별":
            count_star += 1

"""

for lyrics in lyrics_list:
    if "왕" in lyrics:
        count_king += 1

for lyrics in lyrics_list:
    if "별" in lyrics:
        count_star += 1


print(f"왕 == {count_king}번, 별 == {count_star}번 입니다")

file.close()