class CaesarCipher:

    def encrypt(word, key, shift):
        ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypt = ""
        word = word.upper()
        if shift == "l":
            for i in word:
                if i in ab:
                    #print(ab.index(i))
                    #print((ab.index(i)+key)%25)
                    encrypt = encrypt+ab[(ab.index(i)+key)%25]
            return encrypt        

        elif shift == "r":
            for i in word:
                if i in ab:
                    print(ab.index(i))
                    #print((ab.index(i)-key)%25)
                    encrypt = encrypt+ab[(ab.index(i)-key)%25]
            return encrypt

        else:
            return "Please input a proper response"



#word = input("Please input your word (preferably uppercase): ")
#key = int(input("Please input your key [INTEGER]: "))
#shift = input("type l for left shift, r for right shift: ")

print(CaesarCipher.encrypt('Jame', 3, 'l'))
