# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: REDES NEURONALES
Tema: Test Cromosoma Real para AG
Alumnos: Monserrath Rojas Osorio
        Luis Julian Vilchis Medina
        Jair Antonio Palos Hernandez
Profesor: Dr. Asdrúbal López Chau
Descripción: Test Cromosoma Real para AG

"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from AlgoritmoEvolutivo import AlgoritmoEvolutivo

#Declaran los valores minimos y máximos 
minis = [-500,-340,-1000,-455,-13,-123,-34,-50,-330,-100 ]
maxis = [100,240,120,222,380,1700,750,800,1020,410]

#crea el objeto tipo Algoritmo evolutivo 
                        #minis, maxis,iteraciones
ae = AlgoritmoEvolutivo(minis,maxis,100)
#iniciliza el objeto algoritmo genetico 
ae.inicializa()
#muestra la poblacion inicial y el mejor
ae.showPob(True)
ae.elmejor()
#realiza las evolución para las nuevas generaciones 
for i in range(100):
    ae.evolucion()
print("---------------------------------")
#muestra la poblacion final y el mejor
ae.showPob(True)
ae.elmejor()
