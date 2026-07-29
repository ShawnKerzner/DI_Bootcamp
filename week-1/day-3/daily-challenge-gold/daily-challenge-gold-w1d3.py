def encrypt():
    encrypted_text = ""
    user_msg_e = input("Enter your messsage here: ")
    for letter in user_msg_e:
        if letter.isupper():
            new_letter = chr((ord(letter) - ord('A') + 3) % 26 + ord('A'))
            encrypted_text += new_letter
        elif letter.islower():
            new_letter = chr((ord(letter) - ord('a') + 3) % 26 + ord('a'))
            encrypted_text += new_letter
        else: 
            encrypted_text += letter
    print(encrypted_text)


def decrypt():
    decrypted_text = ""
    user_msg_e = input("Enter your messsage here: ")
    for letter in user_msg_e:
        if letter.isupper():
            new_letter = chr((ord(letter) - ord('A') - 3) % 26 + ord('A'))
            decrypted_text += new_letter
        elif letter.islower():
            new_letter = chr((ord(letter) - ord('a') - 3) % 26 + ord('a'))
            decrypted_text += new_letter
        else: 
            decrypted_text += letter
    print(decrypted_text)


        
while True:
    select_task = input("Type 'encrypt' to encrypt a message, type 'decrpyt' to decrypt a message, or 'exit' to quit the program: ")
    if select_task == "encrypt":
        encrypt()
        break
    elif select_task == "decrypt":
        decrypt()
        break
    elif select_task == "exit":
        print("Goodbye")
        break
    else:
        print("Error: input needs to 'encrypt', 'decrypt', or 'exit'. Please try again.")
