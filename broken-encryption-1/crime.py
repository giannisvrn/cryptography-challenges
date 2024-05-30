#!/usr/bin/python2 -u
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import zlib

flag = open("flag", "r").read() # You do not have access to this file.
key = open('enc_key', 'r').read().strip().decode('hex')

welcome = """
************ MI6 Secure Encryption Service ************

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

def encrypt():
  iv = os.urandom(16)
  ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))
  cipher = AES.new(key, AES.MODE_CTR, counter = ctr)

  m = raw_input("Message: ")
  m = "signature=" + flag + m
  m = zlib.compress(m, 9)

  encrypted = cipher.encrypt(m)

  return iv.encode('hex') + encrypted.encode('hex')

def decrypt():
  m = raw_input("Encrypted Message: ")

  iv = m[:32].decode('hex')
  ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))
  cipher = AES.new(key, AES.MODE_CTR, counter = ctr)
  compressed = cipher.decrypt(m[32:].decode('hex'))
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
