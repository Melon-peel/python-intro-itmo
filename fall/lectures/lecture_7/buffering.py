file = open("short_hello.txt", mode="r", encoding="utf-8")

print(file.read())
print(file.tell())
print(file.buffer.tell())

print(file.read() == "")
# print(file.tell())
# print(file.buffer.tell())
# print('----')
# print(file.readline())
# print(file.tell())
# print(file.buffer.tell())
# print(file.tell())
# print(file.readline())
# print(file.buffer.tell())