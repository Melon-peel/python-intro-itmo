# будет работать
# some_list = ["a", "b", "c", "d"]
#
# for i, _ in enumerate(some_list, start=0):
#     pass

# # -----------
# # вызовет ошибку


try:
    1 / 0
except ZeroDivisionError as e:
    print(e)  # если хочется переиспользовать переменную, присвойте нелокализуемое значение
print(e)

# # ---------
# # например, так

# # try:
# #     1 / 0
# # except ZeroDivisionError as e:
# #     print(e)
# #     new_e = e
# # print(new_e)
