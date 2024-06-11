from cryptography.fernet import Fernet
import getpass
import hashlib
import base64

def generate_key(password):
    # Encode password to bytes
    password_bytes = password.encode()

    # Take SHA256 hash of the password
    hashed_password = hashlib.sha256(password_bytes).digest()

    # Return the first 32 bytes of the hashed password
    return base64.urlsafe_b64encode(hashed_password[:32])

def encrypt_string(data, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_string(encrypted_data, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()
    except Exception as e:
        if "Fernet key must be 32 url-safe base64-encoded bytes" in str(e):
            return "Incorrect password."
        else:
            return str(e)

def encrypt_string_user():
  input_string = input("Enter the string to encrypt: ")
  password = getpass.getpass("Enter your password: ")
  return encrypt_string(input_string,password)

def decrypt_string_user():
  input_string = input("Enter the string to decrypt: ")
  password = getpass.getpass("Enter your password: ")
  return decrypt_string(input_string,password)

def encrypt_string_user_pass(mystr):  
  password = getpass.getpass("Enter your password: ")
  return encrypt_string(mystr,password)
  
def decrypt_string_user_pass(mystr):  
  password = getpass.getpass("Enter your password: ")
  return decrypt_string(mystr,password)  