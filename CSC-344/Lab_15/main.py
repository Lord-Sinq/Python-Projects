import math

n = 493
e = 33
d = 17
q = 29

myStr = "Hello world!"
cipherText = []
cipher = []
print(myStr)
for i in myStr:
    cipherText.append(ord(i) **e %n)
print(cipherText)

for i in cipherText:
    cipher.append(chr(i **d %n))
print(cipher)

# 1. key size says 2048
# 2. the e = 65537