# Documentation for current version!

##Let's get if the user is using IDLE or Command Line to run:

`
get = idleorcommandline()
`
#
`
print(get)
`
#
`
True
`
#
Looks like the User is running with IDLE
#
`
print(get)
`
#
`
False
`
#
Looks like the User is running with Command Line
#
##Let's get the users os:
#
`
os = osfinder()
`
#
`
print(os)
`
#
It will print either "posix","nt","dos","ce" or Fasle
#
##Let's get the python version:

`
version = pythonverison()
`
#
`
print(version)
`
#
Let's say my version is 2.7.5 it will print 2.7.5 (as an intager)
##Let's see if the user's computer is 32 bit or 64 bit architecture:

`
bit = bits()
`
#
`
print(bit)
`
#
`
True
`
#
Looks like the user has a 64 bit!
#
`
False
`
#
Looks Like the user has a 32 bit!

#Look what Pylaunch API is doing!

##Pyfancy

Diggo ( https://github.com/ilovecode1/diggo ) is why Pylaunch API was made! It uses Pylaunch API to set it self up!

Pyfancy ( https://github.com/ilovecode1/pyfancy ) is using pylaunch API to make pyfancy smarter. Pyfancy uses 
`
idleorcommandline()
`
to figure out if it should disable pyfancy or not.
