file = open('./2024-11-02.txt', 'rt', encoding='utf-8')

content = file.read()

print(content)

file.close()


# ---------------------
print()

file = open('./2024-11-02.txt', 'rt', encoding='utf-8')

while True:
    content = file.read(5)
    if not content:
        break
    print(content, end='')

file.close()


# --------------------
print()

file = open('./2024-11-02.txt', 'rt', encoding='utf-8')

while True:
    content = file.readline() # 한 줄씩 읽어서 처리
    if not content:
        break
    print(content, end='')

file.close()


# --------------------
print()

file = open('./2024-11-02.txt', 'rt', encoding='utf-8')

content_list = file.readlines()
for index, content in enumerate(content_list, start=1):
    print(f"{index}.{content}", end='')

