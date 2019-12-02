#Test Test test
# Web challenge

Used:
- Linux
- Owasp-Zap

There is a nice web page.
We use owasp-zap to *snif* the website.

During the analysis of the website we can see that there is a **flag.php** page.
But this page won't be displayed because we are redirected to the index.html.

What a shame.

- Run the owasp-zap proxy, put the request in "pause" mode.
- Go to **flag.php**
- Now we can see the flag !
- **TUCTF{d0nt_l34v3_y0ur_d1r3ct0ry_h4n61n6}**

## More easy way !
Just find that during the redaction of this writeup !

- Right click on the browser
- *view-code-source*
- change the URL : *view-source:http://chal.tuctf.com:30004/index.html*
- To : *view-source:http://chal.tuctf.com:30004/flag.php*
