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
Descripción:  Mecanismo de selección
"""
import numpy as np
import random

class Seleccion:
    
    def selecciona(self, aptitudes, k):
        #selecciona a la poblacion para la siguiente generación
        #Darle chance a los feos
        aptitudes = np.array(aptitudes) + .001
        #lista por compresión  para el calculo de las probabilidades de aptitudes
        #usando softmax
        #P(x^i)=e^x^i/Zj=1 e^x^j
        aptitudes= aptitudes/np.max(np.abs(aptitudes))
        probabilidades = [np.exp(aptitud) / np.sum(np.exp(aptitudes)) for aptitud in aptitudes]
        indices = list( range(len(aptitudes)) )
        return random.choices(indices, probabilidades, k=k)
        
        











