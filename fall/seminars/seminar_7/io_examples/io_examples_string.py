import io

# f = open("multiline_file.txt", "r")
# print(f.read())
#
# print(f.readline())
# f.seek(0)
# print(f.readline())
#
# f.seek(0)
# print(f.readline())
# f.seek(0)
# print(f.readline())
#
#
# f = io.StringIO()
# f.write("hi")
# print(f.getvalue())
#
#
# # сейчас буфер указывает на начало
# print(f.tell())
# f.write("w")
# print(f.tell())
# f.seek(0)
# print(f.read())


# --------
# f = io.StringIO("abcdefg")
# f.seek(0, 2)  # перемещение в конец
# # # cookie = 0 - на сколько; whence = 1 - от начала файла, 2 - от конца файла
# f.write("h")
# f.write("i")
# f.seek(0)
# print(f.read())


#
# print(f.readline())
# чтобы прочитать от текущего положения буфера
# print(f.read())
# чтобы узнать обо всем контенте
# print(f.getvalue())


#
# # ---------
# # почему это полезно?
#
# #
result = ""
for i in range(1000):
    result = result + str(i)
    # result += str(i)  # Каждая операция создаёт новую строку
# # # ------------- vs . ----------
# #
buffer = io.StringIO()

for i in range(10000):
    buffer.write(str(i))  # Запись в существующий буфер
result = buffer.getvalue()
# # # ----------------------
