import string

ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypt = ""

word = input("Please input your word (preferably uppercase): ")
key = int(input("Please input your key [INTEGER]: "))

word = word.upper()

shift = input("type l for left shift, r for right shift: ")

if shift == "l":
    for i in word:
        if i in ab:
            #print(ab.index(i))
            #print((ab.index(i)+key)%25)
            encrypt = encrypt+ab[(ab.index(i)+key)%25]
    print(encrypt)        

elif shift == "r":
    for i in word:
        if i in ab:
            #print(ab.index(i))
            #print((ab.index(i)-key)%25)
            encrypt = encrypt+ab[(ab.index(i)-key)%25]
    print(encrypt)

else:
    print("Please input a proper response")
