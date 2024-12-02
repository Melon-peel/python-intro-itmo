# try:
#     my_file = open("write_hello.txt", "r")
# except Exception:
#     print("Excepted!")
# finally:
#     print("anyway...")
#     my_file.close()
#

with open("short_hello.txt", "r") as f:
    lines = f.readlines()

print(lines)
f.read()