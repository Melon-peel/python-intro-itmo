
file = open("short_hello.txt", mode="r", encoding="utf-8")
while True:
    a = file.readline()
    if a:
        print(a)
    else:
        break

print("-----")
# file = open("short_hello.txt", mode="r", encoding="utf-8")
for i in file:
    print(i)
else:
    file.close()
    print("closed!")