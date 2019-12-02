#solutions
##1
`find . -name '*' -exec cat {} \; | grep "TUCTF"`

##2
`find . -name '*' -exec grep -rni 'TUCTF'
