import sys
def caesar_cipher(shift, text):
    encrypt_text = ""
     # initialize the encrypted message and row and column counters to 1
    row = 1
    column = 1
     # loop through each character in the input text
    for character in text.upper():
         # check if the character is a letter
        if character.isalpha() == True:
            # get the ASCII code of the character and shift it
            ascii_char = ord(character)
            new_char = ascii_char + shift 
            
            if new_char > 90:
                remaining_char = new_char - 90
                new_char = 64 + remaining_char

            # get the new character from the shifted ASCII code
            new_char_1 = chr(new_char)
            # if we have 5 characters in the current row, add a space and reset the row counter
            if row == 5:
                encrypt_text += new_char_1
                encrypt_text += " "
                row = 1
                column += 1
            else:
                encrypt_text += new_char_1
                row += 1
            # if we've added 10 blocks of 5 characters each, add a newline and reset the column counter
            if column > 10:
                encrypt_text += "\n"
                column = 1
    # if we've added 10 blocks of 5 characters each, add a newline and reset the column counter
    return encrypt_text

if __name__ == '__main__':
    shift = int(sys.argv[1])
    message = input('Enter a message to encrypt: ')
    encrypted_message = caesar_cipher(shift, message)
    print(encrypted_message)


