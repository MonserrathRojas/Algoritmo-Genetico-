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
Descripción:  Clase fitnessfunction
evalua individuos para ecuación lineal

"""
import numpy as np
import re

class FitnessFunction:
    
    def __init__(self):
        
        self.lamda =1
        self.beta =1
        ecuacion ='5a+2c+3d-4e=500'
        #obtiene solo los numeros de la ecuación
        numeros=[float(num) for num in re.findall(r'-?\d+\.?\d*', ecuacion)]
        self.coeficientes=numeros[0:-1]
        #tamaño de coeficientes
        self.tam=len(self.coeficientes)
        #obtiene el resultado
        self.target = numeros[-1]
        
    def evaluate(self, ind):
        #βe^(-λ|target-resultado|)
        intento = ind
        variables = intento.getValues()
        resultado=0
        
        for i in range(self.tam):
            resultado += variables[i]*self.coeficientes[i]
            x=np.abs(self.target-resultado)
        return  self.beta*np.exp(-self.lamda*x)
    
    def resultado(self,ind):
        #realiza la multiplicación  y suma para las variables con coeficientes
        intento = ind
        variables = intento.getValues()
        resultado=0
        
        for i in range(self.tam):
            resultado += variables[i]*self.coeficientes[i]
        return  resultado 
    
    def size(self):
        #regresa el tamaño que tendrá el cromosoma
        tamC=self.tam
        return tamC