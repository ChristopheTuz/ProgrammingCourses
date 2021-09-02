from pycoin.ecdsa import generator_secp256k1, sign, verify
import hashlib, secrets

def info(flag,msg2):
    if(flag==1): print("\n ERROR: Invalid option\n")
    elif(flag==200): print("\n Successfully: Your public key have been created\n")
    elif(flag==201): print("\n Successfully: Your private key and signaturen have been created\n")
    elif(flag==202): print("\n Successfully: Your message have been verificated\n")
    elif(flag==300): print("\n >>> Wait: Generating publick key\n")
    elif(flag==301): print("\n >>> Wait: Generating private key and signaturen\n")
    elif(flag==302): print("\n >>> Wait: Verify\n")
    elif(flag==777): print("\n Thank you, goodbye!\n")

def sha3_256Hash(msg2):
    hashBytes = hashlib.sha3_256(msg2.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")

def signECDSAsecp256k1(msg2, privKey):
    msg2Hash = sha3_256Hash(msg2)
    signature = sign(generator_secp256k1, privKey, msg2Hash)
    return signature

def verifyECDSAsecp256k1(msg2, signature, pubKey):
    msg2Hash = sha3_256Hash(msg2)
    valid = verify(generator_secp256k1, pubKey, msg2Hash, signature)
    return valid

def ECDSA_function():
    print("\n============================ ECDSA ==============================\n")
    # ECDSA sign message (using the curve secp256k1 + SHA3-256)
    msg  = input(" Give me a message to encrypt: ")
    info(301,"Generating private key")
    privKey = secrets.randbelow(generator_secp256k1.order())
    signature = signECDSAsecp256k1(msg, privKey)

    ### Print data about private key and signature###
    #print(" Private key:", hex(privKey)) #Uncomment if you want to print data about your private key.
    #print(" Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1])) #Uncomment if you want to print data about your signature.
    info(201,"Private key generated")

    # ECDSA verify signature (using the curve secp256k1 + SHA3-256)
    info(300,"Generating public key")
    pubKey = (generator_secp256k1 * privKey).pair()
    valid = verifyECDSAsecp256k1(msg, signature, pubKey)

    ### Print data about public key ###
    #print(" Public key: (" + hex(pubKey[0]) + ", " + hex(pubKey[1]) + ")") #Uncomment if you want to print data about your public key.
    info(200,"Public key generated")
    info(302,"Verify")
    print(" Validate status: [",valid,"]")
    info(202,"verificated")

    # ECDSA verify tampered signature (using the curve secp256k1 + SHA3-256)
    msg2  = input(" Give me a message to verify: ")
    valid = verifyECDSAsecp256k1(msg2, signature, pubKey)
    info(302,"Verify")
    print(" Validate status: [",valid,"]")
    info(202,"verificated")
    

def run():
    ECDSA_function()
    info(777,"DONE")

if __name__ == "__main__":
    run()