
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

#Variables
g01 = sys.argv[2]
g01 = g01.encode("utf-8")
Pwl = len(g01)
newEnc = binascii.hexlify(g01)
finEnc = int(newEnc, 16)
EPX2 = str(Pwl ** 4)
g02 = int(EPX2 * Pwl)
a= int(finEnc);
b= int(g02);
n11 = str(Pwl)
n132 = int(n11)
n21 = int(EPX2[:3])
bytes1 =  int(n21)
bytes2 = bytes1 - 128

#Set Difficulty / IV
n = int(sys.argv[1])
n1 = str(n)

bar = Bar('Processing', max=n);
info1 = str("Keys: "+ str(a)+ ":"  + str(b))
info1 = colored(info1, 'yellow')

Diff = colored(str(n), 'red')
info = colored(str("Hash Difficulty: "), 'white')
#print(info1)
#print(info, Diff);
bar.start();
h = int(finEnc);

while(n>2):
      c=a+b;
      a=b;
      b=c;
      n=n-1;
      bar.next()
#Second Round Preparation

j = c
p = n *n
g07 = int(c * 2)
bar.next()

i= int(g07);

while(p>2):
      j=h+i;
      h=i;
      i=j;
      p=p-1;
      bar.next();

#Golden Itterations

re = str(j)
pr = re.encode("utf-8")
ed = binascii.hexlify(pr)
fin = base64.b64encode(ed)
listH = list(str(finEnc))
r0 = base64.b64encode(fin)
r0 = r0.decode('utf-8')
FirstHash = (r0[:79]) if len(r0) > 79 else r0
text1 = str("First Hash: ")
text2 = colored(text1, 'red')

bar.finish()
print(str(info1))
print(info + Diff)



#<First Shift>
#First character table Preparation
s1 = str(listH[3])
s2 = str(listH[4])
s3 = str(listH[5])
s4 = str(listH[6])
s5 = str(listH[7])
s6 = str(listH[8])
s7 = str(listH[9])
s8 = str(listH[10])
s9 = str(listH[11])
s10 = str(listH[12])
#charracter Array Shift
r1 = r0.replace(s7, s1)
r2 = r1.replace(s4 , s2)
r3 = r2.replace(s9, s3)
r4 = r3.replace(s6, s4)
r5 = r4.replace(s1, s5)
r6 = r5.replace(s3, s6)
r7 = r6.replace(s10, s7)
r8 = r7.replace(s2, s8)
r9 = r8.replace(s5, s9)
r10 = r9.replace(s8, s10)
r10 = r10.encode('utf-8')
r12 = r10.decode('utf-8')
#Print Hash
listI = list(str(r12))
#<Second Shift>
#Second character table Preparation
s11 = str(listI[3])
s12 = str(listI[4])
s13 = str(listI[5])
s14 = str(listI[6])
s15 = str(listI[7])
s16 = str(listI[8])
s17 = str(listI[9])
s18 = str(listI[10])
s19 = str(listI[11])
s110 = str(listI[12])

#Second charracter Array Shift
r11 = r0.replace(s11, s15)
r12 = r11.replace(s110, s17)
r13 = r12.replace(s19, s13)
r14 = r13.replace(s16, s14)
r15 = r14.replace(s12, s18)
r16 = r15.replace(s13, s16)
r17 = r16.replace(s14 , s12)
r18 = r17.replace(s18, s19)
r19 = r18.replace(s15, s19)
r110 = r19.replace(s17, s11)
r110 = r110.encode('utf-8')
r112 = r110.decode('utf-8')

info0 = (r112[:79]) if len(r112) > 79 else r112
lenbit = str(sys.getsizeof(info0))
print("String Size: " + lenbit + " Bit")
info3 = str("Final Hash: ")
info3 = colored(info3, 'blue')
print(text2 + FirstHash)
print(info3 + info0)
