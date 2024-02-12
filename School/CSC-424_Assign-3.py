import binascii
import hashlib
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import  AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import  RSA
from base64 import b64encode, b64decode

def generate_key_pair():
    private_key = RSA.generate(2048).export_key()
    public_key = RSA.import_key(private_key).publickey().export_key()
    return private_key, public_key

def hash_message(message):
    # step 1
    if isinstance(message, str):
        message = message.encode()
    hashed_message = hashlib.sha256(message).digest()
    return hashed_message

def encrypt_rsa(message, key):
    # step 2
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(key))
    encrypted_message = cipher_rsa.encrypt(message)
    return encrypted_message

def decrypt_rsa(encrypted_message, key):
    # step 2
    private_key = RSA.import_key(key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message)
    return decrypted_message

def generate_symmetric_key():
    # step 3
    symmetric_key = AES.get_random_bytes(16)
    return symmetric_key

def encrypt_aes(message, key):
    # step 4
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = cipher.iv
    encrypted_message = iv + cipher_text
    return b64encode(encrypted_message)

def decrypt_aes(encrypted_message, key):
    try:
        # Ensure the IV length is correct
        if len(encrypted_message) < AES.block_size:
            raise ValueError("Incorrect IV length (it must be 16 bytes long)")

        iv = encrypted_message[:AES.block_size]
        cipher_text = encrypted_message[AES.block_size:]

        print("IV:", iv)
        print("Cipher Text:", cipher_text)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(cipher_text), AES.block_size, style='pkcs7')

        print("Decrypted Message:", decrypted_message)

        return decrypted_message.decode()
    except (ValueError, binascii.Error) as e:
        print(f"Error: {e}")

def sender_side(message, sender_private_key, receiver_public_key):
    hashed_message = hash_message(message)
    # step 2
    encrypted_hash = encrypt_rsa(hashed_message, sender_private_key)
    # step 3
    symmetric_key = generate_symmetric_key()
    # step 4
    encrypted_message = encrypt_aes(message, symmetric_key)
    # step 5
    encrypted_symmetric_key = encrypt_rsa(symmetric_key, receiver_public_key)

    # Combine results with consistent delimiter
    delimiter = b'|||'
    final_message = encrypted_message + delimiter + encrypted_hash + delimiter + encrypted_symmetric_key

    print(f"Sender: final_message length: {len(final_message)}")
    return b64encode(final_message)

def receiver_side(final_message, receiver_private_key, sender_public_key):
    final_message = b64decode(final_message)

    delimiter = b'|||'
    parts = final_message.split(delimiter)

    if len(parts) != 3:
        print(f"Error: Incorrect number of parts in final_message. Parts: {len(parts)}")
        print(f"Final Message: {final_message}")
        return

    encrypted_message, encrypted_hash, encrypted_symmetric_key = parts

    # print(f"Receiver: Lengths - encrypted_message:{len(encrypted_message)} encrypted_hash: {len(encrypted_hash)} encrypted_symmetric_key:{len(encrypted_symmetric_key)}")
    # print(f"Receiver: -- Parts --\nencrypted_message:{encrypted_message}\nEncrypted_hash: {encrypted_hash}\nEncrypted_symmetric_key:{encrypted_symmetric_key}")

    try:
        # step 1
        symmetric_key = decrypt_rsa(encrypted_symmetric_key, receiver_private_key)
        print("Decrypted symmetric key:", symmetric_key)
        # step 2
        decrypted_message = decrypt_aes(encrypted_message, symmetric_key)
        print("Decrypted decrypted message:", decrypted_message)
        # step 3
        decrypted_hash = decrypt_rsa(b64decode(encrypted_hash), sender_public_key)
        print("Decrypted decrypted hash:", decrypted_hash)
        # step 4
        hashed_received_message = hash_message(decrypted_message)
        print("Decrypted hashed received message:", hashed_received_message)
        # step 5
        if hashed_received_message == decrypted_hash:
            print("-:Message authenticated:-")
        else:
            print("-:Message -NOT- authenticated:-")
    except(ValueError, binascii.Error) as e:
        print(f"Error: {e}")

def main():
    sender_private_key, sender_public_key = generate_key_pair()
    receiver_private_key, receiver_public_key = generate_key_pair()

    message_to_send = "This is a long message, I hope you can read me."
    final_message = sender_side(message_to_send, sender_private_key, receiver_public_key)

    receiver_side(final_message, receiver_private_key, sender_public_key)



if __name__ == "__main__":
    main()

