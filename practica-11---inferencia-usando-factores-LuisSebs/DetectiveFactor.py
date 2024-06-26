# -*- coding: utf-8 -*-
"""Practica11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nWR-KL3gBF2775iuSZCCg65KGQii_g1c

# Práctica 11: Inferencias en Redes de Bayes usando factores
### Autor:  Arrieta Mancera Luis Sebastian

### Factor.py
"""

from itertools import product
from Factores import Variable, Factor

"""## Antecedentes

Hace tres diás el diamante Colossus fue robado del museo de la Ciudad Ladrillos. El Agente Toño está a cargo del caso y cuenta con la siguiente información. Hay cinco personas sospechosas y se desea determinar quiénes participaron en el robo:

- Daniel
- Rita
- Joaquín
- Camelia
- Sam

de donde tendremos cinco variables aleatorias: **DP**, **RP**, **JP**, **CP**, **SP** correspondiendo a la inicial del nombre y la palabra "participó".
"""

# = Variables =

DP = Variable("DP", [0,1]) # Diego participo
RP = Variable("RP", [0,1]) # Rita participo
JP = Variable("JP", [0,1]) # Joaquin participo
CP = Variable("CP", [0,1]) # Camelia participo
SP = Variable("SP", [0,1]) # Sam participo

"""1. Tanto Daniel como joaquín suelen organizar robos de este tipo. De cada diez casos, Joaquín ha estado en siete y Daniel en cinco"""

fDP = Factor((DP,), [0.5,0.5]) # P(DP)
fJP = Factor((JP,), [0.3,0.7]) # P(JP)

print(fDP)
print(fJP)

"""2. Rita ha participando anteriormente en robos con Daniel y Joaquín, aunque se lleva mejor con Daniel. Además, el empleo E de Rita estaba en riesgo, aunque el reporte no indica si lo perdió o no; la probabilidad de que lo hubiera perdido era del 65 %. Cuando Daniel y Joaquín participaron, ella estuvo con el equipo el 90% de las
ocasiones, si sólo estaba Daniel el 80 %, si sólo estaba Joaquín, el 45 %, y nunca actúa sin alguno de ellos. Si Rita está ocupada con su empleo esas probabilidades se reducen a la mitad.

 **E** =  "Rita perdio el empleo"
"""

# Variables

E = Variable("E", [0,1]) # Rita perdio el empleo

fE = Factor((E,), [0.35,0.65]) # P(E)
fRP_DPJPE = Factor((E,JP,DP,RP), [1,0,0.6,0.4,1-((9/20)/2),(9/20)/2,0.55,0.45,1,0,0.2,0.8,0.55,0.45,0.1,0.9]) # P(RP|DP,JP,E)

print(fE)
print(fRP_DPJPE)

"""3. Se sabe que Sam es amigo de Rita, y no le gusta el empleo de Rita.Por lo que, con tal de que lo deje, si ella conservó el empleo la probabilidad de que hubiera participado es del 80% independientemente de que ella participara o no.Si Rita perdió el empleo y participó, la probabilidad de que Sam también estuviera involucrado es del 65 %, si ella no participó, es del 20 %."""

fSP_ERP = Factor((E,RP,SP), [0.2,0.8,0.2,0.8,0.8,0.2,0.35,0.65]) # P(SP|E,RP)
print(fSP_ERP)

"""4. El alarma del museo fue desactivada, esto se logra mediante el uso de alguno de tres dispositivos: A, B y C, de los cuales debieron haber elegido alguno (DiE = dispositivo elegido). Dependiendo de la pericia de su usuario, puede ser posible retirarlos antes de marcharse o no (DiA = dispositivo abandonado). Camelia trabaja en un laboratorio de electrónica donde se puede tener acceso a estos dispositivos y sabe muy bien cómo usarlos. Si ella participó existe una probabilidad del 20% de que un dispositivo de tipo A haya sido abandonado en el museo, sino, esta probabilidad es del 35 %; ella dejará del dispositivo B con el 40 %, mientras que otro lo hará con un 85 %; sólo en un 10% ella dejará un dispositivo C, mientras que otra persona lo dejára el 45% de la veces.

  **DiE** = "dispositivo elegido"

  **DiA** = "dispositivo abandonado"
"""

# Variables

DiE = Variable("DiE", ["A","B","C"]) # Dispositivo elegido
DiA = Variable("DiA", [0,1]) # Dispositivo abandonado

fDiA_CPDiE = Factor((CP,DiE,DiA), [0.65,0.35,0.15,0.85,0.55,0.45,0.8,0.2,0.6,0.4,0.9,0.1]) # P(DiA|CP,DiE)
print(fDiA_CPDiE)

"""5. Joaquín ha trabajado con Camelia en proyectos legales, existe una probabilidad del 15% de que Camelia hubiera aceptado participar en el robo sólo si Joaquín lo hizo y un 1% de que ella no hubiera participado y de hecho, ella hubiera ideado el robo. Si Joaquín no participó ella queda libre de toda sospecha pues no tendría ni conexión ni motivo para participar.


"""

fCP_JP = Factor((JP,CP), [1,0,0.85,0.15]) # P(CP|JP)
print(fCP_JP)

"""6. Independientemente de que Camelia haya estado ahí para usar el dispositivo, pudo haberse limitado a asesorar a los asaltantes (CA). Se sabe que Daniel la conoce y, de haber participado en el robo, hay un 50% de probabilidades de que le haya pedido asesoría. Si no participó, no hubo quien solicitara la asesoría.

  **CA** = "Camelia asesoró"
"""

# Variables

CA = Variable("CA", [0,1]) # Camelia asesoro

fCA_DP = Factor((DP,CA), [1,0,0.5,0.5]) # P(CA|DP)
print(fCA_DP)

"""7. Entonces, el dispositivo elegido DiE para el robo dependió de si Camelia dió asesoría o participó el robo. Si Camelia participó en el robo definitivamente eligió el dispositivo C, pero si dió asesoría para que lo usara otra persona habrá sugerido el dispositivo B, si no participó ni asesorando ni en persona, un no especialista había elegido el dispositivo A el 25% de las veces, el B el 40% pues es más comercial y el C el 35 %."""

fDiE_CACP = Factor((CA,CP,DiE), [0.25,0.4,0.35,0,0,1,0,1,0,0,0,1]) # P(DiE|CA,CP)
print(fDiE_CACP)

"""8. La probabilidad de encontrar un dispositivo en el museo DiM depende del dispositivo que haya sido elegido y de que éste sea abandonado por quien lo usó. Si un dispositivo tipo A fue abandonado hay un 97% de probabilidades de que la policía lo encuentre; 99% para un dispositivo B y 90% para un dispositivo C.

  **DiM** = "dispositivo en el museo"
"""

# Variables
DiM = Variable("DiM", [0,1]) # Dispositivo en el museo

fDiM_DiEDiA = Factor((DiE,DiA,DiM), [1,0,0.03,0.97,1,0,0.01,0.99,1,0,0.1,0.9]) # P(DiM|DiE,DiA)
print(fDiM_DiEDiA)

"""9. Para encontrar la ubicación U del diamante se consideran tres posibilidades:

- Sam tiene una caja de seguridad en el banco, si él participó el diamante podría estar ahí.
- Daniel es un mandón, pero algo imprudente, cuando ha participado en un robo frecuentemente los objetos han sido encontrados en su casa.
- A Joaquín no le gusta correr riesgos y considera que Daniel es muy descuidado, pero también es muy metódico. En ocasiones anteriores se ha encontrado el botín enterrado en un punto equidistante a las casas de todos los participantes.

  Si, de ellos tres, sólo Sam participó, el diamante estará en su caja de seguridad. Si Daniel participó, pero no Joaquín, hay un 80% de probabilidades de que esté en casa de Daniel, un 15% en la caja de Sam y un 5% de que le hayan copiado la idea a Joaquín. Si Joaquín participó, pero no Daniel, hay un 65% de probabilidad de que el diamante esté enterrado, un 30% de que esté en la caja y un 5% de que
  lo hayan sembrado en casa de Daniel. Si tanto Daniel como Joaquín estuvieron en el equipo, cualquiera de los tres lugares es igualmente probable... incluso si Sam no participó. Si ninguno de los tres participó la casa de Daniel sigue siendo un buen escondite con el 60 %, el punto central con 30% y la caja de Sam 10 %.

  **U** = "ubicación del diamante"
"""

# Variable

U = Variable("U", ["caja", "casa", "ente"]) # Ubicacion del diamante, valores: "casa", "caja", "enterrado"

fU_SPDPJP = Factor((SP,DP,JP,U), [0.1,0.6,0.3,
                                  0.3,0.05,0.65,
                                  0.15,0.8,0.05,
                                  1/3,1/3,1/3,
                                  1,0,0,
                                  0.3,0.05,0.65,
                                  0.15,0.8,0.05,
                                  1/3,1/3,1/3]) # P(U|SP,DP,JP)
print(fU_SPDPJP)

"""# Grafica de Bayes

"""

import networkx as nx
import matplotlib.pyplot as plt

# Definir las adyacencias de los nodos
grafo = {
    'DP': ['U', 'CA', 'RP'],
    'RP': ['SP'],
    'JP': ['U', 'RP', 'CP'],
    'CP': ['DiE', 'DiA'],
    'SP': ['U'],
    'E': ['RP', 'SP'],
    'DiE': ['DiA', 'DiM'],
    'DiA': ['DiM'],
    'CA': ['DiE'],
    'DiM': [],
    'U': [],
}

# Definir la posición de cada nodo manualmente
posiciones = {
    'DP': (4, 5),
    'RP': (5, 4),
    'JP': (2, 5),
    'CP': (0, 4),
    'SP': (5, 3),
    'E': (6, 5),
    'DiE': (2, 3),
    'DiA': (1, 2),
    'CA': (3, 4),
    'DiM': (2, 0),
    'U': (3, 0),
}

# Crear un grafo dirigido desde las adyacencias
G = nx.DiGraph(grafo)

# Dibujar el grafo
pos = posiciones  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', arrowsize=10)

# Mostrar el grafo
plt.title("Red de Bayes: Policias y Ladrones")
plt.show()

"""# P(U)
$P(U) = P(U|SP,JP,DP)P(SP|E,RP)P(RP|E,JP,DP)P(E)P(JP)P(DP)$
### Ecuacion1
$ = Σ_{SP,JP,DP,E,RP} P(U|SP,JP,DP)P(SP|E,RP)P(RP|E,JP,DP)P(E)P(JP)P(DP)$
### Ecuacion2
$ = Σ_{E}P(E)Σ_{RP,SP}P(SP|E,RP)Σ_{DP}P(DP)Σ_{JP}P(U|SP,JP,DP)P(RP|E,JP,DP)P(JP)$
"""

def ecuacion1():

  # Σ_{SP,JP,DP,E,RP} P(U|SP,JP,DP)P(SP|E,RP)P(RP|E,JP,DP)P(E)P(JP)P(DP)

  # Prob = P(JP) * P(DP)
  Prob = fJP.multiply(fDP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(E) * Prob
  Prob = fE.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(RP|E,JP,DP) * Prob
  Prob = fRP_DPJPE.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(SP|E,RP) * Prob
  Prob = fSP_ERP.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(U|SP,JP,DP) * Prob
  Prob = fU_SPDPJP.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))

  # Marginalizacion para Σ_{SP,JP,DP,E,RP}
  Prob = Prob.marginalize(RP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion para Σ_{SP,JP,DP,E}
  Prob = Prob.marginalize(E)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion para Σ_{SP,JP,DP}
  Prob = Prob.marginalize(DP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion para Σ_{SP,JP}
  Prob = Prob.marginalize(JP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion para Σ_{SP}
  Prob = Prob.marginalize(SP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))

  return Prob

def ecuacion2():

  # Σ_{E} P(E) * Σ_{RP,SP} P(SP|E,RP) * Σ_{DP} P(DP) * Σ_{JP} P(U|SP,JP,DP) P(RP|E,JP,DP) P(JP)

  # Prob = P(RP|E,JP,DP) * P(JP)
  Prob = fRP_DPJPE.multiply(fJP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(U|SP,JP,DP) * Prob
  Prob = fU_SPDPJP.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion Σ_{JP}
  Prob =  Prob.marginalize(JP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(DP) * Prob
  Prob = fDP.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion Σ_{DP}
  Prob = Prob.marginalize(DP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(SP|E,RP) * Prob
  Prob = fSP_ERP.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion Σ_{RP,SP}
  Prob = Prob.marginalize(SP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  Prob = Prob.marginalize(RP)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Prob = P(E) * Prob
  Prob = fE.multiply(Prob)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))
  # Marginalizacion Σ_{E}
  Prob = Prob.marginalize(E)
  print("Cantidad de renglones: {}".format(len(Prob.valores)))

  return Prob

"""5. Calcula la probabilidad de que:
  - Los cinco sospechosos hayan participado en el robo
  - Ninguno de ellos haya sido
"""

def consulta5A():

  print("Probabilidad de que los cinco sospechosos hayan participado en el robo")

  # Probabilidad de que los cinco sospechosos hayan participado:
  # P(dp,rp,jp,cp,sp) = \alpha P(dp)P(jp)P(cp|jp) \Sigma_{E}P(E)P(sp|rp,E)P(rp|dp,E) \Sigma_{CA}P(CA|dp) \Sigma_{DiE,DiA,DiM} P(DiE|cp,CA)P(DiA|cp,DiE)P(DiM|DiA,DiE)

  # \Sigma_{DiE,DiA,DiM} P(DiE|cp,CA)P(DiA|cp,DiE)P(DiM|DiA,DiE)
  Prob = fDiA_CPDiE.multiply(fDiM_DiEDiA)
  Prob = fDiE_CACP.multiply(Prob)
  Prob = Prob.marginalize(DiE).marginalize(DiA).marginalize(DiM)

  # \Sigma_{CA}P(CA|dp)
  Prob = fCA_DP.multiply(Prob)
  Prob = Prob.marginalize(CA)

  # \Sigma_{E}P(E)P(sp|rp,E)P(rp|dp,E)
  Prob = fRP_DPJPE.multiply(Prob)
  Prob = fSP_ERP.multiply(Prob)
  Prob = fE.multiply(Prob)
  Prob = Prob.marginalize(E)

  # P(dp)P(jp)P(cp|jp)
  Prob = fCP_JP.multiply(Prob)
  Prob = fJP.multiply(Prob)
  Prob = fDP.multiply(Prob)

  # Multiplicacion por \alpha
  Prob = Prob.normalize()

  p_dp = Prob.reduce(RP,1).reduce(JP,1).reduce(CP,1).reduce(SP,1).valores[1]
  p_rp = Prob.reduce(DP,1).reduce(JP,1).reduce(CP,1).reduce(SP,1).valores[1]
  p_jp = Prob.reduce(DP,1).reduce(RP,1).reduce(CP,1).reduce(SP,1).valores[1]
  p_cp = Prob.reduce(DP,1).reduce(RP,1).reduce(JP,1).reduce(SP,1).valores[1]
  p_sp = Prob.reduce(DP,1).reduce(RP,1).reduce(JP,1).reduce(CP,1).valores[1]

  print("La probabilidad de que todos hayan participado:\n P(dp)= {}\n P(rp)= {}\n P(jp)= {}\n P(cp)= {}\n P(sp)= {}".format(p_dp,p_rp,p_jp,p_cp,p_sp))
  return p_dp, p_rp, p_jp, p_cp, p_sp

def consulta5B():
  
  print("Probabilidad de que ninguno de ellos haya sido")

  # Probabilidad de que ninguno de los cinco sospechosos haya participado:
  # P(dp,rp,jp,cp,sp) = \alpha P(dp)P(jp)P(cp|jp) \Sigma_{E}P(E)P(sp|rp,E)P(rp|dp,E) \Sigma_{CA}P(CA|dp) \Sigma_{DiE,DiA,DiM} P(DiE|cp,CA)P(DiA|cp,DiE)P(DiM|DiA,DiE)

  # \Sigma_{DiE,DiA,DiM} P(DiE|cp,CA)P(DiA|cp,DiE)P(DiM|DiA,DiE)
  Prob = fDiA_CPDiE.multiply(fDiM_DiEDiA)
  Prob = fDiE_CACP.multiply(Prob)
  Prob = Prob.marginalize(DiE).marginalize(DiA).marginalize(DiM)

  # \Sigma_{CA}P(CA|dp)
  Prob = fCA_DP.multiply(Prob)
  Prob = Prob.marginalize(CA)

  # \Sigma_{E}P(E)P(sp|rp,E)P(rp|dp,E)
  Prob = fRP_DPJPE.multiply(Prob)
  Prob = fSP_ERP.multiply(Prob)
  Prob = fE.multiply(Prob)
  Prob = Prob.marginalize(E)

  #P(dp)P(jp)P(cp|jp)
  Prob = fCP_JP.multiply(Prob)
  Prob = fJP.multiply(Prob)
  Prob = fDP.multiply(Prob)

  # Multiplicacion por \alpha
  Prob = Prob.normalize()

  p_dp = Prob.reduce(RP,0).reduce(JP,0).reduce(CP,0).reduce(SP,0).valores[0]
  p_rp = Prob.reduce(DP,0).reduce(JP,0).reduce(CP,0).reduce(SP,0).valores[0]
  p_jp = Prob.reduce(DP,0).reduce(RP,0).reduce(CP,0).reduce(SP,0).valores[0]
  p_cp = Prob.reduce(DP,0).reduce(RP,0).reduce(JP,0).reduce(SP,0).valores[0]
  p_sp = Prob.reduce(DP,0).reduce(RP,0).reduce(JP,0).reduce(CP,0).valores[0]

  print("La probabilidad de que ninguno haya participado:\n P(dp)= {}\n P(rp)= {}\n P(jp)= {}\n P(cp)= {}\n P(sp)= {}".format(p_dp,p_rp,p_jp,p_cp,p_sp))
  return p_dp, p_rp, p_jp, p_cp, p_sp

def consulta6():

  t = """6. Calcula la probabilidad de que Rita haya participado y un dispositivo tipo B haya sido abandonado."""

  print(t)

  # P(rp,dia|die=B) = alpha \Sigma_{CP,JP,CA,DP,E} P(dia|die,CP)P(die|CP,CA)P(CP|JP)P(CA|DP)P(rp|JP,DP,E)P(JP)P(DP)P(E)

  # P(DP)P(E)
  Prob = fDP.multiply(fE)
  # P(JP) * Prob
  Prob = fJP.multiply(Prob)
  # P(rp|JP,DP,E) * Prob
  Prob = fRP_DPJPE.multiply(Prob)
  # P(CA|DP) * Prob
  Prob = fCA_DP.multiply(Prob)
  # P(CP|JP) * Prob
  Prob = fCP_JP.multiply(Prob)
  # P(die|CP,CA) * Prob
  Prob = fDiE_CACP.multiply(Prob)
  # P(dia|die,CP) * Prob
  Prob = fDiA_CPDiE.multiply(Prob)

  # Marginalizacion \Sigma_{CP,JP,CA,DP,E}
  Prob = Prob.marginalize(E)
  # Marginalizacion \Sigma_{CP,JP,CA,DP}
  Prob = Prob.marginalize(DP)
  # Marginalizacion \Sigma_{CP,JP,CA}
  Prob = Prob.marginalize(CA)
  # Marginalizacion \Sigma_{CP,JP}
  Prob = Prob.marginalize(JP)
  # Marginalizacion \Sigma_{CP}
  Prob = Prob.marginalize(CP)
  # Reducciones
  Prob = Prob.reduce(DiE,"B")
  # Normalizamos el último vector que nos queda
  Prob = Prob.normalize()

  # Extraemos las probabilidades
  p_rp = Prob.reduce(DiA,1).valores[1]
  p_dia = Prob.reduce(RP,1).valores[1]

  # Probabilidad final
  Prob = p_rp * p_dia

  print("La probabilidad de que Rita haya participado y un dispositivo tipo B haya sido abandonado : P(rp,dia|die=B)= {}".format(Prob))

  return Prob

def consulta7():

  t = """7. Calcula la probabilidad de que Daniel haya participado, dado que se encontró el dispositivo B en el museo y el diamante estaba en la caja de seguridad de Sam. Para ello seguirás el método siguiente. Recuerda que, por definición de probabilidad
condicional:

$$P(DP|D=A,U=Caja)=\frac{P(DP,DiE=B,U=Caja)}{P(DiE=B,U=Caja)}$$

"""

  print(t)

  # P(dp|die=B,u=caja) = \alpha P(dp) \Sigma_{E}P(E) \Sigma_{JP}P(JP) \Sigma_{CA}P(CA|dp) \Sigma_{CP}P(CP|JP)P(die|CP,CA) \Sigma_{RP,SP} P(RP|dp,JP,E)P(SP|RP,E) \Sigma_{DiA,DiM}P(u|dp,JP,SP)P(DiM|die,DiA)P(DiA|die,CP)

  # \Sigma_{DiA,DiM}P(u|dp,JP,SP)P(DiM|die,DiA)P(DiA|die,CP)
  Prob = fDiA_CPDiE.reduce(DiE,"B")
  Prob = fDiM_DiEDiA.reduce(DiE,"B").multiply(Prob)
  Prob = fU_SPDPJP.reduce(U,"caja").multiply(Prob)
  Prob = Prob.marginalize(DiA).marginalize(DiM)

  # \Sigma_{RP,SP} P(RP|dp,JP,E)P(SP|RP,E)
  Prob = fSP_ERP.multiply(Prob)
  Prob = fRP_DPJPE.multiply(Prob)
  Prob = Prob.marginalize(RP).marginalize(SP)

  # \Sigma_{CP}P(CP|JP)P(die|CP,CA)
  Prob = fDiE_CACP.reduce(DiE,"B").multiply(Prob)
  Prob = fCP_JP.multiply(Prob)
  Prob = Prob.marginalize(CP)

  # \Sigma_{CA}P(CA|dp)
  Prob = fCA_DP.multiply(Prob)
  Prob = Prob.marginalize(CA)

  # \Sigma_{JP}P(JP)
  Prob = fJP.multiply(Prob)
  Prob = Prob.marginalize(JP)

  # \Sigma_{E}P(E)
  Prob = fE.multiply(Prob)
  Prob = Prob.marginalize(E)

  # P(dp)
  Prob = fDP.multiply(Prob)

  # Multiplicacion por \alpha
  Prob = Prob.normalize()

  # Probabilidad de que Daniel haya participado, dado que se encontró el dispositivo B en el museo y el diamante estaba en la caja de seguridad de Sam.
  Prob = Prob.valores[1]

  print("Probabilidad de que Daniel haya participado, dado que se encontró el dispositivo B en el museo y el diamante estaba en la caja de seguridad de Sam: {}".format(Prob))

  return Prob

if __name__ == "__main__":

  print("Ecuacion1 \n {}",ecuacion1())
  print("----")
  print("Ecuacion2 \n {}",ecuacion2())
  consulta5A()
  consulta5B()
  consulta6()
  consulta7()