class VignereCipher:
    #def __init__(self, word, key):
    #    self.word = word.upper()
    #    self.key = key.upper()

    def encrypt(word, key):
        ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypt = ""
        shift = 0
        word = word.upper()
        key = key.upper()
        for i in word:
            #print(i, key[word.index(i)%len(key)])
            shift = (ab.index(i)+ab.index(key[word.index(i)%len(key)]))%25
            #print(ab.index(i), ab.index(key[word.index(i)%len(key)]), shift)
            encrypt = encrypt + ab[shift]
        
        return encrypt
    


#word = input("Please input your word (preferably uppercase): ")
#key = input("Please input your key word: ")
#word = word.upper()
#key = key.upper()




#print(VignereCipher.encrypt('Jame','key'))
