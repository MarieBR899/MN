import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
 st.title('ProyectoMN')
 st.title(":blue[Interpolación de Lagrange]")
  
 """
 Interpolación polinomial
  
Se tiene un conjunto de $n+1$ puntos $(x_i, y_i)$ para $i=0,1,...,n$ representar a $y$ como una función de valuación única de $x$, es posible encontrar un polinomio único de grado $n$ qué pasa por dos puntos.
Por ejemplo y es posible encontrar una recta única que pasa por dos puntos,y es posible encontrar un polinomio cuadrático único que pasa por tres puntos.
La ecuación polinomial para $y$  se puede modelar mediante:
"""
 
st.latex(r""" 
y= a_0 +a_1x+a_2x^{2}+...+a_nx^{n}
""")

"""
y los $n+1$ puntos se pueden usar para escribir n+1 ecuaciones para los coeficientes $a_i$. Estas ecuaciones son:
"""

st.latex(r""" 
y= a_0 +a_1x_j+a_2x_j^{2}+...+a_nx_j^{n}    con  j =0, 1, 2 ,...,n 
""")


"""
y constituyen un sistema de ecuaciones algebraicas lineales. La solución de este sistema se puede terminar aplicando métodos numéricos para ese fin. 
Sin embargo, la matriz de coeficientes, denominada matriz de vander homonde, es sensible al mal planeamiento. 
Además, sobre el sistema de esa manera ineficaz de obtener una representación para $y$

Por lo anterior, se opta por otros métodos por lineales que representan formas más eficaces de predecir y para un valor dado de $x$.
La apariencia de estos modelos puede ser muy distinta a la del modelo antes mencionado; sin embargo, producen la misma curva única que pasa por los $n$ puntos.

Fórmula de lagrange

*Es una técnica que permite encontrar el máximo o mínimo de una función de varias 
dimensiones cuando hay alguna restricción en los valores de entrada que puede usar.

Los polinomios de lagrange se pueden determinar especificando algunos de los puntos en el plano por los cuales debe pasar.
Considérese el problema de determinar el polinomio de grado uno que pasa por los puntos distintos. 

(x_0,y_0) y (x_1,x_2). Este problema es el mismo que el de aproximar una función $f$,para la cual 
$f(x_0)$ =y_0 y fx_1=y_1 por medio de un polinomio de primer grado, interpolando entre,o conincidiendo con,
los valores de $f(x)$ en los puntos dados.
"""
"""
considerese el polinomio 

"""

st.latex(r""" 
P(x)=\frac{ (x-x_1)}{(x_0-x_1)}
L_1(x)\frac{ (x-x_0)}{(x_1-x_0)} y_1= L_0(x)y_0+L_1(x)y_1
""")
"""
el polinomio lineal que pasa por  $ (x_0,f(_0))$ y$ (x_1,f(_1)) $ se construye usando los cocientes
"""

st.latex(r"""L_0(x)=\frac{ (x-x_1)}{(x_0-x_1)}
L_1(x)\frac{ (x-x_0)}{(x_1-x_0)}\\

P(x)=  L_0(x)y_0+L_1(x)y_1
""")
"""
cuando $x=x_0$
"""
st.latex(r""" 
P(x)=\frac{ (x_0-x_1)}{(x_0-x_1)}y_0 +\frac{ (x_0-x_0)}{(x_1-x_0)}y_1 =y_0=f(x_0)
""")
"""
$L_0(x_0)=1$, mientras que $L_1(x_0)=0$
"""
"""
cuando $x=x1$
"""
st.latex(r""" 
P(x)=\frac{ (x_1-x_1)}{(x_0-x_1)}y_0 +\frac{ (x_1-x_0)}{(x_1-x_0)}y_1 =y_1=f(x_1)\\
L_0(x_1)=0 y L_1(x_1)=1
""")

"""
Así $P(x)$ tiene las propiedades requeridas.

Para generalizar el concepto de interpolación lineal, considérese la construcción de un polinomio a lo más grado $n$ que pase por los $n+1$ puntos $(x_0,f(x_0))$, $(x_1,f(x_1))$,$ (x_2,f(x_2))$, …, $(x_n,f(x_n))$, 
Para lo que se requiere, para cada $k=0,1…, n$, un cociente $L_k(x)$ con la propiedad de que $L_k(x_i) =0$ Cuando $i\neq k$, por lo que el numerador debe contener el término:
"""
st.latex(r"""
(x-x_0)(x-x_1)...(x-x_k-1)(x-x_k+1)...(x-x_n)
""")

""""
para satisfacer que $ L_k(X_k) =1 $, el denominador debe ser igual al numerador anterior cuando $ x=x_k $, por lo que cocientes tienen la forma:
"""

st.latex(r""" 
L_k(x)=\frac{ (x-x_0)(x-x_1)...(x-x_k-1)(x-x_k+1)...(x-x_n)}{(x_k-x_0)(x_k-x_1)...(x_k-x_k-1)(x_k-x_k+1)...(x_k-x_n)}=
\prod_{i=0}{i \neq k}^{n}x_{i}= \frac{(x-x_i)}{(x_k-x_i)}

""")
"""

para cada $k=0,1…, n$; el cual se denomina el cociente de lagrange. A partir del cual se define el polinomio de interpolación de lagrange en el siguiente teorema.

**Teorema**
sí $x _o, x_1,…,x_n$ son $(n+1)$ son números diferentes y $f(x)$ es una función cuyos valores están dados en estos puntos, entonces existe un único polinomioP(x) de grado a lo más n con la propiedad de que f(x_k)=P(x_k) hd para cada k=0,1…, n.
Este polinomio está dado por
"""
st.latex(r""" 
P_n(x)f(x_0)L_0(x) + f(x_1)L_1(x)+...+f(x_n)L_n(x)=\displaystyle\sum_{k=0}^{n}x_{i}=f(x_k)L_k(x)  
""")


"""
Dónde $L_k(x)$ está dado por la ecuación del teorema anterior
La técnica usada para construir $P(x)$ esto de interpolación hola que se empleaba para construir las tablas trigonométricas con logarítmicas. 
"""

 with tab2:

 """
 Ejemplo
 las densidades de sodio para 3 temperaturas están dadas por (Nakamura, 1992)

 Para determinar la densidad para t=251°C
 Dado que se tienen 3 puntos, el polinomio que se puede construir es de a lo más  de grado dos, para obtener el valor de los cocientes, se sustituye el valor de t=251
 """

 st.latex(r""" 
 L_0(t)= \frac{ (t-250)(t-371)}{(94-205)(94-371)}= -0.17953  
 """)
 st.latex(r""" 
 L_0(t)= \frac{ (t-94)(t-371)}{(205-94)(205-371)}= 1.022468 
 """)
 st.latex(r""" 
 L_0(t)= \frac{ (t-94)(t-205)}{(371-94)(371-205)}= 0.157061 
 """)

st.latex(r""" 
P_2(t=251)= -0.17953(929) + 1.022468(902) + 0.157061(860) = 890.336612 
""")

"""
Entonces, la densidad del sodio a una temperatura t=251°C es de d= 890.5566117 Kg/$m^{3}$

aquí  cabe aclarar que, aunque con el método de lagrange se puede obtener una expresión ese que potencias que aproxime a la función que
describe la table datos, esto no es una práctica común, porque generalmente se aplica mediante un programa computadora y porque existen 
métodos más eficientes para este fin.
"""
