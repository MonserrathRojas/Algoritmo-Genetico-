# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Géneticos
Tema: Proyecto 1
Alumnos: 
        Palos Hernandez Jair Antonio
        Rojas Osorio Monserrath 
        Vilchis Medina Luis Julian 
         
Profesor: Dr. Asdrúbal López Chau
Descripción: representacion Real para AG
"""
import numpy as np
import random
import math

class GenReal:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.nbits=16
        #calcula Delta --> |min-max|/nbits^2
        self.delta=np.abs(min-max)/2**self.nbits
    
    def init(self):
        # Inicializa el gen pseudoaletoriamente con 
        # ceros y unos

            self.gen = random.choices([0, 1], k=self.nbits)
    
    def cruzar(self,mama):
        #Aplica cruza de este gen con el gen de la madre
       padre = self.gen.copy()
       madre = mama.gen.copy()
       #crosspoint
       #divide el tamaño del indice devolviendolo como entero
       cp1 = int(np.ceil((self.nbits - 1)/3.))
       cp2 = 2 * cp1
       #realiza la cruza para el primer hijo
       #toma la parte del padre desde 0 a cp1
       son1 = padre[0:cp1]
       #toma la parte de la madre desde cp1 hasta cp2
       son1.extend(madre[cp1:cp2])
       #toma la parte del padre desde cp2 a lo que reste
       son1.extend(padre[cp2:])
       #realiza la cruza para el segundo hijo
       #toma el signo de la madre
       son2 = madre[0:cp1]
       #toma el primer crosspoint con genes del padre
       son2.extend(padre[cp1:cp2])
       #toma el segundo crosspoint con genes de la madre
       son2.extend(madre[cp2:])
       
       s1 = GenReal(self.min, self.max)
       s2 = GenReal(self.min, self.max)
       s1.gen = son1
       s2.gen = son2
       return [s1, s2]
    
    def mutar(self):
        #indice del numero aleatorio a elegir
        idx = np.random.choice(self.nbits)
        #numero aleatorio que se va a cambiar 
        cambiar1=0
        cambiar2=1
        #Realiza el cambio de numero en el indice aleatorio
        #si en el indice aleatorio hay un 1, lo cambia a 0
        if self.gen[idx] == 1:
           self.gen[idx] = cambiar1
        #en caso contrario, es decir hay un 0, lo cambia a 1
        else:
            self.gen[idx] = cambiar2
    
    def __str__(self):
        #Regresa el gen como cadena de ceros y unos
        return str(self.gen)
    
    def getValue(self):
        #Regresa el valor real que representa el gen
        #min+delta*particion
        particion = int(''.join([str(i) for i in self.gen]), 2)
        
        return round(self.min + self.delta*particion)
    