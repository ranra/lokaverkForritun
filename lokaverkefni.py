listi=[]
tala1=[]
listi2=[]
nofn=[]
hrutar=[]

tolvan=[]
eg=[]



t=0

class Hrutar(object):
    def __init__(self,nafn,thyngd,mjolk,ull,born,laeri,gredda,bak,malir):
        self.n=nafn
        self.t=thyngd
        self.mj=mjolk
        self.u=ull
        self.bo=born
        self.l=laeri
        self.g=gredda
        self.ba=bak
        self.ma=malir



class Hrutur(Hrutar):
    def typa(self):
        return




with open("hrutar2.txt","r") as f:
    lina=f.read()
    listi = lina.split(",")
    print(listi)
for x in listi:
    print(x)

for x in listi:
    if t%9 !=0:
        tala1.append(x)
    elif t%9==0:
        listi2.append(x)


    t+=1
tolur=list(map(float,tala1))
print(tala1)
print(listi2)
f=1
nofn.append(listi2[0])
for x in listi2:
    listi
    if f>1:
        nofn.append(x[1:])

    f+=1
nofn.remove(x[-1])
print(nofn)

from random import *
t=0
tala=[]
tolur=[]
for x in tala1:
    if t<8:
        tala.append(x)
        t+=1
    elif t==8:
        tolur.append(tala)
        tala=[]
        tala.append(x)
        t=1
tolur.append(tala1[-8:])




print (len(tolur))
print(tolur)
print (len(nofn))
t=0
print(nofn[0],tolur[t][0],tolur[t][1],tolur[t][2],tolur[t][3],tolur[t][4],tolur[t][5],tolur[t][6],tolur[t][7])
for i in range(52):
    hrutur=Hrutur(nofn[t],tolur[t][0],tolur[t][1],tolur[t][2],tolur[t][3],tolur[t][4],tolur[t][5],tolur[t][6],tolur[t][7])
    hrutar.append(hrutur)

    t+=1
print(len(hrutar))
flag=True

talnalisti=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
print(talnalisti[3])
while flag :
    a=len(talnalisti)+1
    rt=randrange(0,a)

    print(rt)
    print(talnalisti[rt])
    if len(eg)<=26:
            eg.append(hrutar[rt])
            del talnalisti[rt]
            print(eg)
            print(talnalisti)
            print(eg)

    elif len(eg)>26:
        tolvan.append(hrutar[rt])
        del talnalisti[rt]



