import pickle

some_dict = {"a": 1, "b": 2, "c": 3}

with open("some_dict.pickle", "wb") as f:
    pickle.dump(obj=some_dict, file=f)

with open("some_dict.pickle", "rb") as f:
    read_dict = pickle.load(f)
    print(read_dict)

