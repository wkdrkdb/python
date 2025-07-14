"""
Set 특징
    순서가 없다 -> 실행할 때 마다 순서가 변경된다
    인덱싱되지 않는 컬렉션
    중복값 없다
    중괄호{} 사용
"""

thisset = {"피카츄", "라이츄", "파이리"}
print(thisset)

# 항목 가져오기 
for x in thisset:
    print(x)


# 값이 있는지 확인
print("피카츄" in thisset)
print("꼬부기" in thisset)


# add() 메소드 - 항목 추가하기
thisset.add("꼬부기")
thisset.add("피카츄")       # 중복으로 값이 추가되지 않는다 
print(thisset)

# update() 메소드 -다른 Set 항목 추가 
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"잠만보", "이브이", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)            # {'잠만보', '이브이', '파이리', '뮤츠', '라이츄', '피카츄'}


# remove() 메소드 - 항목 제거 
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset) 

# 없는 항목 선택시 에러발생 
# thisset.remove("잠만보") -> 에러!
# print(thisset) 

# discard() 메소드 - 에러발생 안 하는 항목제거 
thisset.discard("파이리")
print(thisset)          # {'라이츄'}

thisset.discard("잠만보")
print(thisset)          # {'라이츄'}  -> 에러발생 x 
 

result = thisset.pop()
print(result)
