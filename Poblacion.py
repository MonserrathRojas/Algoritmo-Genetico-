#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Genéticos
Tema:Proyecto Ecuación Lineal
Alumnos: 
        Palos Hernandez Jair Antonio
        Rojas Osorio Monserrath 
        Vilchis Medina Luis Julian 

Profesor: Dr. Asdrúbal López Chau

Descripción:  Población de individuos
"""

from CromosomaReal import CromosomaReal
 
class Poblacion:
    #constructor Población 
    def __init__(self,minis,maxis, size):
        self.minis=minis
        self.maxis=maxis
        self.nbits=16
        self.size = size


    def inicializa(self):
        #INICIALIZACIÓN DE LA POBLACIÓN
        poblacion = []
        #De acuerdo al tamaño de la población, le agrega Cromosoma Real y los inicializa
        for i in range(self.size):
            ind = CromosomaReal(self.minis,self.maxis)
            ind.init()
            #agrega a la población individuos
            poblacion.append(ind)
        self.poblacion = poblacion
        
   
        
        
        
        
        
        
        
        
        
        
        
        