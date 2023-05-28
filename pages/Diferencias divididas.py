import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
  st.title('ProyectoMN')
    st.title(":blue[**Método de Diferencias Divididas**]")

"""
Fórmula de diferencias divididas
 los métodos para determinar la representación explícita de un polinomio de interpolación , a partir de datos tabulados, se conocen como diferencias y pueden usarse con de deducir técnicas para aproximar las derivadas y las integrales de las funciones, así como para aproximar las soluciones de ecuaciones diferenciales.
El tratamiento de las tablas de diferencias divididas supone que la función f(x) es conocida para varios valores de x. Dichos valores no necesariamente están igualmente espaciados u obedecen algún orden (sin embargo, si están ordenados puede ser ventajoso)

supóngase que P_n(x) ese polinomio de lagrange de grado a lo más n que coincide con la función f(x) en los números distintos x _o, x_1,…,x_n. Las diferencias divididas f(x) con respecto  a x _o, x_1,…,x_n se pueden deducir demostrando que P_n(x) tiene representación


con constantes apropiadas a _o, a_1,…,a_n
si P_n(k) cumple con la condición de pasar por los puntos empleados en su construcción entonces evaluando en la ecuación ho anterior

en x =x_0 queda: 
"""
