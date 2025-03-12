def remove_words(s, words):
    word_list = s.split()
    new_list = [word for word in word_list if word not in words]
    return " ".join(new_list)