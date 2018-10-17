#    Ceaser Cipher script by CyberSy
# https://en.wikipedia.org/wiki/Caesar_cipher

# the string to be encrypted/decrypted:
message = input ('Enter your message: ')

# the encryption/decryptin key 
key = input ("Enter The Encryption Key: ")

# tells the program to encrypt or decrypt 
print (" [+] Chose a Mode: \n [1] Encrypt \n [2] Decrypt ")
mode = input ("Enter The Mode: ") # set to "encrypt" or "decrypt"

# every possible symbol that can be encrypted 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message 
message = message.upper()
    
# run the encryption/decryption code on each words in the message string 
for words in message:
    if words in LETTERS:
        # get the encrypted (or decrypted) number for this words
        num = LETTERS.find(words) # get the number of the words
        if mode == 'Encrypt':
            num = num + int(key)
        elif mode == 'Decrypt':
            num = num - int(key) 

        # handle the warp-around if num i larger than the length of 
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)    
        elif num < 0:
            num = num + len(LETTERS)
        
        # add encrypted/decrypted number's words at the end of translated 
        translated = translated + LETTERS[num]

    else:
         # just add the words without encryption/decryption 
         translated = translated + words

print("[+] Your Encrypted Message Is: " + translated)
