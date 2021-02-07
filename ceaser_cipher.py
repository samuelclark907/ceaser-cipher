import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words
word_list = words.words()
# print(word_list)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# abcdefghijklmnopqrstuvwxyz

def encrypt(plain, key):
    encrypted_text = ''
    for char in plain:
        # print(char)   
        # print(char)
        if char.isupper():
            encrypted_text += chr((ord(char) + key-65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + key-97) % 26 + 97)
        else:
            encrypted_text += char
    print(encrypted_text)
    return encrypted_text


def decrypt(encoded, key):
    decrypted_text = encrypt(encoded, -key)
    # print(decrypted_text)
    return decrypted_text

def crack(encoded):
    crack_list = []
    hacked = ''
    for n in range(26):
        encoded_data = decrypt(encoded, n)
        split_data = encoded_data.split()
        crack_list.append(split_data)
        # crack_list.append(e)
    for i in crack_list:
        # print(i)
        current = i
        for j in i:
            print(j)
            
            # print(j)
        # for j in i:
        #     print(j)
        #     if i[j] in word_list:
        #         hacked += i 
            # print(('word', j))
            # if j.isalpha():
            #     lcword = j.lower()
            #     if lcword in word_list:
            #         hacked += f'{lcword} '

    # print(('hacked', hacked))

    # print(('hackedlist', hacked))



if __name__ == "__main__":
    text = "It was the best of times, it was the worst of times."
    enc = encrypt(text, 5)
    decrypt(enc, 5)
    crack(enc)

    