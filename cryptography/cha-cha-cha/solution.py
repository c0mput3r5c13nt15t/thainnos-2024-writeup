from Crypto.Cipher import ChaCha20
from binascii import unhexlify

# Target ciphertext
target_cipher = "42d0abb245c4db4f61aefcce37df3bcda91825cc3faee5da173010938a27"  # Can be extracted from code

# Convert target ciphertext to bytes
target_cipher_bytes = bytes.fromhex(target_cipher)

# Parameters
key = bytes.fromhex(
    "307836313730373836352b30783333323036343665307836313730373836352b"
)  # Key can be extracted from code (variable z in cha_cha_cha)
nonce = bytes.fromhex("0000000000000000")
rounds = 20

# Brute force loop
plaintext = bytearray(len(target_cipher_bytes))
for byte_index in range(len(target_cipher_bytes)):
    for candidate in range(256):  # Try all possible byte values
        # Create a ChaCha cipher object
        cipher = ChaCha20.new(key=key, nonce=nonce)

        # Set the plaintext byte
        plaintext[byte_index] = candidate

        # Encrypt the candidate plaintext
        ciphertext = cipher.encrypt(plaintext)

        # Check if the ciphertext matches the target
        if ciphertext[byte_index] == target_cipher_bytes[byte_index]:
            # If a match is found, print the plaintext byte and exit
            print(f"Found plaintext byte at index {byte_index}: {hex(candidate)}")
            break

# Print the full plaintext when finished
print("Flag:", plaintext.decode())
