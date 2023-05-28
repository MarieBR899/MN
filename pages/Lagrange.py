import streamlit as st
import pandas as pd
import numpy as np
tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
 st.title('ProyectoMN')
 st.title(":blue[Interpolación de Lagrange]")
  
 """
 Interpolación polinomial
 
 
Se tiene un conjunto de n más uno puntos para representar ayer como una función de valuación única de x, es posible encontrar un polinomio único de grado n qué pasa por dos puntos, hp y es posible encontrar un polinomio cuadrático único que pasa por 3 puntos
la ecuación polinomial para y  se puede modelar mediante:
"""
  

"""
y constituyen un sistema de ecuaciones algebraicas lineales. La solución de este sistema se puede terminar aplicando métodos numéricos para ese fin. Sin embargo, la matriz de coeficientes, denominada matriz de vander homonde, es sensible al mal planeamiento. Además, sobre el sistema de esa manera ineficaz de obtener una representación para y
por lo anterior, se opta por otros métodos por lineales que representan formas más eficaces de predecir y para un valor dado de $x$. La apariencia de estos modelos puede ser muy distinta a la del modelo antes mencionado; sin embargo, producen la misma curva única que pasa por los n puntos.

Fórmula de lagrange
*Es una técnica que permite encontrar el máximo o mínimo de una función de varias 
dimensiones cuando hay alguna restricción en los valores de entrada que puede usar.


Los polinomios de lagrange se pueden determinar especificando algunos de los puntos en el plano por los cuales debe pasar.
Consideras el problema de determinar el polinomio de grado uno que pasa por los puntos distintos…. Este problema es el mismo que el de aproximar una función f para la cual…., por medio de un polinomio de primer grado, interpolando entre,  o coincidiendo con, los valores de FDX en los puntos dados.

Considérese el polinomio:

el polinomio lineal que pasa por x cero se construye usando los cocientes



cuando x igual AX cero
cuando x igual AX uno 

Para generar esa cosa de interpolación lineal considérese la construcción de un polinomio a lo más grado n que pase por los n+1 puntos (x_0,f(x_0)), (x_1,f(x_1)), (x_2,f(x_2)), …, (x_n,f(x_n)), Para lo que se quiere, para cada k=0,1…, n, un cociente L_k(x) con la propiedad de que L_k(x_i) =0 Cuando i distinto de k , por lo que el numerador debe contener el término:


para satisfacer que $ L_k(X_k) =1 $, el denominador debe ser igual al numerador anterior cuando $ x=x_k $, por lo que cocientes tienen la forma:


para cada $k=0,1…, n$; el cual se denomina el cociente de lagrange. A partir del cual se define el polinomio de interpolación de lagrange en el siguiente teorema.
Teorema
sí $x _o, x_1,…,x_n$ son $(n+1)4 son números diferentes y $f(x)$ es una función cuyos valores están dados en estos puntos, entonces existe un único polinomioP(x) de grado a lo más n con la propiedad de que f(x_k)=P(x_k) hd para cada k=0,1…, n.
Este polinomio está dado por

Dónde $L_k(x)$ está dado por la ecuación del teorema anterior
la técnica usada para construir $P(x)$ esto de interpolación hola que se empleaba para construir las tablas trigonométricas con logarítmicas. 

Ejemplo
las densidades de sodio para 3 temperaturas están dadas por

hola para determinar la densidad para t=251°C
dado que se tienen 3 puntos, el polinomio que se puede construir es de a lo más  de grado dos, para obtener el valor de los cocientes, se sustituye el valor de t=251

entonces, la densidad del sodio a una temperatura t=251°C es de d= 890.5566117 Kg/m^{3}

aquí  cabe aclarar que, aunque con el método de lagrange se puede obtener una expresión ese que potencias que aproxime a la función que describe la table datos, esto no es una práctica común, porque generalmente se aplica mediante un programa computadora y porque existen métodos más eficientes para este fin.
"""
