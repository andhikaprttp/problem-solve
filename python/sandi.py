# encryption
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from art import *

print(Fore.CYAN + "===========")
tia=text2art("Andhika") 
print(tia)
data = input(("Masukan Teks : "))

# 8 byte block 
key = b'1n1kunC1' 

# Menetapkan panjang data yang akan dienkripsi
BLOCK_SIZE = 32 

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)
print(Fore.RED + "Chipertext anda : ")
print(" ")
print(encrypted_text)
print(" ")
print(Fore.YELLOW + "==============")

# decryption
key = b'1n1kunC1' # 8 byte block
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print(Fore.GREEN + "Plaintext anda : ")
print(" ")
print(decrypted_text.decode())
print(" ")
print(Fore.YELLOW + "=============")
