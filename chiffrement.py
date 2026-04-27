# logique
def Logique(data,key=3,decode=False):
    crypted =""
    if decode:
        key = -key
    for letter in data.upper():
        if letter.isalpha():
            ascii_value = ord(letter) - ord("A")
            crypted_value = (ascii_value + key) % 26
            crypted += chr(crypted_value + ord("A"))
        else:
            crypted += letter
    return crypted

# Menu de lancement
def main():
    print(f"Bienvenue dans CryptoSpace un endroit vous pouriez crypter et decrypter des données")
    print()
    options = input("Choisissez une optione :\n1.crypter\n2.decrypter\nchoix : ")
    data = input("votre message : ")
    if options == "1":
        encode = Logique(data)
        print(f"Le message crypté est : {encode}")
    elif options == "2":
        encode = Logique(data)
        decode = Logique(encode, decode=True)
        print(f"le message decrypté est : {decode}")
    else:
        print(f"Choix indisponible") 
        exit()
    
    data = data.replace("é","e").replace("ê","e").replace("è","e").replace("î","i").replace("à","a").replace("â","a").replace("ù","u").replace("ï","i")
    
      
if __name__=='__main__':
    main()
