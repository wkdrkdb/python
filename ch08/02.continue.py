"""
continue 
    while문이나 for문과 같은 반복문을 강제로 건너뛰게 한다.
"""

total = 0
for a in range(1, 101):
    if a % 3 == 0:              # a가 3의 배수일 때 건너뛰기 
        continue
    total += a 
    
    
    print(f"a: {a}, total: {total}")                    # f-string
    # print("a: {}, total: {}".format(a, total))        # str.format() 메서드 기능
    # print("a: %s, total: %s" % (a, total))            # formatting