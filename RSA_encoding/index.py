from encoding import Encoding
from FileConfiguration import FileConfiguration
import math

cfg = FileConfiguration("Files/public_key")
cfg2 = FileConfiguration("Files/encoded_message")
enc = Encoding()

def main():
    print()
    c = cfg.get("value.c")
    n = cfg.get("value.n")
    enc.get_message(n)
    l = []
    for item in enc.messages:
        l.append(enc.simplify(c, n, int(item)))
    cfg2.set("encoded.messages", l)
    cfg2.save()
    print()
    print("     Done")
    print()

main()