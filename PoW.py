import string 
import random
import hashlib

size = 20

print("The Solution will be print in the terminal")
print("Solution of PoW of buda.com!!!")
print(".")
print("..")
print("...")
print("PoW start")

while(True):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = size))
    encoded=ran.encode()
    result = hashlib.sha256(encoded).hexdigest()
    if "b00da" in result:
        print("#################################################")
        print("Found one string that have the substring...")
        print("String: "+ran)
        print("Hash: "+result)
        print("#################################################")

