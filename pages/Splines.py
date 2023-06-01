import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.title(":blue[**Splines cubicos**]")
    
    """
    **Spline cúbico**
Otra manera de ajustar un polinomio a un conjunto de datos es un $spline$ (trazador) cúbico, la diferencia radica en que este lo hace a través d
e una curva suave, la cual puede ser de varios grados.

En general un conjunto de polinomios de $n-ésimo$ grado se ajusta entre cada par de puntos adyacentes, $g(x)$, desde $x_i$ hasta $x_i+1$. 
Estos polinomios se conocen como curvas $spline$(trazadores). Si el grado del explain es uno, sólo hay rectas entre los puntos, lo cual 
generaría un ajuste.FIG 1 

Aunque los splines pueden ser de cualquier grado, los cúbicos son los más conocidos ya que un polinomio cúbico es el el polinomio de menor 
grado que generalmente satisface las condiciones para el ajuste de curvas que consiste en crear una sucesión  
splines cúbicos sobre intervalos sucesivos de los datos. Estos polinomios tendrán la misma pendiente y curvatura en los puntos(nodos) 
en que se unen, por lo que los intervalos no necesariamente tienen que ser uniformes. 


Entonces la aproximación mediante splits cúbicos se aplica a $n$ pares ordenados de datos. Se buscan $n-1$ curvas que conectan los 
puntos $0 y 1 , 1y 2 , …,(n-1)$ y $n$. Además, se requiere de las curvas que conectan los puntos$(k-1)$ y k y los puntod $k y (k+1)$
Tengan la misma pendiente en el punto $k$. De esta manera, el ajuste de la cultura es suave
Figura 2 

Cómo puede observarse, en los puntos extremos del conjunto de datos sobre los que $f(x)$ se ajusta con los splits cúbicos, 
no hay polinomio de unión. Esto significa que la la pendiente y la curvatura no están restringidas en estos nodos;
estos valores deberán ser asignados a partir de algunas alternativas que se presentan más adelante.
Para  determina la forma en que se obtienen estos trazadores cúbicos se describe la ecuación para un polinomio cúbico  entre los puntos 
$(x_i, y_i)$ y $(x_i+1, y_i+1)$, $g_i(x_i)$ en el $i-ésimo$ intervalo, 
"""
st.latex(r"""
 g_i(x_i)=a_i(x-x_i)^{3}+b_i(x-x_i)^{2} + c_i(x-x_i)+ d_i
 """)
"""
 La funcion se $spline$ cúbico que se desea es de la forma: 
 $g_i(x_i)=g_i(x_i)$ sobre el intervalo [x_i,x_i+1] para $i=0,1,...,n-1$
 y cumple con las condiciones:
 * $g_i(x_i)=y_i  i=0,1,...,n-1$   Implica que se ajusta a cada uno de los puntos
 * $g_n-1(x_n)=y_n$                El último polinomio  ajusta al último punto
 * $g_i(x_i+1)= g_i+1(x_i+1)$      Los polinomios coinciden en los nodos 
 * $g'_i(x_i+1)= g'_i+1(x_i+1)$    Continuidad  en pendiente (coinciden en los nodos)
 * $g''_i(x_i+1)= g''_i+1(x_i+1) $ Continuidad  en la curvatura, $i=0,1,...,n-1$
 
 Si hay $n+1$ puntos, el número de intervalos y el número de polinomios $g_i(x)$ es $n$, entonces hay  cuatro veces $n$ incognpitas que son las 
 ${a_i,b_i,c_i,d_i}$ para $i=0,1,...,n-1$.
 De la primera condicion se piede ver que $d_i=y_i$, para $i=0,1,...,n-1$
 En el polinomio cúbico $g_i(x)= a_i(x-x_i)^{3}+b_i(x-x_i)^{2} + c_i(x-x_i)+ y_i+y_i$ se puede emplear  $h_i=x_i+1-X_i$ como la amplitud del
 último intervalo y reescribirse como:
 """
st.latex(r"""
 g'_i a_i h_i^{3}+b_ihi^{2} + c_i h_i + y_i
 """)
"""
 para  $i=0,1,...,n-1$
"""
"""
 El cual  se deriva para relacionar las pendienres y las curvaturas de los splines de la unión:
 """
st.latex(r"""
 g'_i(x_i)=3a_i h_i^{2}+2b_ihi + c_i
 """)
st.latex(r"""
 g''_i(x_i)=6a_i h_i+2b_i hi
 """)
"""
Aprovechando que $g''_i(x_i)$ es lineal  en el intervalo [x_i,x_i+1] se hace:
$S_i=g''_i(x_i)$ para  $i=0,1,...,n-1$
$S_n = g''n-1(x_n)$
entonces 
"""
st.latex(r"""
 S_i=g''_i(x_i)=6a_i(x_i-x_i)+2b_i=g''_i(x_i) =2b_i
 """)
st.latex(r"""
 S_i+1=g''_i(x_i+1)=6a_i(x_i+1-x_i)+2b_i= 6a_ih_i+2b_i
 """)
"""
Despejando los coeficientes $a_i,b_i$:
 $b_i= \dfrac{S_i}{2}$    $a_i= \dfrac{S_i+1-S_i}{6h_i}$
 
 Sustituyendo los valores  de $a_i,b_i y d_i$ en $g_i(x)=y_i+1$ para despejar c_i;
"""
st.latex(r"""
 y_i+1= (\dfrac{S_i+1-S_i}{6h_i}) h_i^{3} +  \dfrac{S_i}{2}h_i^{2} +c_ih_i + y_i
 """)
st.latex(r"""
 c_i= \frac {y_i+1-y_i}{h_i}-(\dfrac{S_i+1+2S_i}{6})h_i= f[x_i,x_i+1] -(\dfrac{S_i+1+2S_i}{6})h_i  
 """)
"""
De esta manera los coeficientes $a_i,b_i, c_iy d_i$ quedan determinados en términos de S_i. Acontinuación se determinan los valores de las
$S_i$ para $i=0,1,...,n-1$
Dado que las pendiente de las dos cúbicas que se unen en $(x_i,y_i)$ son iguales.
"""
st.latex(r"""
 y'_i= 3a_i(x_i-x_i)^{2} +2b_i(x_i-x_i)+c_i  
 """)
"""
Para la ecuación en el $i-ésimo$ intervalo, con $x=x_i$, la ecuación anterior es:
"""
st.latex(r"""
 y'_i= 3a_i(x_i-x_i)^{2} +2b_i(x_i-x_i)+c_i=c_i  
 """)
"""
En el intervalo previo, de $x_i-1 a x_i$ la pendiente en su extremo derecho es:
"""
st.latex(r"""
 y'_i= 3a_i-1(x_i-x_i-1)^{2} +2b_i-1(x_i-x_i)+c_i-1   
 """)
st.latex(r"""
 y'_i= 3a_i-1h_i^{2} +2b_i-1h_i-1 +c_i-1
 """)
"""
Al igualar las ecuaciones  y sustituir  para $a_i,b_i y c_i$,para obtener sus relaciones en terminos de S_i y h:
"""
st.latex(r"""
3(\dfrac{S_i-1S_i-1}{6h_i-1})h_i-1^{2} + 2 \dfrac{S_i-1}{2}h_i-1 + f[x_i-1,x_i]-(\dfrac{S_i+2S_i-1}{6})h_i-1=
f[x_i,x_i+1]-(\dfrac{S_i+1 +2S_i}{6})h_i
 """)
"""
Al simplificar
"""
st.latex(r"""
h_i-1S_i-1+2(h_i-1+h_i)S_i +h_iS_i+1 =6( f[x_i,x_i+1]-f[x_i-1,x_i])
""")
"""
Esta última ecuación es válida en cada punto interno $i=0,1,...,n-1$, lo cual genera un sistema de $n-1$ ecuaciones que relacionan los
$n+1$ valores $S_i$.

Una vez defininidos los valores para los extremos, se escribe la ecuación  anterior  en forma matricial con $S_1, S_2, ...S_n-1$
 como las incógnitas:
 """
st.latex(r"""
\begin{equation}
 \begin{pmatrix}
  h_0    & 2(h_0+h_1) & h_1        & 0         & \cdots   & 0             & 0 \\
  0      & h_1        & 2(h_1+h_2) & h_2       &\cdots    &               &\cdots\\
  0      & 0          & h_2        &2(h_2+h_3) & \cdots   &\cdots         &\cdots  \\
  \vdots &\vdots      &\cdots       & \ddots    & \cdots  &\cdots         & \cdots \\
  0      & 0          & 0           & \cdots     &h_n     & %2(h_n-2+h_n-1) &h_n-1
   \end{pmatrix}
   
   \begin{pmatrix}
   S_0\\
   S_1 \\
   \vdots\\
   \vdots
   S_n
    \end{pmatrix}
  =
  \begin{pmatrix}
   f[x_1,x_2] - f[x_0,x_1] \\
   f[x_2,x_3] - f[x_1,x_2] \\
   \vdots\\
   \vdots
   f[x_n-1,x_n] - f[x_n-2,x_n-1]
    \end{pmatrix}
        \end{equation} 
 """)
"""
Como puede observarse hay $n+1$ incógnitas y $n-1$ ecuaciones. Para hacer este sistema cuadrado se detemrinan 
$S_0 y S_n$ usando algunas de las supociones antes mencionadas en la frontera, la más comú  de ellas es el spline natural.
Una ves que se obtienen los valores $S_i$ se obtienen los coeficientes  $a_i,b_i, c_i y d_i$ para cada uno de los polinomios cúbicos 
en cada intervalo. A partir de éstos es posible  calcular puntos en la curvatura de interpolación. 
"""

with tab2:
    """
   **Ejemplo** Emplear los datos de la siguiente tabla: para hacer un ajuste por spline cúbico y determinar  una estimación 
   para $f(0.66) y f(1.75)$
   
   |   $x$     |   $f(x)$ |
   ------------------------
   |$0.0$      | $2$   |
   |$1.0$      |$4.4366$|
   |$1.5$      |$6.7134$|
   |$2.25$     |$13.9130$|
   
 Para construir el sistema cuyo resultado son los S_i primero se determinan los elementos necesarios para su construcción, los $h_i$ y 
 las primeras diferencias divididas
 
  |   $x_i$     |   $f(x_i)$ |      $h_i$ | $f[x_i,x_i+1]$ |
   -----------------------------------------------------------
   |$0 $       |$2$         |       $1 $ |  $2.4366$   |
   |$1$        |$4.4366$    |    $0.5 $  |  $4.5536 $  |
   |$1.5$      |$6.7134$    |    $0.75 $ |  $9.599467 $|
   |$2.25$     |$13.9130$   |            |             |
   
   empleando el spline natural, $S_0 y S_n=0$, el sistema queda:
   """
  st.latex(r"""
    \begin{equation}
    \begin{pmatrix}
   2(1.5)  & 0.5  \\
    0.5     & 2(1.25) \\
     \end{pmatrix}
    \begin{pmatrix}
      S_1\\
      S_2
    \end{pmatrix}
    =
    \begin{pmatrix}
      12.702\\
      30.2752
    \end{pmatrix}
        \end{equation} 
 """)
   """ el cual  al resolverse  da como resultado:$S_1= 2.292055$ y $S_2= 11.65167$
   Con estos valores se obtienen los coeficientes  $a_i,b_i, c_i y d_i$ de cada uno de los polinomios cúbicos.
   Los datos se muestran acontinuación:
   
   |   $S_i$   |   $a_i$   |    $b_i$     | $c_i$        | $d_i$ 
   ------------------------------------------------------------------
   |$0 $       |$0.382009$ |       $0 $  |  $2.054591 $  | $2 $     |
   |$2.292055$ |$3.119871$ | $1.146028 $ |  $3.200618 $  |$4.4366$ |
   |$11.65167$ |$-2.589260$| $5.825834 $ |  $6.686549 $  |$6.7134 $|
   |$0$        |           |             |               |         |
   
   Dado que son cuatro puntos y tres subintervalos, se obtienen 3 curvas cúbicas. Los polinomios quedan como:
   $g_0(x)= 0.38201(x-0)^{3}+ 2.0546(x-0)+2 $                               para $0\leq x \leq 1$
   $g_1(x)= 3.11987(x-1)^{3}+ 1.14603(x-1)^{2}+3.200618(x-1)+4.4366 $       para $1\leq x \leq 1.5$
   $g_2(x)= -2.58926(x-1.5)^{3}+ 5.8258(x-1.5)^{2}+6.6865(x-1.5)+6.7134 $   para $1.5\leq x \leq 2.25$
   y finalmente: $g_0(0.66)=3.465509, g_2(1.75)=8.708669.
   """
  




