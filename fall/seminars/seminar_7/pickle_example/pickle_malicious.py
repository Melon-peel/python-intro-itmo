# class Example:
#     def __reduce__(self):
#         return (print, ("Hello from __reduce__!",))
#
#
#
# # Сериализация
# import pickle
# example = Example()
# with open("example.pkl", "wb") as f:
#     pickle.dump(example, f)
# # Десериализация
# with open("example.pkl", "rb") as f:
#     obj = pickle.load(f)  # При загрузке будет вызван print


#
#
#
# # -------
# #
#
# class Malicious:
#     def __reduce__(self):
#         import os
#         return (os.system, ("echo 'Hello, World!' > hello_world.txt",))
#
# import pickle
# malicious = Malicious()
# with open("totally_safe.pkl", "wb") as f:
#     pickle.dump(malicious, f)
#
#
import pickle
with open("totally_safe.pkl", "rb") as f:
    malicious_new = pickle.load(f)