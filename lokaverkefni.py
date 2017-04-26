from random import *
stokkur=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]#þetta eru öll spilin
valmynd=["ekkert","Þyng í kílóum","Mjólkurlagni dætra ","Einkunn ullar ","Fjöldi afkvæma ","Einkunn læris","Frjósemi ","Gerð/Þykkt bakvöðva ","Einkunn fyrir malir"]#listi til að geta kallað í það sem valið var
listi=[]
tlisti=[]
nlisti=[]
nofn=[]
hrutar=[]
geymsla=[]





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


def deiling(a):
    utkoma=52/a
    return utkoma



with open("hrutar2.txt","r") as f:# opnar hruta file-inn
    lina=f.read()
    listi = lina.split(",")# nær kommunni burt
    print(listi)

t=0
for x in listi:
    if t%9 !=0:
        tlisti.append(x)#tek tölurnar og set í sér lista
    elif t%9==0:
        nlisti.append(x)#tek nöfnin og set í annan lista
    t+=1

tlisti=list(map(float,tlisti))#breyti tölunum í float
print(tlisti)
print(nlisti)
t=1
nofn.append(nlisti[0])#fyrsta nafn  var venjulegt svo ég bæti þvi við útfyrir loop

for x in nlisti:#tek út /n fyrir framan öll nofn
    if t>1:
        nofn.append(x[1:])
    t+=1
nofn.remove(nofn[-1])# tek út seinasta stak
print(nofn)


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







flag=True
while flag:
    print("hrútaspilið er góð skemmtun")
    print("veldu 1 til að keppa á móti tölvunni")
    print("veldu 2 til að keppa á móti tölvunni")
    svar=input(">>")


    if svar =="1":
        player1 = []
        player2 = []
        skipta=deiling(2)#deilt spilum milli spilara
        while len(stokkur) != 0:  # læt renna meðan stokkurinn er ekki tomur
            a = len(stokkur)  # hversu morg spil eru eftir í stokknum
            rt = randrange(0, a)  # random tala frá null og uppí fjölda spila
            nt=stokkur[rt]#spilið sjálft
            if len(player1) < skipta:#skipt spilum eftir fjölda spilara
                player1.append(hrutar[nt])# fyrsti stokkur fær 26 random spil
                print(nt,end=" ")

            else:
                player2.append(hrutar[nt])  # annar stokkur fær 26 random spil

                print(nt,end=": ")


            del stokkur[rt]  # spilinu er eytt úr stokknum

        tkast=randint(1,2)#kastað uppá hver byrjar



        while len(player1)!=0 or len(player2)!=0:
            hlutur1 = [player1[0].n, player1[0].t, player1[0].mj, player1[0].u, player1[0].bo, player1[0].l,player1[0].g, player1[0].ba, player1[0].ma]  # einföld leið til að sækja valið er
            hlutur2 = [player2[0].n, player2[0].t, player2[0].mj, player2[0].u, player2[0].bo, player2[0].l,player2[0].g, player2[0].ba, player2[0].ma]  #

            if tkast==1:#þá fær spilari 1 að gera
                flag=True
                fj = len(geymsla)#til að geta gefið upp hversu margir hrútar í geymslu
                print("þú átt að gera")#valmynd fyrir spilin
                gera=input("ýttu á 3 til að draga spil")
                print("\n")
                print("Hrúturinn heitir ",player1[0].n)#allar upplýsingar um spilið gefnar upp
                print("1.Þyng í kílóum ",player1[0].t)
                print("2.Mjólkurlagni dætra ", player1[0].mj)
                print("3.Einkunn ullar ", player1[0].u)
                print("4.Fjöldi afkvæma ", player1[0].bo)
                print("5.Einkunn læris", player1[0].l)
                print("6.Frjósemi ", player1[0].g)
                print("7.Gerð/Þykkt bakvöðva ", player1[0].ba)
                print("8.Einkunn fyrir malir", player1[0].ma)
                print("\n")
                while flag:#þartil valið er rétt
                    val=int(input("veldu flokk til að keppa í"))
                    if val >0 and val<9:
                        flag=False
                    print("\n")

                print("þú valdir ",valmynd[val],"sem er ",hlutur1[val])#prentar út það sem valið er
                print("\n")
                print("tölvan dregur spil ")
                print("Hrúturinn heitir ", hlutur2[0],"og hefur ",valmynd[val]," ",hlutur2[val])
                print("\n")

                if hlutur1[val] > hlutur2[val]:#ef þú ert með hærri einkunn

                    print("hrúturinn þinn var með hærri einkunn og þarmeð eignast þú hrútinn ",hlutur2[0])
                    player1.append(player2[0])#bætir við hjá þer
                    player1.append(player1[0])
                    player1.remove(player1[0])
                    player2.remove(player2[0])#eyðir hjá hinum
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))
                    if len(geymsla)!=0:# ef eitthver spil eru i geymslu eftir jafntefli
                        for x in geymsla:
                            player1.append(x)
                        print("og þú vannst", fj, "hrúta úr jafnteflinu")
                        geymsla=[]



                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))
                    print("\n")

                if hlutur1[val]==hlutur2[val]:
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))
                    geymsla.append(player1[0])
                    geymsla.append(player2[0])
                    player1.remove(player1[0])
                    player2.remove(player2[0])
                    print("þið voruð jafnir", hlutur1[0], " var með ", hlutur1[val], " og ", hlutur2[0], "var með",hlutur2[val])

                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))

                    print(geymsla)

                    p=1

                if hlutur2[val] > hlutur1[val]:
                    print("hrútur tölvunar var með hærri einkunn og þarmeð eignast hún hrútinn ", hlutur1[0])
                    player2.append(player1[0])  # bætir við hjá þer
                    player2.append(player2[0])
                    player2.remove(player2[0])
                    player1.remove(player1[0])  # eyðir hjá hinum
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))

                    if len(geymsla)!=0:
                        for x in geymsla:
                            player2.append(x)
                        print("og þú vannst",fj,"hrúta úr jafnteflinu")
                        geymsla = []


                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))
                    print("\n")
                    tkast=2




            elif tkast==2:
                flag = True
                fj = len(geymsla)
                gera=input("tölvan á að gera og dregur spil..(ýttu á 3 til að halda áfram)")  # valmynd fyrir spilin
                print("\n")
                print("Hrúturinn heitir ", player2[0].n)
                print("1.Þyng í kílóum ", player2[0].t)
                print("2.Mjólkurlagni dætra ", player2[0].mj)
                print("3.Einkunn ullar ", player2[0].u)
                print("4.Fjöldi afkvæma ", player2[0].bo)
                print("5.Einkunn læris", player2[0].l)
                print("6.Frjósemi ", player2[0].g)
                print("7.Gerð/Þykkt bakvöðva ", player2[0].ba)
                print("8.Einkunn fyrir malir", player2[0].ma)
                print("\n")
                val =randint(1,8)
                print("\n")

                print("tölvan valdi ", valmynd[val], "sem er ", hlutur2[val])  # prentar út það sem valið er
                print("\n")
                draga=input("ýttu á 3 til að draga spil ")
                print("Hrúturinn heitir ", hlutur1[0],"og hefur",valmynd[val]," ",hlutur1[val])
                print("\n")

                if hlutur2[val] > hlutur1[val]:
                    print("hrútur tölvunar var með hærri einkunn og þarmeð eignast hún hrútinn ", hlutur1[0])
                    player2.append(player1[0])  # bætir við hjá þer
                    player2.append(player2[0])
                    player2.remove(player2[0])
                    player1.remove(player1[0])  # eyðir hjá hinum
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))
                    if len(geymsla)!=0:
                        for x in geymsla:
                            player2.append(x)
                        print("og þú vannst", fj, "hrúta úr jafnteflinu")
                        geymsla = []

                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))
                    print("\n")

                if hlutur1[val]==hlutur2[val]:
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))
                    geymsla.append(player1[0])
                    geymsla.append(player2[0])
                    player1.remove(player1[0])
                    player2.remove(player2[0])

                    print("þið voruð jafnir",hlutur2[0]," var með ",hlutur2[val]," og ",hlutur1[0],"var með",hlutur1[val])


                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))




                if hlutur2[val] < hlutur1[val]:  # ef þú ert með hærri einkunn
                    print("hrúturinn þinn var með hærri einkunn og þarmeð eignast þú hrútinn ", hlutur2[0])
                    player1.append(player2[0])  # bætir við hjá þer
                    player1.append(player1[0])
                    player1.remove(player1[0])
                    player2.remove(player2[0])  # eyðir hjá hinum
                    print(len(geymsla))
                    print(len(player1))
                    print(len(player2))
                    if len(geymsla)!=0:
                        for x in geymsla:
                            player1.append(x)
                        print("og hún vann", fj, "hrúta úr jafnteflinu")
                        geymsla = []


                    print(len(player1))
                    print(len(player2))
                    print(len(geymsla))

                    print("\n")
                    tkast = 1


    elif val=="2":
        print("veldu fjölda spilara frá 2-5")
        fjoldi=int(input(">>"))
        afgangur=52%fjoldi
        lengd=len(stokkur)-afgangur

        skipta = deiling(fjoldi)  # deilt spilum milli spilara
        while lengd != 0:  # læt renna meðan stokkurinn er ekki tomur
            a = len(stokkur)  # hversu morg spil eru eftir í stokknum
            rt = randrange(0, a)  # random tala frá null og uppí fjölda spila
            nt = stokkur[rt]  # spilið sjálft
            if len(player1) < skipta:  # skipt spilum eftir fjölda spilara
                player1.append(hrutar[nt])  # fyrsti stokkur fær 26 random spil
                print(nt, end=" ")

            else:
                player2.append(hrutar[nt])  # annar stokkur fær 26 random spil

                print(nt, end=": ")

            del stokkur[rt]  # spilinu er eytt úr stokknum





















    else:
        print("úps eh fór úrskeiðis")











