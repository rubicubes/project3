def shift(k, text):
    res = ""
    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c)-97 + k) % 26 + 97)
        else:
            res += c
    return res

with open("ex3.txt", "r") as f:
    cipher = f.read()

for k in range(26):
    print(k, shift(-k, cipher))
