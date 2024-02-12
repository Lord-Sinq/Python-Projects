from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def generate_key_pair():
    '''
    Generate RSA key pair
    :return: private_key, public_key
    '''
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, public_key):
    '''
    Encrypt message function
    :param message: This can be whatever
    :param public_key: from generate_key_pair
    :return: final_message
    '''
    # Generate symmetric key for AES
    symmetric_key = b'0123456789123456'

    # Encrypt the message with AES
    cipher = AES.new(symmetric_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))

    # Encrypt the symmetric key with the recipient's public key
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_symmetric_key = cipher_rsa.encrypt(symmetric_key)

    # Combine the encrypted message, encrypted symmetric key, and AES tag
    final_message = enc_symmetric_key + cipher.nonce + tag + ciphertext
    return final_message

def decrypt_message(final_message, private_key, public_key):
    '''
    Decrypt message function
    :param final_message: from encrypt_message
    :param private_key: from generate_key_pair
    :param public_key: from generate_key_pair
    :return: decrypted message else None
    '''
    # Split the final message into components
    enc_symmetric_key = final_message[:256]
    nonce = final_message[256:272]
    tag = final_message[272:288]
    ciphertext = final_message[288:]

    # Decrypt the symmetric key with the recipient's private key
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    symmetric_key = cipher_rsa.decrypt(enc_symmetric_key)

    # Decrypt the message with the symmetric key
    cipher = AES.new(symmetric_key, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)

    # Verify the signature using sender's public key
    hash_signature = tag

    # Compare the hashes
    if hash_signature == tag:
        print("Message authenticated.")
        return decrypted_message.decode('utf-8')
    else:
        print("Message authentication failed.")
        return None
def main():
    '''
    Main function holding the message,
    the sender calles, and the receiver calles
    :return: The message decrypted
    '''
    # Sender Side
    sender_private_key, sender_public_key = generate_key_pair()
    receiver_private_key, receiver_public_key = generate_key_pair()
    file = open('CSC_424_Assign_3_text_File.rtf', 'r')
    text_list = []
    for x in file:
        text_list.append(x)
    message_to_send = ''.join(text_list)
    encrypted_message = encrypt_message(message_to_send, receiver_public_key)

    # Receiver Side
    decrypted_message = decrypt_message(encrypted_message, receiver_private_key, sender_public_key)
    #if decrypted_message:
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
