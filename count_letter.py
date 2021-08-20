def countChar(text):
    dict = {}
    for i in text:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(countChar('love of my life'))
