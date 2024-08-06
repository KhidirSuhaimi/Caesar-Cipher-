alphabet = list('abcdefghijklmnopqrstuvwxyz')


# encrypted_letter = ''
new_letter_index = 0


# def encrypt(text,shift):
#     encrypted_letter = ''
#     for letter in text:
#         new_letter_index = alphabet.index(letter) + shift
#         new_letter_index %= len(alphabet)
#
#         encrypted_letter += alphabet[new_letter_index]
#     print(f'Here is your encoded result  {encrypted_letter}')

# encrypt(text,shift)

# def decrypt(text,shift):
#     decrypted_letter = ''
#     for letter in text:
#         new_letter_index = alphabet.index(letter) - shift
#         new_letter_index %= len(alphabet)
#
#         decrypted_letter += alphabet[new_letter_index]
#     print(f'Here is your decoded result  {decrypted_letter}')
# decrypt(text,shift)

def ceasar(text, shift, direction):
        if direction == 'decode':
            shift *= -1
        encrypted_letter = ''
        for letter in text:

            if letter.isalpha():
                new_letter_index = alphabet.index(letter) + shift
                new_letter_index %= len(alphabet)

                encrypted_letter += alphabet[new_letter_index]
            else:
                encrypted_letter += letter
        print(f'Here is your {direction}d result: {encrypted_letter}')


again = True

while again:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))
    ceasar(text,shift,direction)
    decision = input("Type \"Yes\" if you want to go again.\nType \"No\" if you want to end. ").lower()
    if decision == "yes":
        again = True
    else:
        again = False