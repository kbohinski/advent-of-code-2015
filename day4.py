import hashlib

inp = "ckczppom"

for i in range(0, 9999999):
    toHash = inp + str(i)
    toCompare = hashlib.md5(toHash.encode(('utf-8'))).hexdigest()
    if toCompare[:5] == "00000":
        print(i)
        break

for i in range(0, 9999999):
    toHash = inp + str(i)
    toCompare = hashlib.md5(toHash.encode(('utf-8'))).hexdigest()
    if toCompare[:6] == "000000":
        print(i)
        break