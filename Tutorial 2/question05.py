def slice_string(s):
    odd_chars = ""
    even_chars = ""
    for i in range(len(s)):
        if i % 2 == 0:
            odd_chars += s[i]
        else:
            even_chars += s[i]
    return odd_chars, even_chars