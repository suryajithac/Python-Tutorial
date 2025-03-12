def modify_string(s):
    if ' ' in s:
        return s.replace(' ', 'or')
    else:
        return 'S' + s + 'S'