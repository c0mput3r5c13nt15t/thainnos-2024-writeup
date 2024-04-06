from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Components (taken from the hex message in the format nonce16byte:tag16byte:s3cr3tm3ssag3isth3pbkdf2input, which is the name in reverse)
nonce = bytes.fromhex("546869732069732061206e6f6e636521")
gcm_tag = bytes.fromhex("d3a8c7d7aab4d80337e31c67d8f65723")
ciphertext = bytes.fromhex(
    "076e8f1742bd3c8564afdb4b45309dae7455002f091ec704fa573ff78969dc6f9b9b58e5d5f16b4a67d8"
)

# Parameters taken from the challenge description
iterations = 1000000
key_length = 32

# Derive the key using PBKDF2
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA1(),
    length=key_length,
    salt=b"This_is_totally_not_an_initialization_vector_IV456",
    iterations=iterations,
    backend=default_backend(),
)

key = kdf.derive(b"This_is_totally_not_a_32_byte_1000000_iteratrion_sha1_PBKDF2_key123")

# Decrypt the message
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, gcm_tag), backend=backend)
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print("Flag:", plaintext.decode())
