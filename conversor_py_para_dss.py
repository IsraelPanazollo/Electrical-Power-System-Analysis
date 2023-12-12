import numpy as np
import math

# INSERINDO DBAR

DBAR = np.array([["1","0","L","2","69","Atlantic-69","5","1020","-58.","0.","-.238","-9999","99999","0","0","0","0","1","1000"],
["50048","0","L","0","69","ENT936----69","0","1020","-58.","0.","0.","0","0","0.","10.","2.","0","1","1000"],
["50052","0","L","0","69","ENT804C---69","0","1020","-58.","0","0","0","0","0","5.","1.","0","1","1000"],
["50058","0","L","0","69","ENT804B---69","0","1020","-58.","0","0","0","0","0","6.","1.","0","1","1000"],
["50066","0","L","0","69","EN804A---69","0","1020","-58.","0","0","0","0","0","0","0","0","1","1000"]])

# INSERINDO DLIN

DLIN = np.array([["1","0","0","0","50048","1","0","0","3.55","10.317",".175","0","0","0","0","0","75.","90.","75."],
["1","0","0","0","50052","1","0","0",".372","1.06",".018","0","0","0","0","0","75.","90.","75."],
["1","0","0","0","50058","1","0","0",".372","1.06",".018","0","0","0","0","0","75.","90.","75."],
["1","0","0","0","50066","1","0","0",".372","1.06",".018","0","0","0","0","0","75.","90.","75."]])

# INSERINDO DCTE

DCTE =np.array([["Base", "100."]])      # Valor da base de potência

# INSERINDO DGBT

DGBT = np.array([["69","69."]])

#BASE DE POTÊNCIA

if 'DCTE' in globals():                  # verifica se existe DCTE
    Sbase=float(DCTE[0][1])*1E6          # extrai o valor da base de potência do DCTE
else:
    Sbase=100E6                          # coloca um valor padrão de 100 MVA

#DEFININDO CIRCUIT

sizedbar=len(DBAR)                       # obtém o tamanho da DBAR
sizedlin=len(DLIN)                       # obtém o tamanho da DLIN
i = 0

while (i<sizedbar):
    if DBAR[i][3] == "2":                           # verifica se a barra é Vtheta
        if DBAR[i][2] == "L" or DBAR[i][2] == "0":  # verifica se a barra está ligada
            linha = i
            i=sizedbar+1
    i=i+1

bus=DBAR[linha][0]               # recebe o número da barra Vtheta
nome=DBAR[linha][5]              # recebe o nome da barra Vtheta
ang=float(DBAR[linha][8])        # recebe o ângulo da barra Vtheta
pu=float(DBAR[linha][7])/1000    # recebe o valor em pu da barra Vtheta

# BASE DE TENSÃO DA BARRA VTHETA

sizedgbt = 0

if 'DGBT' in globals():                          # verifica se existe DGBT
    sizedgbt = len(DGBT)                         # obtém o tamanho de DGBT
    i=0
    if DBAR[linha][4] == '0':                    # verifica se o valor de base de tensão é o padrão
        base = '1'                               # define o valor padrão de 1 kV para a base de tensão
    else:
        while (i < sizedgbt):
            if DBAR[linha][4] == DGBT[i][0]:     # verifica qual é o valor de base de tensão associado da barra
                base = DGBT[i][1]                # extrai o valor da base de tensão da tabela DBGT
            i = i + 1
else:
    base = '1'

#MATRIZ DE BASES DE TENSÃO

i=0
j=0
GB=[]                                       #vetor usado para criar a matriz das barras e suas tensões

if 'DGBT' in globals():
    while (i < sizedgbt):
        j=0
        while (j < sizedbar):
            if DBAR[j][4] == DGBT[i][0]:        # verifica qual é o valor de base de tensão associado da barra
                linhaGB = []
                linhaGB.append(DBAR[j][0])      # cria um vetor para associar uma base de tensão para cada barra
                linhaGB.append(DGBT[i][1])      # associa o valor da base tensão da tabela DBGT com a barra
                GB.append(linhaGB)
            elif DBAR[j][4] == '0':
                linhaGB = []
                linhaGB.append(DBAR[j][0])      # cria um vetor para associar uma base de tensão para cada barra
                linhaGB.append('1')             # associa o valor da base tensão padrão com a barra
                GB.append(linhaGB)
            j=j+1
        i = i + 1

else:
    while (j < sizedbar):
        DBAR[j][4] == '0'            # se o valor do DBAR para a base tensão é "0", colocar o padrão
        linhaGB = []
        linhaGB.append(DBAR[j][0])   # cria um vetor para associar uma base de tensão para cada barra
        linhaGB.append('1')          # associa o valor da base tensão padrão com a barra
        GB.append(linhaGB)
        j = j + 1

#TRAFO

i=0
j=0
traf=0
barradetr=[]    # Barra de origem do transformador
barraparatr=[]  # Barra de destino do transformador
XHL=[]          # Reatância do transformador
r=[]            # Resistência do transformador
tap=[]          # Tap do transformador
numtap=[]       # Número de taps do transformador
Strafo=[]       # Potência em kVA do transformador
sizeGB=len(GB)  # Tamanho da matriz de Base de Tensão
GB2=[]          # Base de tensão secundária do trafo

while (i<sizedlin):
    if DLIN[i][11] != '0':                             # verifica se não tem TAP e caso tenha TAP é um trafo
        if DLIN[i][6] == 'L' or DLIN[i][6] == '0':     # verifica se a linha está ligada
            traf=1
            barradetr.append(DLIN[i][0])
            barraparatr.append(DLIN[i][4])
            base2=float(DLIN[i][4])
            k=0
            while(k<sizeGB):
                if base2 == float(GB[k][0]):
                    GB2.append(GB[k][1])
                k=k+1
            XHL.append(DLIN[i][9])                 # obtém a reatância do transformador
            r.append(float(DLIN[i][8]))            # obtém a resistência do transformador
            tap.append(DLIN[i][11])                # obtém o tap do transformador
            numtap.append(DLIN[i][18])             # obtém o número de taps do transformador
            if DLIN[i][16] != '0':
                Strafo.append(float(DLIN[i][16])*1000) # obtém a potência do transformador
            else:
                Strafo.append('100000')            # define a potência do transformador como padrão
            j=j+1
    i=i+1

if traf == 1:
    traf = len(barradetr)

#LINHA

i=0
lin=0
barrade=[]     # Barra de origem da linha
barrapara=[]   # Barra de destino da linha

while (i<sizedlin):
    if DLIN[i][11] == '0':                            # verifica se não tem TAP
        if DLIN[i][6] == 'L' or DLIN[i][6] == '0':    # verifica se a linha está ligada
            lin=1
            barrade.append(DLIN[i][0])              # obtém a barra onde está conectada (bus 1)
            barrapara.append(DLIN[i][4])            # obtém a barra onde está conectada (bus 2)
    i=i+1

if lin == 1:                         # usado para verificar se há linha e caso haja, quantas são
    lin = len(barrade)


# LINECODE

i=0
j=0
k=0
linecode=0
cabo=[]    # Número do cabo
R1=[]      # Resistência do cabo em Ohm
X1=[]      # Reatância do cabo em Ohm

while (i<sizedlin):
    if DLIN[i][11] == '0':                            # verifica se não tem TAP
        if DLIN[i][6] == 'L' or DLIN[i][6] == '0':    # verifica se a linha está ligada
            linecode=1
            cabo.append(i)
            k=0
            while (k<sizedbar):
                if barrade[j]==GB[k][0]:
                    zbase = ((float(GB[k][1])*1000)**2)/(Sbase)/100 # obtêm a base para essa barra
                    r1= float(DLIN[i][8]) * zbase   # obtém a resistência positiva da linha
                    x1= float(DLIN[i][9])* zbase    # obtém a reatância positiva da linha
                    R1.append(r1)
                    X1.append(x1)
                k=k+1
            j=j+1
    i=i+1

if linecode == 1:                    # usado para verificar se há linecode e caso haja, quantos são
    linecode = len(cabo)

# CARGA

i=0
cg=0
nomecarga=[]   # Nome da carga
barracarga=[]  # Barra da carga
carga=[]       # Potência ativa da carga
cargar=[]      # Potência reativa da carga
FPcar=[]       # Fator de potência do gerador

while (i<sizedbar):
    if DBAR[i][14] != '0' or DBAR[i][15] != '0':        # verifica se a barra possui uma carga ativa
        if DBAR[i][14] != '0.'or DBAR[i][15] != '0.':   # verifica se a barra possui uma carga reativa
            if DBAR[i][2] == 'L' or DBAR[i][2] == '0':  # verifica se a barra está ligada
                cg = 1
                nomecarga.append(i)  # define o nome da carga
                barracarga.append(DBAR[i][0])  # obtém a barra onde a carga está conectada
                carga.append(float(DBAR[i][14]) * 1E3)  # obtém a Potência Ativa consumida pela carga
                cargar.append(float(DBAR[i][15]) * 1E3)  # obtém a Potência Reativa consumida pela carga
                if float(DBAR[i][15]) == 0.0:  # caso não haja potência ativa
                    FPcar.append('1')  # define o valor de FP=1
                else:
                    FPcar.append(math.cos(math.atan((float(DBAR[i][15]) / float(DBAR[i][14])))))  # obtém o FP da carga
    i = i + 1

linhascarga = len(barracarga)

if cg == 1:                         # usado para verificar se há carga e caso haja, quantas são
    cg = len(barracarga)

#GERADOR

i = 0
ger=0
nomeger=[]    # Nome do gerador
barrager=[]   # Barra do gerador
Pger=[]       # Potência ativa do gerador
Qger=[]       # Potência reativa do gerador
FP=[]         # Fator de potência do gerador

while (i<sizedbar):
    if DBAR[i][3]=='1':                                # verifica se a barra é PV
        if DBAR[i][2]=='L' or DBAR[i][2]=='0':         # verifica se a barra está ligada
                ger=1
                nomeger.append(i)                      # define o nome do gerador
                barrager.append((DBAR[i][0]))          # obtém a barra onde o gerador está conectado
                Qger.append(float(DBAR[i][10])*1E3)    # obtém a Potência Reativa do Gerador
                if float(DBAR[i][9]) == 0.0:           # caso não haja potência ativa
                    FP.append('1')                     # define o valor de FP=1
                    Pger.append('0.00001')             # define o valor de uma potência muito pequena
                else:
                    Pger.append(float(DBAR[i][9]) * 1E3)    # obtém a Potência Ativa do Gerador
                    FP.append(math.cos(math.atan((float(DBAR[i][10])/float(DBAR[i][9])))))  # obtém o FP do Gerador
    i = i+1

linhasger = len(barrager)

if ger == 1:                         # usado para verificar se há gerador e caso haja, quantos são
    ger = len(barrager)

#CAPACITOR

i = 0
j = 0
caps = 0
barradecap = []      # barra do capacitor
mvar = []            # potência reativa do capacitor
GBcap = []           # tensão da barra do capacitor

while (i<sizedlin):
    if DLIN[i][10] != '0':          # verifica se tem susceptância
        caps = 1
        barradecap.append(DLIN[i][0])          # obtém a barra onde o capacitor está conectado
        GBcap.append(GB[i][1])                 # obtém a tensão da barra onde o capacitor está
        mvar.append(float(DLIN[i][10])*1000)   # obtém a potência reativa do capacitor
    i = i + 1

if caps == 1:                       # usado para verificar se há capacitor e caso haja, quantos são
    cap = len(barradecap)
else: cap=0

# CALCVOLTAGE BASES

cvbt = []                    # vetor de tensões usados no voltagebases

for i in range(len(GB)):
    cvbt.append(GB[i][1])
cvb = sorted(set(cvbt))      # vetor ordenado e sem repetições das tensões usadas no voltagebases
cvbn=len(cvb)                # cvbn recebe o tamanho do vetor cvb

#DOCUMENTO

#arquivo = open("nbarras.dss","w")  # cria um dss na pasta onde está o código
arquivo = open("nbarras.txt","w")  # cria um txt na pasta onde está o código

arquivo.write("Clear \n\n")

arquivo.write("// ------------------------------- Novo Circuito --------------------------------- \n\n")

arquivo.write("New circuit.")
arquivo.write(nome)
arquivo.write(" bus1=")
arquivo.write(bus)
arquivo.write(" baseMVA=")
arquivo.write('{:.6}'.format(Sbase/1e6))
arquivo.write(" basekv=")
arquivo.write('{:.6}'.format(base))
arquivo.write(" angle=")
arquivo.write('{:.6}'.format(ang))
arquivo.write(" pu=")
arquivo.write('{:.6}'.format(pu))
arquivo.write(" phases=3 frequency=60 \n\n")

i=0
if traf>0:
    arquivo.write("// ------------------------------- Transformador -------------------------- \n\n")
while (i<traf):
    arquivo.write("New transformer.TR")
    arquivo.write('{}'.format(i))
    arquivo.write(" XHL=")
    arquivo.write('{:.6}'.format(XHL[i]))
    arquivo.write(" %r=")
    arquivo.write('{:.6}'.format(r[i]/2))
    arquivo.write(" numtaps=")
    arquivo.write('{:.6}'.format(numtap[i]))
    arquivo.write(" windings=2 \n")
    arquivo.write("~ wdg=1 bus=")
    arquivo.write(barradetr[i])
    arquivo.write(" tap=")
    arquivo.write('{:.6}'.format(tap[i]))
    arquivo.write(" conn=wye kv=")
    arquivo.write(GB[i][1])
    arquivo.write(" kva=")
    arquivo.write('{:.6}'.format(Strafo[i]))
    arquivo.write(" \n")
    arquivo.write("~ wdg=2 bus=")
    arquivo.write(barraparatr[i])
    arquivo.write(" conn=wye kv=")
    arquivo.write(GB2[i])
    arquivo.write(" kva=")
    arquivo.write('{:.6}'.format(Strafo[i]))
    arquivo.write(" \n\n")
    i=i+1

i=0
if linecode>0:
    arquivo.write("// -------------------------- Linecode --------------------------------\n\n")
while (i<linecode):
    arquivo.write("New Linecode.Cabo")
    arquivo.write('{}'.format(cabo[i]))
    arquivo.write(" R1=")
    arquivo.write('{:.6}'.format(R1[i]))
    arquivo.write(" X1=")
    arquivo.write('{:.6}'.format(X1[i]))
    arquivo.write("Units=km \n\n")
    i=i+1

i=0
if lin>0:
    arquivo.write("// ----------------------------- Linhas ----------------------------------------------\n\n")
while (i<lin):
    arquivo.write("New Line.L")
    arquivo.write('{}'.format(i))
    arquivo.write(" bus1=")
    arquivo.write(barrade[i])
    arquivo.write(" bus2=")
    arquivo.write(barrapara[i])
    arquivo.write(" linecode=Cabo")
    arquivo.write('{}'.format(cabo[i]))
    arquivo.write(" length=1 units=km \n\n")
    i=i+1

i=0
if cg>0:
    arquivo.write("// ----------------------------- Cargas ----------------------------------------------\n\n")
while (i<cg):
    arquivo.write("New load.C")
    arquivo.write('{}'.format(nomecarga[i]))
    arquivo.write(" bus1=")
    arquivo.write(barracarga[i])
    arquivo.write(" kv=")
    arquivo.write('{:.6}'.format(GB[i][1]))
    arquivo.write(" kw=")
    arquivo.write('{:.6}'.format(carga[i]))
    arquivo.write(" kvar=")
    arquivo.write('{:.6}'.format(cargar[i]))
    arquivo.write(" pf=")
    arquivo.write('{:.6}'.format(FPcar[i]))
    arquivo.write(" phases=3 \n\n")
    i=i+1

i=0
if ger>0:
    arquivo.write("// ----------------------------- Gerador ----------------------------------------------\n\n")
while (i<ger):
    arquivo.write("New generator.G")
    arquivo.write('{}'.format(nomeger[i]))
    arquivo.write(" bus1=")
    arquivo.write(barrager[i])
    arquivo.write(" kv=")
    arquivo.write(GB[i][1])
    arquivo.write(" kw=")
    arquivo.write('{:.7}'.format(Pger[i]))
    arquivo.write(" kvar=")
    arquivo.write('{:.6}'.format(Qger[i]))
    arquivo.write(" model=1 phases=3 \n\n")
    i=i+1

i=0
if caps>0:
    arquivo.write("// ----------------------------- Capacitor ----------------------------------------------\n\n")
while (i<cap):
    arquivo.write("New capacitor.CAP")
    arquivo.write('{}'.format(i))
    arquivo.write(" bus1=")
    arquivo.write(barradecap[i])
    arquivo.write(" kv=")
    arquivo.write('{:.6}'.format(GBcap[i]))
    arquivo.write(" kvar=")
    arquivo.write('{:.6}'.format(mvar[i]))
    arquivo.write(' phases=3')
    arquivo.write(" \n\n")
    i=i+1

arquivo.write("// ------------------------------------ Tipo de Solução --------------------------\n\n")
arquivo.write("Set mode=snapshot \n\n")

arquivo.write("// -------------------------------- Valores bases de tensão --------------------------\n\n")
i=0
arquivo.write("Set voltagebases=[")
while (i<cvbn):
    arquivo.write(' {}'.format(cvb[i]))
    i=i+1
arquivo.write("] \n")
arquivo.write("calcvoltagebases \n\n")

arquivo.write("// ------------------------------------ Solucionar --------------------------\n\n")
arquivo.write("Solve\n")

arquivo.close()