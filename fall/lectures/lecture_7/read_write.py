
my_file = open("write_hello.txt", "w")

for i in range(3):
    my_file.write("string 1\n")
my_file.close()