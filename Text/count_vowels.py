

def count_vowels(s):
    count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for i in s:
        if i in count:
            count[i] += 1

    return count