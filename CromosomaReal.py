#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: Algoritmos Géneticos
Tema: Cromosoma Real para AG
Alumnos: 
        Palos Hernandez Jair Antonio
        Rojas Osorio Monserrath 
        Vilchis Medina Luis Julian 

Profesor: Dr. Asdrúbal López Chau
Descripción: Cromosoma Real para AG
"""
from GenReal import GenReal as Real
from FitnessFunction import FitnessFunction

class CromosomaReal:
    def __init__(self, minis, maxis):
        '''
        Parameters
        ----------
        minis : list
            DESCRIPTION.valores minimos
        maxis : list
            DESCRIPTION. valores maximos

        Returns
        -------
        None.

        '''
        #si la longitud de los valores minimos y maximos es diferente
        if len(minis) != len(maxis):
            return
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.nbits = 16
        self.genes = []

        #obtiene los valores minimos, maximos para cada gen 
        for min, max in zip(minis, maxis):
            gen = Real(min, max)
            self.genes.append(gen)
            
    def init(self):
        # Inicializa los genes 
        for gen in self.genes:
            gen.init()

    def __str__(self):
        #Regresa los genes como cadena de ceros y unos
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad

    def getValues(self):
        #Guarda los valores reales de cada gen 
        values = []
        for gen in self.genes:
            values.append(gen.getValue())
        return values

    def cruzar(self, madre):
        #Realiza la cruza de todos los genes madre y padre
        genesHijos1 = []
        genesHijos2 = []

        for papa, mama in zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genesHijos1.append(g[0])
            genesHijos2.append(g[1])
        h1 = CromosomaReal(self.minis, self.maxis)
        h2 = CromosomaReal(self.minis, self.maxis)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
    
    def mutar(self):
        #muta los genes
        for gen in self.genes:
            gen.mutar()