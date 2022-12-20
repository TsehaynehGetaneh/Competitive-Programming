def swap_case(s):
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i].islower():
            list_s[i] = list_s[i].upper()
        elif list_s[i].isupper():
            list_s[i] = list_s[i].lower()
    return ''.join(list_s)
