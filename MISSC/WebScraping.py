# dic1 = {"513R":["951L","513P","779Q"]}
# dic2 = {"513P":["951L","822Q","779Q"]}
# key = list(dic2.keys())[0] # get the first key of dict2
# if key in dic1["513R"]: # check if the key is in the list of values of dict1
#     print(True)
# else:
#     print(False)


dic1 = {"513R": ["951L", "513P", "779Q"]}
dic2 = {"513P": ["524S", "822Q", "147L"]}
items1 = dic1.items()
items2 = dic2.items()
for key1, value1 in items1:
    for key2, value2 in items2:
        if key2 in value1:
            new = {*value1, *value2}
            dic1[key1] = new
            print(dic1.items())
        else:
            print(False)
