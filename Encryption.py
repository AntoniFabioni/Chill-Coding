# Constructing and testing a message encryption system.

import hashlib

str = "Test"

result = hashlib.sha256(str.encode())

print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest())