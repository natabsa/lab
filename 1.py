
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("cipher", help="Value from 0 to 25", type=int)
parser.add_argument("file", help="Text file to apply the cipher to")

args = parser.parse_args()

with open(args.file, "r") as file:
    
    char = file.read(1)

    while char != "":

        if char.isalpha():
            ascii_cipher = ord(char)+args.cipher
            if char.isupper() and ascii_cipher > 90:
                ascii_cipher -= 26
            elif char.islower() and ascii_cipher > 122:
                ascii_cipher -= 26            
            char = chr(ascii_cipher)
    
        print(char, end="")
        char = file.read(1)
