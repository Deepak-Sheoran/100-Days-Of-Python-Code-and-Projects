from art import logo

print(logo)

alphabets = list("abcdefghijklmnopqrstuvwxyz")


def encrypt():
    message = list(input("Type your message: "))
    shift_number = int(input("Enter the shift number: "))
    encoded_message = ''
    for letter in message:
        if letter.lower() in alphabets:
            index = alphabets.index(letter.lower()) + shift_number

            # These while loops are here in case of big shift numbers
            while index > 25:
                index -= 26
            while index < 0:
                index += 26

            # These if else statement check whether the letter in the message is upper or lower case and changes
            # the letter based on the result
            if letter.islower():
                encoded_message += alphabets[index]
            else:
                encoded_message += alphabets[index].upper()

        # The following else statement is for letters that are not alphabet
        else:
            encoded_message += letter
    return encoded_message


def decrypt():
    message = list(input("Type your message: "))
    shift_number = int(input("Enter the shift number: "))
    decoded_message = ''
    for letter in message:
        if letter.lower() in alphabets:
            index = alphabets.index(letter.lower()) - shift_number

            while index > 25:
                index -= 26
            while index < 0:
                index += 26

            if letter.islower():
                decoded_message += alphabets[index]
            else:
                decoded_message += alphabets[index].upper()

        else:
            decoded_message += letter
    return decoded_message


# The following function can be used to fulfill the roles of both encrypt and decrypt functions
def caesar(opt="encode"):
    message = list(input("Type your message: "))
    shift_number = int(input("Enter the shift number: "))
    message = ''
    if opt == "decode":
        shift_number *= -1

    for letter in message:
        if letter.lower() in alphabets:
            index = alphabets.index(letter.lower()) + shift_number

            # These while loops are here in case of big shift numbers
            while index > 25:
                index -= 26
            while index < 0:
                index += 26

            # These if else statement check whether the letter in the message is upper or lower case and changes
            # the letter based on the result
            if letter.islower():
                message += alphabets[index]
            else:
                message += alphabets[index].upper()

        # The following else statement is for letters that are not alphabet
        else:
            message += letter
    return message


while True:
    option = input("Type 'encode' to encrypt, Type 'decode' to decrypt, Type 'exit' to stop the program: ").lower()
    if option == 'encode':
        print(f"Here's the encoded message = {encrypt()}")
    elif option == 'decode':
        print(f"Here's the decoded message = {decrypt()}")
    elif option == 'exit':
        break
    else:
        print("Wrong Choice!!")
