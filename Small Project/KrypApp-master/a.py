#dynamiccoding.tech
# pip install cryptography
from cryptography.fernet import Fernet
 
def generate_key():
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)
        print("Key is generated Sucessfully")
 
def load_key():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
        return key
 
def encript_file(filename):
    # First load the key..
    key = load_key()
 
    f = Fernet(key)
    with open(filename, 'rb') as original_file:
        original = original_file.read()
    
    enc_file = "enc"+str(filename)
        
    encrypted = f.encrypt(original)
    with open (enc_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
 
    print("File is encripted and save as "+enc_file)
 
def decript_file(filename):
    # First load the key..
    key = load_key()
 
    f = Fernet(key)
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
 
    dec_file = "dec"+str(filename)
    
    decrypted = f.decrypt(encrypted)
    with open(dec_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    print("File is decripted and save as "+dec_file)
 
# Calling Generate key function.
#generate_key() # At First Run This file before main
 
def main():
    filename =input("Enter file name to Encript/ Decript : ")
 
    choice = int(input(f"press 1 for encript and 2 for decript {filename} : "))
    if choice == 1:
        encript_file(filename)
    elif choice==2:
        decript_file(filename)
    else:
        print("wrong input")
 
if __name__ == "__main__":
    main()
 
