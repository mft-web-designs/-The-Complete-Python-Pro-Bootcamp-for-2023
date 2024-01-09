alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ""
    unknown_char = "%"
    for letter in plain_text:
        #print(f"letter: {letter}")
        if letter in alphabet:
            position = alphabet.index(letter)
            #print(f"position: {position}")
            new_position = position + shift_amount
            if new_position > 25:
                new_position = new_position - 25
            #print(f"new_position: {new_position}")
            #print(f"New Letter: {alphabet[new_position]}")

            cipher_text += alphabet[new_position]
        else:
            cipher_text += unknown_char
    print(f"The encoded text is {cipher_text}")

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt("abcde uvwxyz", 12)
