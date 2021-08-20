# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:04:37 2020

@author: JOSUE
"""

import math as m
import os
import io
import numpy as np
import random

class proceso():
   
    dx=0.001 #incremento de integracion
    xi=0 # tiempo iniciaal
    xf1=25#tiempo final en minutos
    xf=xf1+dx
    V=1500 # volumen inicial del tanque en litros
    XPRINT=1 # intervalo de impresion de datos
    
    
    def evaluar(self,F1,F2,CA1,CA): # funcion para evaluar la ecuacion
        X=np.arange(start=self.xi, stop=self.xf, step=self.dx)
        n = len(X)
        
        Y = self.V # INICIALIZA EL VECTOR Y
        Y=np.zeros(n)
        Z=CA
        Z=np.zeros(n)
        VCA=self.V*CA
        
        for i in range(0,n):
            
            dV = (F1-F2)
            dVCA=F1*CA1-F2*CA
            
            # SECCION DE INTEGRACION
            self.V = self.V + dV*self.dx
            VCA = VCA + dVCA*self.dx
            CA=VCA/self.V
            
            Y[i] = self.V
            Z[i]=CA
            
        YZ=[Y,Z]
        return YZ
    
    def imprimir(self,Y): # retorna un vector con los intervalos 
        X=np.arange(start=self.xi, stop=self.xf, step=self.dx)
        n = len(X)
        i=self.XPRINT/self.dx
        
        j=np.arange(start=0, stop=n, step=i)
        return j
    
    
    def aleatorio(self):# genera parametros aleatorios en caso que no corrsponda con los parametros
        archivo= open('parametros_mezclador.txt', 'r')
        #archivo.seek(19)
        lineas=archivo.readlines()
        lista=[]
        for i in range(15):
            if i!=10 and i!=5 and i!=0:      
                x=lineas[i]
                y=float(x[3:])
                lista.append(y)
        
        caudal=[lista[0],lista[1],lista[4],lista[5],lista[8],lista[9]]
        concentracion=[lista[2],lista[3],lista[6],lista[7],lista[10],lista[11]]
            
        
        
              
        print("F1: Caudal de entrada en L/min")
        print("F2: Caudal de salida en L/min")
        print("CA1: Concentracion de entrada en mol/L")
        print("CA: concentracion inicial en mol/L")
        print(" ")
        print("Del archivo texto ")
                
        print("Parametros de entrada 1")
        print(" F1:  ",caudal[0],"\n","F2:  ",caudal[1],"\n","CA1: ",concentracion[0],"\n","CA:  ",concentracion[1])
        print("Parametros de entrada 2")
        print(" F1:  ",caudal[2],"\n","F2:  ",caudal[3],"\n","CA1: ",concentracion[2],"\n","CA:  ",concentracion[3])  
        print("Parametros de entrada 3")
        print(" F1:  ",caudal[4],"\n","F2:  ",caudal[5],"\n","CA1: ",concentracion[4],"\n","CA:  ",concentracion[5]) 
         
        
        ban1=0
        ban2=0
        for i in range(len(caudal)):
            a=float(caudal[i])
            b=float(concentracion[i])
                    
            if a<0 or a>10000 :
                ban1=1
                del caudal[i] 
                x=random.randint(0,10)*100
                caudal.insert(i,x)
            if b<0 or b>100:
                ban2=1
                del concentracion[i]
                x=random.randint(0, 10)*10
                concentracion.insert(i, x)
        
        datos_basicos={
                    "f1":caudal[0],"f2":caudal[1],"c1":concentracion[0],"c2":concentracion[1],
                    "f12":caudal[2],"f22":caudal[3],"c12":concentracion[2],"c22":concentracion[3],
                    "f13":caudal[4],"f23":caudal[5],"c13":concentracion[4],"c23":concentracion[5]
                            }
        if ban1==1 or ban2==1:
            print(" ")
            print("Parametros con datos aleatorios ")
                    
            print("Parametros de entrada 1")
            print(" F1:  ",datos_basicos["f1"],"\n","F2:  ",datos_basicos["f2"],"\n","CA1: ",datos_basicos["c1"],"\n","CA:  ",datos_basicos["c22"])
            print("Parametros de entrada 2")
            print(" F1:  ",datos_basicos["f12"],"\n","F2:  ",datos_basicos["f22"],"\n","CA1: ",datos_basicos["c12"],"\n","CA:  ",datos_basicos["c22"])  
            print("Parametros de entrada 3")
            print(" F1:  ",datos_basicos["f13"],"\n","F2:  ",datos_basicos["f23"],"\n","CA1: ",datos_basicos["c13"],"\n","CA:  ",datos_basicos["c23"])
        
        fc=[caudal,concentracion]
        return fc
    def guardar(self,x,n,Y1,Z1,Y2,Z2,Y3,Z3):#guarda e imprime las salidas del sistema
        archivo2=open('resultados.text','w')

        for j in range(x): 
            
            for i in range(len(n)):#n
                z=n[i]
                if j==0:
                    if i==0:
                        print(" ")
                        print("Salidas con parametros de entrada 1")
                        print("tiempos(min)       volumen (L)          concentracion(mol/L)")   
                    if Y1[int(z)]<0:
                        Y1[int(z)]=0
                        Z1[int(z)]=0
                    resulY1=Y1[int(z)]
                    resulZ1=Z1[int(z)]
                    
                        
                    a1=str(round(resulY1,2))
                    a2=str(round(resulZ1,2))
                    b1=str(n[i]/1000)
                    ca=str(b1 +"         \t      " + a1 +"          \t  "+a2)
                    
                    if i==0:
                        archivo2.writelines( "salidas con parametros de entrada 1\n")
                        archivo2.writelines( "tiempos(min)       volumen (L)          concentracion(mol/L)\n")
                    archivo2.writelines(ca + "\n" )
                    print(n[i]/1000,"          \t   ",round(Y1[int(z)],2),"            \t ",round(Z1[int(z)],2))
                    
                if j==1:
                    if i==0:
                        print(" ")
                        print("Salidas con parametros de entrada 2")
                        print("tiempos(min)       volumen (L)          concentracion(mol/L)") 
                    if Y2[int(z)]<0:
                        Y2[int(z)]=0
                        Z2[int(z)]=0
                    resulY2=Y2[int(z)]
                    resulZ2=Z2[int(z)]
                    a1=str(round(resulY2,2))
                    a2=str(round(resulZ2,2))
                    b1=str(n[i]/1000)
                    ca=str(b1 +"         \t      " + a1 +"          \t  "+a2)
  
                    if i==0:
                        archivo2.writelines( "               \n" )
                        archivo2.writelines( "salidas con parametros de entrada 2\n" )
                        archivo2.writelines( "tiempos(min)       volumen (L)          concentracion(mol/L)\n")
                    archivo2.writelines(ca + "\n" )
                    print(n[i]/1000,"          \t   ",round(Y2[int(z)],2),"            \t ",round(Z2[int(z)],2))
                    
                if j==2:
                    if i==0:
                        print(" ")
                        print("Salidas con parametros de entrada 3")
                        print("tiempos(min)       volumen (L)          concentracion(mol/L)") 
                    if Y3[int(z)]<0:
                        Y3[int(z)]=0
                        Z3[int(z)]=0
                    resulY3=Y3[int(z)]
                    resulZ3=Z3[int(z)]
                    a1=str(round(resulY3,2))
                    a2=str(round(resulZ3,2))
                    b1=str(n[i]/1000)
                    ca=str(b1 +"         \t      " + a1 +"          \t  "+a2)
                    if i==0:
                        archivo2.writelines( "               \n" )
                        archivo2.writelines( "salidas con parametros de entrada 3\n" )
                        archivo2.writelines( "tiempos(min)       volumen (L)          concentracion(mol/L)\n" )
                    archivo2.writelines(ca + "\n" )
                    print(n[i]/1000,"          \t   ",round(Y3[int(z)],2),"            \t ",round(Z3[int(z)],2))
                    
               
                    
                
                    
        archivo2.close()
   
#creacion de objetos
ecuacion1=proceso()
ecuacion2=proceso()
ecuacion3=proceso()

guardar_mostrar=proceso()


a=ecuacion1.aleatorio()

f=a[0]
c=a[1]





YZ1=ecuacion1.evaluar(float(f[0]),float(f[1]),float(c[0]),float(c[1]))
YZ2=ecuacion2.evaluar(float(f[2]),float(f[3]),float(c[2]),float(c[3])) 
YZ3=ecuacion3.evaluar(float(f[4]),float(f[5]),float(c[4]),float(c[5]))



Y1=YZ1[0]
Z1=YZ1[1]
Y2=YZ2[0]
Z2=YZ2[1]
Y3=YZ3[0]
Z3=YZ3[1]


n=ecuacion1.imprimir(Y1)

milista1=[]
milista2=[]
milista3=[]
milista4=[]
milista5=[]
#print("numero de pasos      resultado ")


 #x,n,y1,2,y3,y4,y5
        
guardar_mostrar.guardar(5, n, Y1,Z1,Y2,Z2,Y3,Z3)


