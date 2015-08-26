

def pig_latin(s):
    s = s.lower()
    index = len(s)
    ending = ""
    vowels = {"a", "e", "i", "o", "u"}
    for i, j in enumerate(s):
        if j not in vowels:
            ending += j
        else:
            index = i
            break

    if ending:
        ending += "ay"
    else:
        ending = "yay"

    return s[index:] + ending