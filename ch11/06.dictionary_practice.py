# 딕셔너리 -> 특정 키 값을 기준으로 데이터를 관리할 수 있기 때문에 사용합니다.

original_dict = {
                    "name" : "장가유", 
                    "numbers" : [1, 2, 3],
                    "job" : ["개발자", "학생", "강사"]
                }


# 딕셔너리의 얕은 복사
copy_dict = original_dict.copy()

# 복사본을 수정
copy_dict["name"] = "hyun"
copy_dict["numbers"].append(4)
copy_dict["job"].append("멘토")

print(original_dict)
print(copy_dict)


# 딕셔너리의 깊은 복사(리스트도 동일)
import copy

copy_dict2 = copy.deepcopy(original_dict)

copy_dict2["numbers"].append(5)
copy_dict2["job"].append("멘토")

print(original_dict)
print(copy_dict2)