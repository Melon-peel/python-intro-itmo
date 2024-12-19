# для получения системной кодировки (используется при чтении/записи по умолчанию)
import locale

print(locale.getpreferredencoding())

# -------------
# пример вызовет ошибку, т.к. чтение скорее всего происходит в кодировке, отличнеой от cp1251 (windows-1251)

# with open("cp1251file.txt", "w", encoding="cp1251") as f:
#     f.write("Запись в такой-то кодировке! Hell yeah")


# with open("cp1251file.txt", "r") as f:
#     print(f.read())

# ----------------
# текстовый файл можно считать и бинарно

with open("cp1251file.txt", "rb") as f:
    content = f.read()

# и кастануть в другую кодировку
# print(content)
# print(content.decode("cp1251").encode("utf-8"))

# может вызвать ошибку, если content не в utf-8
print(content.decode("utf-8"))

# исправление кодировки исходного файла и запись в нужной
with open("cp1251file.txt", "wb") as f:
    utf_8_content = content.decode("cp1251").encode("utf-8")
    f.write(utf_8_content)

