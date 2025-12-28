import hashlib

signature = 2466594619
E = 1329863093
N = 4900280003

def file_hash_4byte(filename):
    with open(filename, "rb") as f:
        data = f.read()
    h = hashlib.sha256(data).digest()
    return int.from_bytes(h[:4], "big")

verified_hash = pow(signature, E, N)
print("Verified hash:", verified_hash)

h1 = file_hash_4byte("ex2_file1.txt")
h2 = file_hash_4byte("ex2_file2.txt")

print("file1:", h1)
print("file2:", h2)
