"""
cryptography.py
Author: Kai Darrow
Credit: http://stackoverflow.com/questions/3391076/repeat-string-to-certain-length/3391142, Noah Cowey

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md

Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!

"""
def encrypt(x, y):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    output = []
    keyoutput = []
    for c in x:
        output.append(associations.find(c))
    for c in y:
        keyoutput.append(associations.find(c))
    for i in range(0,len(y)):
        output[i] = (output[i] + keyoutput[i])%len(associations)
    encrypted = []
    for n in output:
        encrypted.append(associations[n])
    return("".join(encrypted))
    
def decrypt(x, y):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    output = []
    keyoutput = []
    for c in x:
        output.append(associations.find(c))
    for c in y:
        keyoutput.append(associations.find(c))
    for i in range(0,len(y)):
        output[i] = (output[i] - keyoutput[i])%len(associations)
    encrypted = []
    for n in output:
        encrypted.append(associations[n])
    return("".join(encrypted))
    
x = 1
while x == 1:
    cmd = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
    if cmd == "e":
        message = input("Message: ")
        key = input("Key: ")
        messagenumber = len(message)
        keynumber = len(key)
        if messagenumber == keynumber: 
            x = 1
            print(encrypt(message, key))
        elif messagenumber > keynumber:
            newkey = key * messagenumber
            newkeytwo = newkey[0:messagenumber]
            x = 1
            print(encrypt(message, newkeytwo))
        else: 
            memes = key[0:messagenumber]
            print(memes)
            x = 1
            print(encrypt(message,memes))
    elif cmd == "d":
        message = input("Message: ")
        key = input("Key: ")
        messagenumber = len(message)
        keynumber = len(key)
        if messagenumber == keynumber: 
            x = 1
            print(decrypt(message,key))
        elif messagenumber > keynumber:
            newkey = key * messagenumber
            newkeytwo = newkey[0:messagenumber]
            print(decrypt(message,newkeytwo))
            x = 1
        else: 
            memes = key[0:messagenumber]
            x = 1
            print(decrypt(message,memes))

    elif cmd == "q":
        x = 0
        print("Goodbye!")

    else: 
        print("Did not understand command, try again.")
    

