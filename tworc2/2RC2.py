#!/usr/bin/python2 -u

from Crypto.Cipher import ARC2
import os
import string
import random

flag = open("flag", "r").read().strip() # You do not have access to the flag file.

master_key = ''.join(random.choice(string.digits + 'abcdef') for _ in range(12)).decode('hex')
key1 = master_key[:3]
key2 = master_key[3:]

def encrypt(m):
  cipher = ARC2.new(key1, ARC2.MODE_ECB)
  m = cipher.encrypt(m)
  cipher = ARC2.new(key2, ARC2.MODE_ECB)
  m = cipher.encrypt(m)
  return m.encode('hex')

welcome = """
*******************************************
***             Welcome to the          ***
***    FlAg EnCrYpTiOn SeRviCe 7006!    ***
*******************************************

We encrypt the flags, you get the points!"""

print(welcome)

#no one will ever be able to solve our super challenge!
m = "To prove how secure our service is, "
m += "here is an encrypted flag:\n"
m += "==================================\n"
m += encrypt(flag)
m += "\n==================================\n"
m += "Find the plaintext and we'll give you points\n"

print(m)

while True:
  m = raw_input("\nNow enter a message you wish to encrypt: ")
  if len(m) % 8 == 0:
    print("Your super unreadable ciphertext is:")
    print("==================================")
    print(encrypt(m)) 
    print("==================================")
  else:
    print("Your message's length should be a multiple of 8")
