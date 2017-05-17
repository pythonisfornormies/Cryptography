"""
cryptography.py
Author: Kai Darrow
Credit: http://stackoverflow.com/questions/3391076/repeat-string-to-certain-length/3391142

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
def encrypt(x):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    xspaced = " ".join(x)
    xlist = list(xspaced)
    for y in xlist:
        
def decrypt(x):
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    
    
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
            encrypt(message)
            print(message)
        elif messagenumber > keynumber:
            newkey = key * messagenumber
            newkeytwo = newkey[0:messagenumber]
            print(newkeytwo)
            x = 1
            encrypt(message)
            print(message)
        else: 
            memes = key[0:messagenumber]
            print(memes)
            x = 1
            encrypt(message)
            print(message)
    elif cmd == "d":
        message = input("Message: ")
        key = input("Key: ")
        messagenumber = len(message)
        keynumber = len(key)
        if messagenumber == keynumber: 
            x = 1
            decrypt(message)
            print(message)
        elif messagenumber > keynumber:
            newkey = key * messagenumber
            newkeytwo = newkey[0:messagenumber]
            print(newkeytwo)
            x = 1
            decrypt(message)
            print(message)
        else: 
            memes = key[0:messagenumber]
            print(memes)
            x = 1
            decrypt(message)
            print(message)

    elif cmd == "q":
        x = 0
        print("Goodbye!")

    else: 
        print("Did not understand command, try again.")
    

