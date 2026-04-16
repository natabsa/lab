
# Abre arquivo
# Para i em ['a', 'b'..., 'z']
#   Decifra com i
#   Avalia qual o mais provável até então
# Printa a decifra mais provável


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Text file to apply the cipher to")
args = parser.parse_args()

probable = ('a', 0)
common  = ['a','e','o','s','r','i','n','d','m']

for i in range(27):

    tmp = 0

    with open(args.file, "r") as file, open("ourput.txt", "w") as output:

        char = file.read(1)

        while char != "":
            if char.isalpha():
                ascii_unciphered = ord(char)-i
                if char.isupper() and ascii_unciphered < 65:
                    ascii_unciphered += 26
                elif char.islower() and ascii_unciphered < 97:
                    ascii_unciphered += 26
            if chr(ascii_unciphered) in common:
                tmp += 1
            char = file.read(1)

        if tmp > probable[1]:
            probable = (chr(i+95), tmp)



with open(args.file, "r") as file:
    
    char = file.read(1)

    while char != "":

        if char.isalpha():
            ascii_unciphered = ord(char)-ord(probable[0])
            if char.isupper() and ascii_unciphered < 65:
                ascii_unciphered += 26
            elif char.islower() and ascii_unciphered < 97:
                ascii_unciphered += 26            
            char = chr(ascii_unciphered)
    
        print(char, end="")
        char = file.read(1)

