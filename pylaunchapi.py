#Pylaunch API 0.2.5

try:
   import sys
   import time
   import os
   import platform
   
except:
    print("A Needed Module for Pylaunch API does not exist!")
    time.sleep(2)
    sys.exit()

def idleorcommandline():
   'If idleorcommandline returns True its IDLE if False its command line!'
   a = sys.executable
   m = '\\\\'
   m = m[0]
   while True:
       b = len(a)
       c = a[(b - 1)]
       if c == m:
           break
       a = a[:(b - 1)]
   if sys.executable == a + 'pythonw.exe':
       return True
   else:
       return False

def osfinder():
   'returns os name'
   if os.name == "posix":
       return("posix")
       
   elif os.name in ("nt"):
       return("nt")\

   elif os.name in ("dos"):
       return("dos")
       
   elif os.name in ("ce"):
       return("ce")
   else:
      return False

def pythonversion():
    'returns current python version'
    version = platform.python_version()
    version = int(version)
    return(version)

def bits():
     'checks if computer is 32 bit or 64 bit architecture returns True if 64 Bit reruns False if 32 Bit'
     bit = sys.maxsize > 2**32
     return(bit)
   }
