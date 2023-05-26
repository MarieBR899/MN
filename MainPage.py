import streamlit as st
import pandas as pd
import numpy as np


st.title('ProyectoMN')

'''
Metodo de Broyden  
'''
'''
El metodo cuasi Newton o método de Broyden 
Como se menciono anteriormente el metodo de Newton tiene como principal desventaja  el cálculo y evaluación de las derivadas parciales ,asi como lainversion
de la matriz jacobiana. Cuando no es práctico, o posible obtener las derivadas  parciales pueden usarse las aproximaciones  por diferencias finitas
a dichas derivadas, lo que representa  la generalizacion del método  de la secante para la solución de sistemas  de ecuaciones no lineales  y se conoce 
así como el método  de cuasi Newton o Broyden.


Este método requiere $n$ evaluaciones  funcionales por iteración  ya que remplaza la matriz jacobiana  con una matriz de aproximación 
que se actualiza en cada iteración y también disminuye el número de  calculos aritméticos a $O(n^2)$. Pertenece a una clase de tecnicas que 
reemplazan a la matriz jacobiana con una matriz de aproximación  que se actualiza con cada iteración. 
Su desventaja radica en que se pierde  la convergencia cuadrática de Newton, al ser sustituida por una convergencia denominada superlineal, 
la cual implica que:  

 $\lim_{x\to\infty}$  $(d\frac{||X^{(x+1)}-X||}$ ${||X^{(i)}-X||}=0$
'''

'''
El método de Broyden condiste en que a partir de 2 aproximaciones iniciales:


$X^{(0)}$ y $ X^{(1)}$ y la solucion de $X$ de $F(x)=0

se calcula de $X^{(2)}$ en afelante von el método de Broyden. La primera iteracion se calcula por método de Newton, o si es difícil determinar se calcula por $J(x^{(0)})$ se utilizan las ecuaciones de diferencias para aproximar las derivadas parciales.
Antes de iniciar con el metodo de Broyden es importante recordar que el metodo de la secante multivariable implica la siguiente fórmula para sustituir el cálculo de la derivadas.
'''

st.latex(r"""
f'(x_1)= \frac {f(x_1)- f(x_0)}{x_1-x_0}
""")


"""
Dado que en los sistemas de ecuaciones no lineales $X^{(1)}$-$X^{(0)}$ es un vector, el cociente correspondiente esta indefinido.
Sin embargo , el método procedes de manera semejante al método de Newton, por que la matriz  $J(X^{(1)})$ es reemplazada  por una matriz $A$ que tiene  la propiedad 
de que :

$A^{(1)}(X^{(1)}-X^{(0)}$= $F(X^{(1)}-F(X^{(0)})$

Esta matriz es la que se usa para  determinar $X^{(2)}$ como:

   $X^{(2)} = X^{(1)}-(A^{(1)})^{-1} F(X^{(1)})$
   
   
   Y cuyos componentes se ontienen con las dos iteraciones previas  $X^{(k)}$ y $X^{(k-1)}$ de la siguiente manera:
"""


st.latex(r"""
    A^{(k)}= A^{(k-1)} + \frac{[F(X^{(k)})-A^{(k-1)}-A^{(k-1)}(X^{(k)}-X^{(k-1)}](X^{(k)}-X^{(k-1)})^{t}}{||(X^{(k)}-X^{(k-1)})||_2^{2}}
""") 

"""
O bien 
"""

st.latex(r"""
    A^{(k)}= A^{(k-1)} + [\frac{[\DeltaF^{(k)}-A^{(k-1)}-\DeltaX^{(k)}](\DeltaX^{(k)})^{t})}{||\DeltaX^{(k)}||_2^{2}}
    """)
                        
