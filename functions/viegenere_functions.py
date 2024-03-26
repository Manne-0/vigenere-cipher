def encoder(text, keyword):
    text = text.lower()
    keyword = keyword.lower()
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = ''
    for char in text.lower():
    #if character is not an alphabet, just append(no encryption for non alphabet characters)
        if not char.isalpha():
            encrypt += char
        else:
            #1. get the character at the index of keyword
            key_char = keyword[key_index % len(keyword)]
            key_index += 1
            #2. get the index of the keyword character in the alphabet(their position in the alphabet)
            offset = alphabet.index(key_char)
            #3. finds the position of the character of the plain text in the alphabets
            index = alphabet.find(char)
            #4. add the plain text charindex and the keyword index to get the position for the new char (to be encrypted)
            new_index = (index + offset) % len(alphabet)
            encrypt += alphabet[new_index]
    return encrypt


def decoder(encryption, keyword):
    encryption = encryption.lower()
    keyword = keyword.lower()
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypt = ''
    for char in encryption.lower():
    #if character is not an alphabet, just append(no encryption for non alphabet characters)
        if not char.isalpha():
            decrypt += char
        else:
            #1. get the character at the index of keyword
            key_char = keyword[key_index % len(keyword)]
            key_index += 1
            #2. get the index of the keyword character in the alphabet(their position in the alphabet)
            offset = alphabet.index(key_char)
            #3. finds the position of the character of the plain text in the alphabets
            index = alphabet.find(char)
            #4. add the plain text charindex and the keyword index to get the position for the new char (to be encrypted)
            new_index = (index + offset * -1) % len(alphabet)
            decrypt += alphabet[new_index]
    return decrypt
