import sys
from Power_Pow import power_pow

class Encoding:
    def __init__(self, message = 0):
        self.message = message

    def get_message(self,n):
        insertstring = False
        while True:
            ip = input("     Willst du einen String konvertieren? [y/n]:     ")
            if ip == "y":
                insertstring = True
                break
            elif ip == "n":
                insertstring = False
                break
        self.message = str(input("     Nachricht: "))
        if insertstring:
            msg = []
            msg[:0] = self.message
            msg2 = ""
            for i in msg:
                msg3 = str(ord(i))
                if len(msg3) == 2:
                    msg3 = "0" + msg3
                msg2+=msg3
            self.message2 = msg2
        else: 
            try:
                int(self.message)
            except:
                self.get_message(n)
                return
            self.message2 = self.message

        nlength = len(str(n))
        self.messages = []
        i2 = 0
        while len(self.message2) >= nlength:
            self.messages.append(self.message2[0 : nlength-1])
            self.message2 = self.message2[nlength-1:]
            i2 += 1
        self.messages.append(self.message2)

    def simplify(self, c, n, message):
        x = message
        z = 1
        y = power_pow(x,c,n)
        return y
