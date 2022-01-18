from decoding import Decoding
from FileConfiguration import FileConfiguration

cfg = FileConfiguration("Files/public_key")
cfg2 = FileConfiguration("Files/private_key")
cfg3 = FileConfiguration("Files/encoded_message")
dec = Decoding()

def main():
    print()
    c = cfg2.get("value.c")
    n = cfg2.get("value.n")
    m = cfg2.get("value.m")
    msg = cfg3.get("encoded.messages")
    messages = []
    finalmessage = ""

    insertstring = False
    while True:
        ip = input("     Willst du das Ergebnis zu einem String konvertieren? [y/n]:     ")
        if ip == "y":
            insertstring = True
            break
        elif ip == "n":
            insertstring = False
            break
    
    for item in msg:
        message = str(dec.decode_message(c,n,item,m))
        length = len(message)
        msg2 = ""
        if length%3 != 0:
            message = "0" + message
            length += 1
        for i in range(length//3):
            try:
                msg3 = message[3*i : 3*i+3]
                if insertstring:
                    msg2 += chr(int(msg3))
                else:
                    msg2 += msg3
            except:
                pass
        messages.append(msg2)
        finalmessage += msg2

    print()
    print()
    print("     Nachricht: " + str(finalmessage))
    print()
    print()
    print("     Developed by Jérôme, Elias, Timon")
    print()

main()