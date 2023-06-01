import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
  st.title('ProyectoMN')
  st.title(":blue[**Método de Diferencias Divididas**]")

"""
  Fórmula de diferencias divididas
  Los métodos para determinar la representación explícita de un polinomio de interpolación , a partir de datos tabulados, se conocen como diferencias y pueden usarse con de deducir técnicas para aproximar las derivadas y las integrales de las funciones, 
  así como para aproximar las soluciones de ecuaciones diferenciales. 
  El tratamiento de las tablas de diferencias divididas supone que la función $f(x)$ es conocida para varios valores de x. Dichos valores no necesariamente están igualmente espaciados u obedecen algún orden (sin embargo, si están ordenados puede ser ventajoso)

  Supóngase que $P_n(x)$ ese polinomio de lagrange de grado a lo más n que coincide con la función $f(x)$ en los números distintos $x _0, x_1,…,x_n. Las diferencias divididas f(x) con respecto  a x _0, x_1,…,x_n$ 
  se pueden deducir demostrando que $P_n(x)$ tiene representación
"""
st.latex(r"""
P_n(x)= a_0 +a_1(x-x_o)+a_2(x-x_0)(x-x_1)+ ...+a_n(x-x_0)(x-x_1)...(x-x_n-1)
""")

"""
  Con constantes apropiadas $a _0, a_1,…,a_n$
  Si $P_n(k)$ cumple con la condición de pasar por los puntos empleados en su construcción, entonces evaluando en la ecuación 
  anterior $x=x_0$ queda: 
"""
st.latex(r"""
 P_n(x_0)= a_0 =f(x_0) 
 """)
  
""" 
   Similarmente , cuand se evalúa en x_1, los unicos términos distintos de cero en la evaluación  de $P_n(x_1)$ son la constante y el término lineal, 
   el cual se despeja $a_1$:
   
"""
st.latex(r"""
  P_n(x_1)=f(x_0)+a_1(x_1-x_0)=f(x_1)
 """)
  
st.latex(r"""
  a_1= \frac {f(x_1)-f(x_0)}{x_1-x_0}
 """)
"""
  Es aqui en donde se  introduce la notación de la diferencia dividida, la primera diferencia dividida de $f(x)$ con respecto a $x_i$ y $x_i+1$, se denota  por $f[x_i,X_i+1]$ 
  y está definida  como:
"""
st.latex(r"""
  f[x_i,X_i+1]=\ frac {f[X_i+1]-f[x_i]}{X_i+1 -x_i}
 """)
"""
  La diferencia dividida de cero de la función $f(x)$, con respecto a $x_i$, se denota por $f[x_i]$, y es simplemente  la evaluación de $f(x)$ en $x_i$
"""
st.latex(r"""
  f[x_i]= f(x_i) 
 """)
  
"""
  Las diferencias divididas se definen  inductivamente , las pimeras de las cuales se muestran  en la siguiente tabla
"""
  
st.latex(r"""  
| x_i         | f_i=f[x_i] | f[x_i,x_i+1]  |f[x_i,x_i+1,x_i+2]| f[x_i,x_i+1,x_i+2, x_i+3]|
| --------------| ------------- |-----------------|--------------------| ---------------------------|
|   x_0| f(0)|  f[X_0,x_1]$=$\frac{f_1-f_0}{x_1-x_0}| f[X_0,x_1,X_2]=\frac{f_1-f_0}{x_1-x_0}$ | f[X_0,x_1,X_2, X_3]\ frac {[X_0,x_1,X_2, X_3]-f[X_0,x_1,X_2}{x_3 -x_0}
| Content Cell  | Content Cell  |
