from random import *
listi=[]
tlisti=[]
nlisti=[]
nofn=[]
hrutar=[]

player1=[]
player2=[]





class Hrutar(object):#smiðurinn
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



class Hrutur(Hrutar):#classi  gerður svo að objectið heiti hrutar
    def typa(self):
        return




with open("hrutar2.txt","r") as f:# opnar hruta file-inn
    lina=f.read()
    listi = lina.split(",")# nær kommunni burt


t=0
for x in listi:
    if t%9 !=0:
        tlisti.append(x)#tek tölurnar og set í sér lista
    elif t%9==0:
        nlisti.append(x)#tek nöfnin og set í annan lista
    t+=1

tolur=list(map(float,tlisti))#breyti tölunum í float


t=1
nofn.append(nlisti[0])#fyrsta nafn  var venjulegt svo ég bæti þvi við útfyrir loop
for x in nlisti:#tek út /n fyrir framan öll nofn
    listi
    if t>1:
        nofn.append(x[1:])
    t+=1
nofn.remove(x[-1])# tek út seinasta stak



t=0
tala=[]
tolur=[]
for x in tlisti:#set fram loopu með teljara til að ná saman 8 stökum og setja saman i lista inni lista
    if t<8:
        tala.append(x)
        t+=1
    elif t==8:
        tolur.append(tala)
        tala=[]
        tala.append(x)
        t=1
tolur.append(tlisti[-8:])#loopan skildi eftir seinustu 8 tölurnar svo ég redda þvi svona





t=0
for i in range(52):#bý til  hrúta spilin og læt þau í  lista
    hrutur=Hrutur(nofn[t],tolur[t][0],tolur[t][1],tolur[t][2],tolur[t][3],tolur[t][4],tolur[t][5],tolur[t][6],tolur[t][7])
    hrutar.append(hrutur)
    t+=1#nota teljara til að halda öllu saman



stokkur=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]#þetta eru öll spilin

while len(stokkur)!=0 :#læt renna meðan stokkurinn er ekki tomur
    a = len(stokkur)  # hversu morg spil eru eftir í stokknum
    rt = randrange(0, a)  # random tala frá null og uppí fjölda spila
    if len(player1)<26:
        player1.append(hrutar[rt])#fyrsti stokkur fær 26 random spil
        print(len(player1))
    else:
        player2.append(hrutar[rt])  # annar stokkur fær 26 random spil
        print(len(player2))


    del stokkur[rt]#spilinu er eyttt úr stokknum
print (len(stokkur))
print(player1)
print(player2)