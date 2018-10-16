# Ceaser Cipher script by CyberSy
# https://en.wikipedia.org/wiki/Caesar_cipher

# the string to be encrypted/decrypted:
message = input ('Enter your message: ')

# the encryption/decryptin key 
key = 1

# tells the program to encrypt or decrypt 
mode = 'encrypt' # set to "encrypt" or "decrypt"

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
        if mode == 'encrypt':
            num = num + key 
        elif mode == 'decrypt':
            num = num - key 

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

print(translated)
 