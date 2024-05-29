import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <ciphertext_hex>")
    sys.exit(1)

ciphertext_hex = sys.argv[1]
ciphertext_bytes = bytes.fromhex(ciphertext_hex)

block_size = 16
cipher_blocks = [ciphertext_bytes[i:i+block_size] for i in range(0, len(ciphertext_bytes), block_size)]

second_block = cipher_blocks[1]  # Get the last block
#sixth_block = cipher_blocks[5]
second_block_hex = second_block.hex()
#sixth_block_hex = sixth_block.hex()
#if last_block_hex == "80875480b23e04bc57e29122aa9f3979":
#print(last_block_hex)
print(second_block_hex)
