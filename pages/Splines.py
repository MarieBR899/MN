import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.title(":blue[**Splines cubicos**]")
    
    """
    Spline cúbico
otra manera de ajustar un polinomio a un conjunto de datos es un spline(trazador) cúbico, la diferencia radica en que este lo hace a través d
e una curva suave, la cual puede ser de varios grados

En general un conjunto de polinomios de n-esimo grado se ajusta entre cada par de puntos adyacentes, g(x), desde x_i hasta x_i+1. 
Estos polinomios se conocen como curvas spline(trazadores). Si el grado del explain es uno, sólo hay rectas entre los puntos, lo cual 
generaría un ajuste como el que se muestra en la siguiente figura. 


Que los splines pueden ser de cualquier grado, los cúbicos son los más conocidos ya que un polinomio cúbico es el el polinomio de menor 
grado que generalmente satisface las condiciones para el ajuste de curvas que consiste en crear una sucesión  
splines cúbicos sobre intervalos sucesivos de los datos. Estos polinomios tendrán la misma pendiente y curvatura en los puntos(nodos) 
en que se unen, por lo que los intervalos no necesariamente tienen que ser uniformes. 


Entonces la aproximación mediante splits cúbicos se aplica a n pares ordenados de datos. Se buscan n-1 curvas que conectan los puntos 0 y 1 , 1y 2 , …, (n-1) y n. Además, se requiere de las curvas que conectan los puntos(k-1) y k y los puntod k y (k+1) Tengan la misma pendiente en el punto k. De esta manera, el ajuste de la cultura es suave
Figura 10 

cómo puede observarse, en los puntos extremos del conjunto de datos sobre los que f(x) se ajusta con los splits cúbicos, 
no hay polinomio de unión. Esto significa que la la pendiente y la curvatura no están restringidas en estos nodos;
estos valores deberán ser asignados a partir de algunas alternativas que se presentan más adelante
"""
