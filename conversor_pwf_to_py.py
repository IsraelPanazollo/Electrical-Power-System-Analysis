import numpy as np

#Definir qual arquivo será convertido
nome = list(open("SIST5BARRAS.PWF","r"))      # Abrir na pasta o arquivo que será convertido
nome = [s.rstrip() for s in nome]             # Remove \n no fim de cada linha
A = np.array(nome)                            # Criar um vetor com o arquivo
#print(A)
n=len(A)                                      # Obtem o número de itens em A
#print(n)
B=A.T                                         # Realiza a transposição de A
#print(B)

#Separar cada termo
i=0
C=[]
E=[]                   # Matriz que receberá todos caracteres do arquivo
while(i<n):
    C = B[i]
    m=len(C)
    j=0
    linhaE = []
    while (j<m):
        linhaE.append(C[j])
        j = j + 1
    E.append(linhaE)
    i = i + 1
print(E)

#Escrevendo DBAR

K=[]            #vetor para receber o DBAR
i=4            #linha no pwf para começar a conversão
while(i<9):     #linha no pwf para terminar a conversão
    t=len(E[i])
    #print(t)
    # Número
    K1 = []
    N = [E[i][0], E[i][1], E[i][2], E[i][3], E[i][4]]   # Número de identificação da barra CA.
    #print(N)
    m = len(N)
    j = 0
    while (j < m):
        if N[j] != ' ':
            K1.append(N[j])
        j = j + 1
        Kr1= ''.join(K1)
    #print(Kr1)

    # Operação
    K2 = []
    if E[i][5] == ' ':
        K2.append('0')       # Valor padrão -> adição de dados de barra
    else:
        K2.append(E[i][5])
    #print(K2)

    # Estado
    K3 = []
    if E[i][6] == ' ':
        K3.append('0')      # Valor padrão -> barra está ligada
    else:
        K3.append(E[i][6])
    #print(K3)

    # Tipo
    K4 = []
    if E[i][7] == ' ':
        K4.append('0')      # Valor padrão -> Barra PQ
    else:
        K4.append(E[i][7])
    #print(K4)

    # Grupo Base de Tensão
    K5 = []
    GBT = [E[i][8], E[i][9]]
    # print(GBT)
    m = len(GBT)
    j = 0
    while (j < m):
        if GBT[j] != ' ':
            K5.append(GBT[j])
            #print(K5)
        j = j + 1
        Kr5= ''.join(K5)
        if len(K5) == 0:
            Kr5='0'
    #print(Kr5)
    #print(K5)

    # Nome
    K6 = []
    Nome = [E[i][10], E[i][11], E[i][12], E[i][13], E[i][14], E[i][15],
            E[i][16], E[i][17], E[i][18], E[i][19], E[i][20], E[i][21]]
    #print(Nome)
    m=len(Nome)
    j = 0
    while (j < m):
        if Nome[j] != ' ':
            K6.append(Nome[j])
        j = j + 1
        Kr6= ''.join(K6)
    #print(Kr6)

    # Grupo Limite de Tensão
    K7 = []
    GLT = [E[i][22], E[i][23]]
    # print(GLT)
    m = len(GLT)
    j = 0
    while (j < m):
        if GLT[j] != ' ':
            K7.append(GLT[j])
        j = j + 1
        Kr7= ''.join(K7)
    if len(K7) == 0:
        Kr7='0'

    # Tensão

    K8 = []
    T = [E[i][24], E[i][25], E[i][26], E[i][27]]
    # print(T)
    m = len(T)
    j = 0
    while (j < m):
        if T[j] != ' ':
            K8.append(T[j])
        j = j + 1
        Kr8= ''.join(K8)
    if len(K8) == 0:
        Kr8='0.'
    #print(Kr8)

    # Ângulo

    K9 = []
    Ang = [E[i][28], E[i][29], E[i][30], E[i][31]]
    # print(Ang)
    m = len(Ang)
    j = 0
    while (j < m):
        if Ang[j] != ' ':
            K9.append(Ang[j])
        j = j + 1
        Kr9= ''.join(K9)
    if len(K8) == 0:
        Kr9='0.'
    #print(Kr9)

    # Geração Ativa
    K10 = []
    Gat = [E[i][32], E[i][33], E[i][34], E[i][35], E[i][36]]
    # print(Gat)
    m = len(Gat)
    j = 0
    while (j < m):
        if Gat[j] != ' ':
            K10.append(Gat[j])
        j = j + 1
        Kr10= ''.join(K10)
    if len(K10) == 0:
        Kr10='0.'
    #print(Kr10)

    # Geração Reativa
    K11 = []
    Grat = [E[i][37], E[i][38], E[i][39], E[i][40], E[i][41]]
    m = len(Grat)
    j = 0
    while (j < m):
        if Grat[j] != ' ':
            K11.append(Grat[j])
        j = j + 1
        Kr11= ''.join(K11)
    if len(K11) == 0:
        Kr11='0.'
    #print(Kr11)

    # Geração Reativa Mínima
    K12 = []
    Grmin = [E[i][42], E[i][43], E[i][44], E[i][45], E[i][46]]
    # print(Grmin)
    m = len(Grmin)
    j = 0
    while (j < m):
        if Grmin[j] != ' ':
            K12.append(Grmin[j])
        j = j + 1
        Kr12= ''.join(K12)
    if len(K12) == 0:
        Kr12='0.'
    #print(Kr12)

    # Geração Reativa Máxima
    K13 = []
    Grmax = [E[i][47], E[i][48], E[i][49], E[i][50], E[i][51]]
    # print(Grmax)
    m = len(Grmax)
    j = 0
    while (j < m):
        if Grmax[j] != ' ':
            K13.append(Grmax[j])
        j = j + 1
        Kr13= ''.join(K13)
    if len(K13) == 0:
        Kr13='0.'
    #print(Kr13)

    # Barra Controlada
    K14 = []
    Bctrl = [E[i][52], E[i][53], E[i][54], E[i][55], E[i][56], E[i][57]]
    # print(Bctrl)
    m = len(Bctrl)
    j = 0
    while (j < m):
        if Bctrl[j] != ' ':
            K14.append(Bctrl[j])
        j = j + 1
        Kr14= ''.join(K14)
    if len(K14) == 0:
        Kr14='0.'
    #print(Kr14)

    # Carga Ativa
    K15 = []
    Cat = [E[i][58], E[i][59], E[i][60], E[i][61], E[i][62]]
    # print(Cat)
    m = len(Cat)
    j = 0
    while (j < m):
        if Cat[j] != ' ':
            K15.append(Cat[j])
        j = j + 1
        Kr15= ''.join(K15)
    if len(K15) == 0:
        Kr15='0.'
    #print(Kr15)

    # Carga Reativa
    K16 = []
    Crat = [E[i][63], E[i][64], E[i][65], E[i][66], E[i][67]]
    # print(Crat)
    m = len(Crat)
    j = 0
    while (j < m):
        if Crat[j] != ' ':
            K16.append(Crat[j])
        j = j + 1
        Kr16= ''.join(K16)
    if len(K16) == 0:
        Kr16='0.'
    #print(Kr16)

    if t == 68:
        Kr17='0'
    else:
        # Capacitor Reator
        K17 = []
        Cp = [E[i][68], E[i][69], E[i][70], E[i][71], E[i][72]]
        # print(Cp)
        m = len(Cp)
        j = 0
        while (j < m):
            if Cp[j] != ' ':
                K17.append(Cp[j])
            j = j + 1
            Kr17 = ''.join(K17)
        if len(K17) == 0:
            Kr17 = '0.'
        # print(Kr17)

    Kr18 = '0'
    Kr19 = '0'

    if t > 73:
        # Área
        K18 = []
        Area = [E[i][73], E[i][74], E[i][75]]
        # print(Area)
        m = len(Area)
        j = 0
        while (j < m):
            if Area[j] != ' ':
                K18.append(Area[j])
            j = j + 1
            Kr18 = ''.join(K18)
        if len(K18) == 0:
            Kr18 = '0.'
        # print(Kr18)

    if t > 76:
        # Tensão para definição de Carga
        K19 = []
        Tencar = [E[i][76], E[i][77], E[i][78], E[i][79]]
        # print(Tencar)
        m = len(Tencar)
        j = 0
        while (j < m):
            if Tencar[j] != ' ':
                K19.append(Tencar[j])
            j = j + 1
            Kr19 = ''.join(K19)
        if len(K19) == 0:
            Kr19 = '0.'
        # print(Kr19)

    Klinha = [Kr1, K2[0], K3[0], K4[0], Kr5, Kr6, Kr7, Kr8, Kr9, Kr10, Kr11, Kr12, Kr13, Kr14,
              Kr15, Kr16, Kr17, Kr18, Kr19]
    #print(Klinha)

    K.append(Klinha)
    i=i+1

DBAR=K
print(DBAR)

##Escrevendo DLIN

K=[]             #vetor para receber o DLIN
i=12             #linha no pwf para começar a conversão
while(i<18):     #linha no pwf para terminar a conversão
    t=len(E[i])
    #print(t)
    # Da barra
    K1 = []
    DBarra = [E[i][0], E[i][1], E[i][2], E[i][3], E[i][4]]
    #print(N)
    m = len(DBarra)
    j = 0
    while (j < m):
        if DBarra[j] != ' ':
            K1.append(DBarra[j])
        j = j + 1
        Kr1= ''.join(K1)
    #print(Kr1)

    # Abertura da Barra
    K2 = []
    if E[i][5] == ' ':
        K2.append('L')
    else:
        K2.append(E[i][5])
    #print(K2)

    # Nenhum 07
    K3 = ['0']
    #print(K3)

    # Operação
    K4 = []
    if E[i][7] == ' ':
        K4.append('A')
    else:
        K4.append(E[i][7])
    #print(K4)

    # Nenhum 09
    K5 = ['0']
    #print(K5)

    # Abertura para Barra
    K6 = []
    if E[i][9] == ' ':
        K6.append('L')
    else:
        K6.append(E[i][9])
    #print(K6)

    # Para Barra
    K7 = []
    PBarra = [E[i][10], E[i][11], E[i][12],E[i][13],E[i][14]]
    # print(PBarra)
    m = len(PBarra)
    j = 0
    while (j < m):
        if PBarra[j] != ' ':
            K7.append(PBarra[j])
        j = j + 1
        Kr7= ''.join(K7)
        if len(K7) == 0:
            Kr7='0'
    #print(Kr7)
    #print(K7)

    #Circuito
    K8 = []
    Circ = [E[i][15], E[i][16]]
    # print(Circ)
    m = len(Circ)
    j = 0
    while (j < m):
        if Circ[j] != ' ':
            K8.append(Circ[j])
        j = j + 1
        Kr8= ''.join(K8)
        if len(K8) == 0:
            Kr8='0'
    #print(Kr8)

    #Estado
    K9 = []
    if E[i][17] == ' ':
        K9.append('L')
    else:
        K9.append(E[i][17])
    #print(K9)

    #Proprietário
    K10 = []
    if E[i][18] == ' ':
        K10.append('F')
    else:
        K10.append(E[i][18])
    #print(K10)

    #Nenhum 20
    K11 = ['0']
    #print(K11)

    #Resistência
    K12 = []
    R = [E[i][20], E[i][21], E[i][22],E[i][23],E[i][24],E[i][25]]
    # print(R)
    m = len(R)
    j = 0
    while (j < m):
        if R[j] != ' ':
            K12.append(R[j])
        j = j + 1
        Kr12= ''.join(K12)
        if len(K12) == 0:
            Kr12='0'
    #print(Kr12)
    #print(K12)

    #Reatância
    K13 = []
    X = [E[i][26], E[i][27], E[i][28],E[i][29],E[i][30],E[i][31]]
    # print(X)
    m = len(X)
    j = 0
    while (j < m):
        if X[j] != ' ':
            K13.append(X[j])
        j = j + 1
        Kr13= ''.join(K13)
        if len(K13) == 0:
            Kr13='0'
    #print(Kr13)
    #print(K13)

    Kr14 = '0'
    Kr15 = '0'
    Kr16 = '0'
    Kr17 = '0'
    Kr18 = '0'
    Kr19 = '0'
    Kr20 = '0'
    Kr21 = '0'
    Kr22 = '0'
    Kr23 = '0'

    if t > 32:
        # Susceptância
        K14 = []
        S = [E[i][32], E[i][33], E[i][34], E[i][35], E[i][36], E[i][37]]
        # print(S)
        m = len(S)
        j = 0
        while (j < m):
            if S[j] != ' ':
                K14.append(S[j])
            j = j + 1
            Kr14 = ''.join(K14)
            if len(K14) == 0:
                Kr14 = '0'
        # print(Kr14)
        # print(K14)

    if t > 38:
        # Tap
        K15 = []
        Tap = [E[i][38], E[i][39], E[i][40], E[i][41], E[i][42]]
        # print(Tap)
        m = len(Tap)
        j = 0
        while (j < m):
            if Tap[j] != ' ':
                K15.append(Tap[j])
            j = j + 1
            Kr15 = ''.join(K15)
            if len(K15) == 0:
                Kr15 = '0'
        # print(Kr15)
        # print(K15)

    if t > 43:
        # Tap mínimo
        K16 = []
        Tapmin = [E[i][43], E[i][44], E[i][45], E[i][46], E[i][47]]
        # print(Tapmin)
        m = len(Tapmin)
        j = 0
        while (j < m):
            if Tapmin[j] != ' ':
                K16.append(Tapmin[j])
            j = j + 1
            Kr16 = ''.join(K16)
            if len(K16) == 0:
                Kr16 = '0'
        # print(Kr16)
        # print(K16)

    if t > 48:
        # Tap máximo
        K17 = []
        Tapmax = [E[i][48], E[i][49], E[i][50], E[i][51], E[i][52]]
        # print(Tapmax)
        m = len(Tapmax)
        j = 0
        while (j < m):
            if Tapmax[j] != ' ':
                K17.append(Tapmax[j])
            j = j + 1
            Kr17 = ''.join(K17)
            if len(K17) == 0:
                Kr17 = '0'
        # print(Kr17)
        # print(K17)

    if t > 53:
        # Defasagem
        K18 = []
        Dfsg = [E[i][53], E[i][54], E[i][55], E[i][56], E[i][57]]
        # print(Dfsg)
        m = len(Dfsg)
        j = 0
        while (j < m):
            if Dfsg[j] != ' ':
                K18.append(Dfsg[j])
            j = j + 1
            Kr18 = ''.join(K18)
            if len(K18) == 0:
                Kr18 = '0'
        # print(Kr18)
        # print(K18)

    if t > 58:
        # Barra controlada
        K19 = []
        Bctrlv = [E[i][58], E[i][59], E[i][60], E[i][61], E[i][62], E[i][63]]
        # print(Bctrlv)
        m = len(Bctrlv)
        j = 0
        while (j < m):
            if Bctrlv[j] != ' ':
                K19.append(Bctrlv[j])
            j = j + 1
            Kr19 = ''.join(K19)
            if len(K19) == 0:
                Kr19 = '0'
        # print(Kr19)
        # print(K19)

    if t > 64:
        # Capacidade Normal
        K20 = []
        Cnorm = [E[i][64], E[i][65], E[i][66], E[i][67]]
        # print(Cnorm)
        m = len(Cnorm)
        j = 0
        while (j < m):
            if Cnorm[j] != ' ':
                K20.append(Cnorm[j])
            j = j + 1
            Kr20 = ''.join(K20)
            if len(K20) == 0:
                Kr20 = '0'
        # print(Kr20)
        # print(K20)

    if t > 68:
        # Capacidade em Emergência
        K21 = []
        Cemer = [E[i][68], E[i][69], E[i][70], E[i][71]]
        # print(Cemer)
        m = len(Cemer)
        j = 0
        while (j < m):
            if Cemer[j] != ' ':
                K21.append(Cemer[j])
            j = j + 1
            Kr21 = ''.join(K21)
            if len(K21) == 0:
                Kr21 = '0'
        # print(Kr21)
        # print(K21)

    if t > 72:
        # Número de taps
        K22 = []
        Ntap = [E[i][72], E[i][73]]
        # print(Ntap)
        m = len(Ntap)
        j = 0
        while (j < m):
            if Ntap[j] != ' ':
                K22.append(Ntap[j])
            j = j + 1
            Kr22 = ''.join(K22)
            if len(K22) == 0:
                Kr22 = '0'
        # print(Kr22)
        # print(K22)

    if t > 74:
        # Capacidade do equipamento
        K23 = []
        Cequi = [E[i][74], E[i][75], E[i][76], E[i][77]]
        # print(Cequi)
        m = len(Cequi)
        j = 0
        while (j < m):
            if Cequi[j] != ' ':
                K23.append(Cequi[j])
            j = j + 1
            Kr23 = ''.join(K23)
            if len(K23) == 0:
                Kr23 = '0'
        # print(Kr23)
        # print(K23)

    Klinha = [Kr1, K2[0], K4[0], K6[0], Kr7, Kr8, K9[0], K10[0], Kr12, Kr13, Kr14,
              Kr15, Kr16, Kr17, Kr18, Kr19, Kr20, Kr21, Kr22, Kr23]
    K.append(Klinha)
    i = i + 1
    # print(Klinha)

DLIN=K
print(DLIN)

#Escrevendo DGBT

K=[]             #vetor para receber o DGBT
i=1            #linha no pwf para começar a conversão
while(i<1):     #linha no pwf para terminar a conversão
    t=len(E[i])
    #print(t)
    # Grupo base de tensão
    K1 = []
    GB = [E[i][0], E[i][1]]
    #print(N)
    m = len(GB)
    j = 0
    while (j < m):
        if GB[j] != ' ':
            K1.append(GB[j])
        j = j + 1
        Kr1= ''.join(K1)
        if len(Kr1) == 0:
            Kr1 = '0'
    #print(Kr1)

    # Tensão
    K2 = []
    Tas = [E[i][3], E[i][4], E[i][5], E[i][6], E[i][7]]
    #print(N)
    m = len(Tas)
    j = 0
    while (j < m):
        if Tas[j] != ' ':
            K2.append(Tas[j])
        j = j + 1
        Kr2= ''.join(K2)
        if len(Kr2) == 0:
            Kr2 = '1'
    #print(Kr2)
    Klinha = [Kr1, Kr2]
    #print(Klinha)
    K.append(Klinha)
    i=i+1

DGBT=K
print(DGBT)


