from hashlib import sha256 # Import Hashlib Library with the SHA-256 Hash Algorithm

h = sha256()

h.update(b'EastBlueTradingCo') # The string is the text that is going to be converted to a Hash

hash = h.hexdigest() # Gets output of Hash Function 

print(hash) # Prints the SHA-256 Hash to the treminal 