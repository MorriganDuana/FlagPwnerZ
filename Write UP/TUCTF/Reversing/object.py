from pwn import *

cipher = "\xfd\xff\xd3\xfd\xd9\xa3\x93\x35" \
         "\x89\x39\xb1\x3d\x3b\xbf\x8d\x3d" \
         "\x3b\x37\x35\x89\x3f\xeb\x35\x89" \
         "\xeb\x91\xb1\x33\x3d\x83\x37\x89" \
         "\x39\xeb\x3b\x85\x37\x3f\xeb\x99" \
         "\x8d\x3d\x39\xaf"

clear = ""

def recover(c):
    r = xor(c, "\xaa")
    r = bnot(ord(r),8)+1
    r = r >> 1
    return chr(r)

for c in cipher:
    clear += recover(c)

print clear

# TUCTF{c0n6r47ul4710n5_0n_br34k1n6_7h15_fl46}
