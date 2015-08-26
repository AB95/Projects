

def encode(s, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    chars = list(s)
    for i, n in enumerate(chars):
        chars[i] = alphabet[(alphabet.find(n) + key) % len(alphabet)]
    return "".join(chars)


def decode(s, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    chars = list(s)
    for i, n in enumerate(chars):
        chars[i] = alphabet[(alphabet.find(n) - key) % len(alphabet)]
    return "".join(chars)

string = "Hello worl35"
print string
print encode(string, 8)
print decode(encode(string, 8), 8)