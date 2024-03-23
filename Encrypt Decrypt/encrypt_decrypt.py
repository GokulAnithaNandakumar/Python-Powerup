def Encrypt(file):
    f = open("hello.txt", "r")
    content = f.read()

    key = int(input("Enter the key : "))

    encrypt = ""

    for ch in content:
        if ch.islower():
            encrypt += chr(ord('a')+((ord(ch)+key-ord('a'))%26))
        elif ch.isupper():
            encrypt += chr(ord('A')+((ord(ch)+key-ord('A'))%26))
        elif ch.isdigit():
            encrypt += str((int(ch)+key)%10)
        else:
            encrypt += ch

    print(encrypt)

    with open("hello.txt", "w") as f:
        f.write(encrypt)

def Decrypt(file):    
    f = open(file, "r")
    content = f.read()

    key = int(input("Enter the key : "))

    decrypt = ""

    for ch in content:
        if ch.islower():
            decrypt += chr(ord('a')+((ord(ch)-key-ord('a'))%26))
        elif ch.isupper():
            decrypt += chr(ord('A')+((ord(ch)-key-ord('A'))%26))
        elif ch.isdigit():
            decrypt += str((10+int(ch)-key)%10)
        else:
            decrypt += ch

    print(decrypt)

    with open("hello.txt", "w") as f:
        f.write(decrypt)

Decrypt("hello.txt")