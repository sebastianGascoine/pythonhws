# File Name:     midtermTHProject1.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 15, 2022
#
# Problem Statement: Write a program that can encode and decode Caesar ciphers. You will also need to deal with letters dropping off the end of the alphabet.

def main():
    key, code, message = input("What is the Key, code, and message of the Cipher (Ex: 2, encode/decode, Hello World)").split(', ')
    # key is how many letters moved 
    cipher = caeser(key, code, message)
    print("The result of cypher is",cipher)

def caeser(key, code, message): # alphabet, cipher to return 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    if(code == 'encode'): #enc will be multiply the shift so that it can de/encode
        shift = key
        print(str(shift))
    else: #shift foward key is = shift back 26 - key
        shift = 26 - int(key)
        print(str(shift))

    for i in message: # get the index of where the character shows in alphabet then get index of it + key and add to cipher

        index = alphabet.index(i) + int(shift)
        # if index is greater than 26 get mod
        if(index > 26):
            index = index % 26
        
        print(index)
        cipher += alphabet[index]
    
    return cipher

main()