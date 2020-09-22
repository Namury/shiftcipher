# Nama  : Nazmi M Abkary
# NPM   : 140810180037
# Kelas : B

def switch():
    print("Shift Cipher")
    text = input("Enter string: ")
    shift = int(input("Enter shift number: "))
    
    print('')
    print("1. Encrypt")
    print("2. Decrpyt")
    i = int(input("Input: "))
    print('')

    def encrypt():
 
        cipher = ''
        for char in text: 
            if char == ' ':
                cipher = cipher + char
            elif  char.isupper():
                cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
        
        print("After encryption: ", cipher)

    def decrypt():

        cipher = ''
        for char in text:
            if char == ' ':
                cipher = cipher + char
            elif char.isupper():
                cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97) 
        print("After decryption: ", cipher)

    def default():
        print("Incorrect option")

    dict = {
        1 : encrypt,
        2 : decrypt,

    }
    dict.get(i,default)()

switch()