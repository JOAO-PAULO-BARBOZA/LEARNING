"""EXEMPLOS A SEREM TESTADOS:

Sample input:    
abcxyzABCxyz 123
2
------------------
Sample output:    
cdezabCDEzab 123
------------------
Sample input:
The die is cast
25
------------------
Sample output:
Sgd chd hr bzrs

"""


message = input("Type the message that will be encrypted: ")

encrypted_message = ""

shift = 0

while not (25  >= shift >= 1): 

    try:
        shift = int(input("Type a number from 1 to 25: "))
        if shift <= 0 or shift > 25:
            print(f"{shift} is out of the range!")
    except:
        print("Are you sure that this is a number?.")

for ch in message:
    if not ch.isalpha():
        encrypted_message += ch
        continue
    
    elif ch.upper() != ch and (ord(ch) + shift > 122):
        encrypted_message += chr(ord("a") + (shift - (122 - ord(ch)) - 1))
    
    elif ch.lower() != ch and (ord(ch) + shift > 90):
        encrypted_message += chr(ord("A") + (shift - (90 - ord(ch)) - 1))
    
    else:
        encrypted_message += chr(ord(ch) + shift)

print(encrypted_message)
