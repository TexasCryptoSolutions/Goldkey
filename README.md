# Goldkey
Fibonacci Golden Crypto Key Generator Hash Tool for Python  


Example :   user@user:~\$ python3  



This tool uses inputs to generate number strings that are used to  
generate a unique Hash for encryption use with other block ciphers.  


Raw Algo is based on:  
  
while(n>2):  
      c=a+b;  
      a=b;  
      b=c;  
      n=n-1;  
      bar.next()    
      
Requirements: 
import base64  
import binascii  
import math  
import sys  
import progressbar  
from termcolor import colored  
from ipywidgets import IntProgress  
from IPython.display import display  
from binascii import hexlify  
from progress.bar import Bar  
  
