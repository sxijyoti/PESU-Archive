import binascii
from Crypto.Cipher import AES

# Provided values (hex strings)
PLAINTEXT_HEX = "255044462d312e350a25d0d4c5d80a34"
CIPHERTEXT_HEX = "d06bf9d0dab8e8ef880660d2af65aa82"
IV_HEX = "09080706050403020100A2B2C2D2E2F2"

# convert to bytes
plaintext = binascii.unhexlify(PLAINTEXT_HEX)
target_ct = binascii.unhexlify(CIPHERTEXT_HEX)
iv = binascii.unhexlify(IV_HEX)

print("Plaintext (len={}): {}".format(len(plaintext), PLAINTEXT_HEX))
print("IV (len={}): {}".format(len(iv), IV_HEX))
print("Target ciphertext: {}".format(CIPHERTEXT_HEX))
print("Reading keys from keys.txt ...")

found = False
with open("keys.txt", "r") as f:
    for lineno, line in enumerate(f, start=1):
        key_hex = line.strip()
        if not key_hex:
            continue
        try:
            key = binascii.unhexlify(key_hex)
        except binascii.Error:
            continue

        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = cipher.encrypt(plaintext)

        if ct == target_ct:
            print("Match found!")
            print("Line:", lineno)
            print("Key (hex):", key_hex)
            print("Key (bytes):", key)
            found = True
            break

if not found:
    print("No match found in keys.txt.")
