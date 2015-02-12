#Pythong script for Vigenere Cipher encryption
#uses block encryption technique for key repetition
#Author: Samuel Coe 
#http://samuelm.co

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,-_'

message = raw_input("Message to encrypt: ")
key = raw_input('Encryption key: ').upper()

encrypted = []

index = 0

for character in message:
  current = CHARSET.find(character.upper())
  if current != -1:
    current += CHARSET.find(key[index])
    current %= len(CHARSET)
    encrypted.append(CHARSET[current].upper())
    index += 1
    if index == len(key):
      index = 0
      key = encrypted
  else:
    encrypted.append(character)

print "Input: %s" % message
print "Output: %s" % ''.join(encrypted)