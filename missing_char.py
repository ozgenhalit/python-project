def missing_char(word, n) :
    word = list(word)
    for i in word :
        if 0<=n<len(word) :
            del word[n]
            word = "".join(word)
            return word
