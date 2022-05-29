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
Descripción: clase algoritmo evolutivo
"""

import numpy as np
import random
from Poblacion import Poblacion
from FitnessFunction import FitnessFunction
from Seleccion import Seleccion

class AlgoritmoEvolutivo:

    def __init__(self, minis,maxis, size):
        self.minis=minis
        self.maxis=maxis
        self.nbits= 16
        self.size = size#tamaño de poblacion
        self.pob = None #pob=null(vacio)


    def showPob(self, showAptitude=False):
        #Muestra población
        #si es true
        if showAptitude:
            #calcula las aptitudes
            aptitudes = [self.ff.evaluate(ind) for ind in self.pob.poblacion]
            #calcula el resultado
            resultado = [self.ff.resultado(ind) for ind in self.pob.poblacion]
        #ciclo en el tamaño de la población
        for i in range(self.size):
            #si es true
            if showAptitude:
                #imprime los Cromosomas binarios para cada población junto con aptidtud y el resultado
                
                print("\n"+self.pob.poblacion[i].__str__() +
                      " FF-> " + str(aptitudes[i]))
                #imprime variables de los Cromosomas 
                print("Variables --> "+str(self.pob.poblacion[i].getValues()) +" Resultado --> " + str(resultado[i]))
            #si es false    
            else:
                #imprime la población
                print(self.pob.poblacion[i])

    def inicializa(self):
        #crea un objeto de tipo fitnessfunction 
        self.ff = FitnessFunction()
        #calcula cuantos cromosomas no se ocuparán
        tam = 10 - self.ff.size()
        #elimina los valores minimos y máximos que no se ocuparán
        for i in range (tam):
            self.minis.pop()
            self.maxis.pop()
        
        #objeto de tipo poblacion se le manda valores minimos,maximos y tamaño de poblacion
        pob = Poblacion(self.minis,self.maxis, self.size)
        #inicializa población
        pob.inicializa()
        self.pob = pob
        #crea un objeto de tipo seleccion
        self.seleccion = Seleccion()

    def evolucion(self):
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población
        #si la poblacion esta vacia
        if self.pob is None:
            print("Inicialice la población")
            return
        #1) Evaluar individuos
        #se obtiene la poblacion del objeto pob
        poblacion = self.pob.poblacion
        #calcula las aptitudes
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]
        # # 2) Seleccionar padres para cruza
        #divide el tamaño de la poblacion en 2 y lo convierte a entero
        k = int(self.size/2)
        #si el numero es impar
        if k%2 == 1:
            k += 1
        #obtiene el indice que se obtiene con la función
        #Seleccion  se le manda las aptitudes e indice k
        idx = self.seleccion.selecciona(aptitudes,k)
        #3) Generar hijos (cruza)
        descendencia = []
        for i in list(range(0,k-1,2)):
            #selecciona el indice padre
            ip = idx[i]
            #selecciona el indice de la madre
            im = idx[i+1]
            #obtiene el cromosoma del indice padre
            papa = poblacion[ip]
            #obtiene el cromosoma del indice madre
            mama = poblacion[im]
            #crea dos hijos nuevos cruzando el papa con la mama
            hijos = papa.cruzar(mama)
            #agrega a descendencia el primer hijo
            descendencia.append(hijos[0])
            #agrega a descendencia el segundo hijo
            descendencia.append(hijos[1])

        # 4) Mutar a algunos (5%)
        #convierte a entero un numero redondeado del 1 porciento de la longitud de la descendencia
        totalMutar = int(np.ceil(len(descendencia)*0.1))
        #en el tamaño de mutar
        for i in range(totalMutar):
            #obtiene el indice aleatorio de la descendencia
            idx = random.choice(range(len(descendencia)))
            #muta el cromosoma del indice aleatorio
            descendencia[idx].mutar()
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente
        #     población
        # Junto padres e hijos
        for hijo in descendencia:
            poblacion.append(hijo)
        # calculo aptitudes de todos
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]
        # ELITISMO!!!!!
        #obtiene el cromosoma con la mejor aptitud
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        #agrega el indice con la mejor aptitud a la nueva poblacion
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        # Selecciono indices de
        # individuos para la siguiente generacion
        idx = self.seleccion.selecciona(aptitudes,self.size)
        # Creo la lista de individuos de la siguiente
        # generación
        for i in idx:
            siguientePob.append(poblacion[i])
        # Guardo para la siguiente evolución
        self.pob.poblacion = siguientePob

    def elmejor(self):
        poblacion = self.pob.poblacion
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]
        resultado =  [self.ff.resultado(ind) for ind in poblacion]
        idxMejor = np.argmax(aptitudes)
        print("\n---El mejor--- \n ",self.pob.poblacion[idxMejor].__str__() + " FF-> " + str(aptitudes[idxMejor]))
        print("Variables --> "+str(self.pob.poblacion[idxMejor].getValues())+" Resultado--> " + str(resultado[idxMejor]))
    
    
        