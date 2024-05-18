from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

secret_message = "8ab2dae2f9d127ed966086c243f14a6360a9e36f0c64f8b6cdf9805a3de12b3b"
iv = "3b9390ed898378210016db09002f115c"
key = "c3baa53a66f0a5beddce45d938ac7975"

# Convert hex encoded parameters to bytes
secret_message_bytes = binascii.unhexlify(secret_message)
iv_bytes = binascii.unhexlify(iv)
key_bytes = binascii.unhexlify(key)

# Create AES cipher object in CBC mode
cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

# Decrypt the secret message
decrypted_data = cipher.decrypt(secret_message_bytes)

# Print the decrypted data
print("Decrypted message:", decrypted_data.decode('utf-8'))
