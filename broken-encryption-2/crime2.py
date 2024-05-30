#!/usr/bin/python -u
from Crypto.Cipher import AES
import os
import zlib

flag = open("flag", "r").read()
key = open('enc_key', 'r').read().strip().decode('hex')

welcome = """
************ MI6 Secure Encryption Service ************
                [ Streaming is a crime! ]

       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/ 
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/


Enter your command:
"""

def pad(m):
  m = m + '1'
  while len(m) % 16 != 0:
    m = m + '0'
  return m

def unpad(m):
  while m[-1] == '0':
    m = m[:-1]
  return m[:-1]

def encrypt():
  iv = os.urandom(16)
  # Block ciphers prevent CRIME!
  cipher = AES.new(key, AES.MODE_CBC, iv)

  m = raw_input("Message: ")
  m = "signature=" + flag + m
  i = len("signature=" + flag)
  m = zlib.compress(m, 9)
  m = pad(m)

  encrypted = cipher.encrypt(m)

  return iv.encode('hex') + encrypted.encode('hex')

def decrypt():
  m = raw_input("Encrypted Message: ")

  iv = m[:32].decode('hex')
  cipher = AES.new(key, AES.MODE_CBC, iv)
  compressed = cipher.decrypt(m[32:].decode('hex'))
  m = unpad(m)
  m = zlib.decompress(compressed)

  if m[10:10 + len(flag)] != flag:
    return "Invalid signature!"

  return m[10 + len(flag):]

def process(cmd):
  if cmd == "help":
    return "Commands:\n\thelp - this\n\tencrypt - encrypt a message\n\tdecrypt - decrypt a message\n"
  if cmd == "encrypt":
   return encrypt() 
  if cmd == "decrypt":
    return decrypt()
  return "Invalid command. See help for a list of commands\n"

m = raw_input(welcome)
response = process(m.strip())
print(response)
