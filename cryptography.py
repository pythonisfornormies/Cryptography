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
def cyc(sg, lngth):
    a, b = 1, sg
    while len(sg) < lngth:
        sg += b[a - 1]
        a = (a+1)%len(b)
    return sg
    
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
x = 1
while x == 1:
    cmd = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
    if cmd == "e":
        message = input("Message: ")
        key = input("Key: ")
        messagenumber = message.count()
        keynumber = key.count()
        if messagenumber == keynumber: 
            x = 1
        else:
            cyc(key, messagenumber)
            print(key)
    elif cmd == "d":
        print("g")

    elif cmd == "q":
        x = 0
        print("Goodbye!")

    else: 
        print("Did not understand command, try again.")
    

