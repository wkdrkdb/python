"""
Dictionary
    - key:value 쌍으로 이루어진 데이터 구조 
    - Key 순서가 없고, 변경 가능하며, 중복을 허용하지 않음
    - Value 모든 타입의 객체 저장 가능, 중복 가능, 수정 가능 
"""

# 딕셔너리 선언
thisdict =  {
                "brand" : "나이키",
                "model" : "Max90",
                "year" : "1990"
            }

# 값 가져오기 
print(f"브랜드: {thisdict['brand']}") 
print(f"모델: {thisdict['model']}") 
print(f"년도: {thisdict['year']}") 

print(thisdict)                                 # {'brand': '나이키', 'model': 'Max90', 'year': '1990'}

# 키 목록 가져오기  
print(f"키 목록 : {thisdict.keys()}")            # 키 목록 : dict_keys(['brand', 'model', 'year'])



# 항목 추가하기
thisdict["color"] = "red"
print(f"color 추가 후 : {thisdict}")              # color 추가 후 : {'brand': '나이키', 'model': 'Max90', 'year': '1990', 'color': 'red'}

thisdict.update({"bgcolor" : "black"})
print(f"bgcolor 추가 후 : {thisdict}")            # bgcolor 추가 후 : {'brand': '나이키', 'model': 'Max90', 'year': '1990', 'color': 'red', 'bgcolor': 'black'}



# 항목 수정하기
thisdict["brand"] = "나이스"
print(f"항목 수정하기 : {thisdict}")              # 항목 수정하기 : {'brand': '나이스', 'model': 'Max90', 'year': '1990', 'color': 'red', 'bgcolor': 'black'}



# 항목 제거하기
result = thisdict.pop("year")                    # 항목제거 pop('year') : {'brand': '나이키', 'model': 'Max90', 'color': 'red', 'bgcolor': 'black'}
print(f"항목제거 pop('year') : {thisdict}")       # result : 1990

del thisdict["bgcolor"]
print(f"del thisdict['bgcolor'] : {thisdict}")   # del thisdict['bgcolor'] : {'brand': '나이키', 'model': 'Max90', 'color': 'red'}



# 존재하지 않는 키 접근하기
# print(thisdict["age"])
print(thisdict.get("age", "키가 존재하지 않습니다."))
print("프로그램 종료")

# 딕셔너리 관련 함수들

print(len(thisdict))    # 키-값 쌍의 개수를 반환

# thisdict.clear()      전체 비워내는 함수
# print(thisdict)

new_dic = thisdict.setdefault("age", 0)
print(new_dic)
print(thisdict)

copy_thisdict = thisdict.copy()
print("아래는 복사된 딕셔너리 입니다.")
print(copy_thisdict)