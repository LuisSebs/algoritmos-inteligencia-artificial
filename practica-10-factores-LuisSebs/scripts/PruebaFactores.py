#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Factores import *

# Variables del problema

MA = Variable("MA", [0,1])
MP = Variable("MP", [0,1])
AA = Variable("AA", [0,1])
AP = Variable("AP", [0,1])
JA = Variable("JA", [0,1])
JP = Variable("JP", [0,1])
BA = Variable("BA", [0,1])
BP = Variable("BP", [0,1])
LI = Variable("LI", [0,1])
LF = Variable("LF", [0,1])
FIN = Variable("FIN", [0,1])
E = Variable("E", [0,1])
IT = Variable("IT", [0,1])
VP = Variable("VP", [0,1])

pLF = Factor((LF,), [0.78,0.22])
pLI = Factor((LI,), [0.78,0.22])
pFIN = Factor((FIN,), [0.72,0.28])
pIT = Factor((IT,), [0.7,0.3])
pE = Factor((E,), [0.35,0.65])
pJA_LI = Factor((JA,LI), [0.1,0.6,0.9,0.4])
pAA_FIN = Factor((AA,FIN), [0.6,0.2,0.4,0.8])
pBA_IT = Factor((BA,IT), [0.05,0.7,0.95,0.3])
pMP_MA = Factor((MP,MA), [0.97,0.03,0.03,0.97])
pAP_AA = Factor((AP,AA), [0.5,0.2,0.5,0.8])
pMA_JAAA = Factor((MA,JA,AA), [0.5,0.15,0.05,0.95,0.5,0.85,0.95,0.05])
pVP_AABA = Factor((VP,AA,BA), [0.3,0.6,0.1,0.0,0.7,0.4,0.9,1.0])
pJP_JALF = Factor((JP,JA,LF), [0.6,1.0,0.1,0.3,0.4,0.0,0.9,0.7])
pBP_BAE = Factor((BP,BA,E), [0.8,1.0,0.05,1.0,0.2,0.0,0.95,0.0])

def pLuviaInv_NoMayNoFin():
    print("P(li|¬mp,¬fin)")
    Prob = pAA_FIN.reduce(FIN,0)
    Prob = pMA_JAAA.multiply(Prob)
    Prob = Prob.marginalize(AA)
    Prob = pMP_MA.reduce(MP,0).multiply(Prob)
    Prob = Prob.marginalize(MA)
    Prob = pJA_LI.multiply(Prob)
    Prob = Prob.marginalize(JA)
    Prob = pLI.multiply(Prob)
    Prob = Prob.normalize()
    print("Resultado = ", Prob)
    
if __name__ == '__main__':
    pLuviaInv_NoMayNoFin()
