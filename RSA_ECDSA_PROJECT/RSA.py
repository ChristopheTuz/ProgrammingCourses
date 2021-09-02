from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def info(flag,msg):
    if(flag==1): print("\n ERROR: Invalid option")
    elif(flag==200): print("\n Successfully: Your public key key have been created ")
    elif(flag==201): print("\n Successfully: Your private key key have been created ")
    elif(flag==202): print("\n Successfully: Your message have been encrypted")
    elif(flag==203): print("\n Successfully: Your message have been decrypted")
    elif(flag==300): print("\n >>> Wait: Generating publick key")
    elif(flag==301): print("\n >>> Wait: Generating private key")
    elif(flag==302): print("\n >>> Wait: Encrypting message")
    elif(flag==303): print("\n >>> Wait: Decrypting message")
    elif(flag==777): print("\n Thank you, goodbye!\n")

def RSA_function():
    print("\n============================= RSA ===============================\n")
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()


    # Public key
    info(300,"GENERATING PubK")
    pubKeyPEM = pubKey.exportKey()
    info(200,"PubK generated")

    # Private key
    info(301,"GENERATING PriK")
    privKeyPEM = keyPair.exportKey()
    info(201,"PriK generated")

    ### Print data about public key ###
    #print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})") #Uncomment if you want to print data about your public key.
    #print(pubKeyPEM.decode('ascii')) #Uncomment if you want to print your public key.

    ### Print data about private key ###
    #print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})") #Uncomment if you want to print data about your private key.
    #print(privKeyPEM.decode('ascii')) #Uncomment if you want to print your private key.

    # Input message
    msg  = input("\n Give me a message to encrypt: ")
    msg2 = msg.encode('utf-8')

    # Encrypting message
    info(302,"Encrypting message")
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg2)
    print("\n Encrypted:", binascii.hexlify(encrypted).decode('utf-8'))
    info(202,"Message encrypted")

    # Decrypting message
    info(303,"Decrypting message")
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\n Decrypted:', decrypted.decode('utf-8'))
    info(203,"Message decrypted")

def run():
    RSA_function()
    info(777,"DONE")

if __name__ == "__main__":
    run()