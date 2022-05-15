
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print('Encryption has started.')
    msg=input("Enter Message to be encrypted: ")
    key=int(input("Enter key(1 to 94): "))
    encrypted_text=""
    for i in range(len(msg)):
        temp= (ord(msg[i])+key)
        if temp>126:
            temp=temp-127+32
            encrypted_text+=chr(temp)
    print(encrypted_text)

def decryption():
    print('Decryption has started.')
    print("Message can only be in lower/upper case alphabet.")
    msg=input("Enter Message to be decrypted: ")
    key=int(input("Enter key(1 to 94): "))
    decrypted_text=""
    for i in range(len(msg)):
        temp= (ord(msg[i])-key)
        if temp<32:
            temp=temp+127-32
            decrypted_text+=chr(temp)
    print(decrypted_text)

if __name__ == "__main__":
    main()
