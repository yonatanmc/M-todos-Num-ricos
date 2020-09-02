#!/usr/bin/env python
# coding: utf-8

# In[32]:


import math
import pandas as pd
# definir la función a evaluar
def f(x):
    funcion = 4*pow(x, 2) - 5*x #pow(x, 2) - 3*x - 1
    return funcion

def metodoBiseccion(xi, xs, margen_error):
    
    #PASO 1 f(xi)*f(xs)<0
    if f(xi)*f(xs)<0:  
        # almacenar datos de cada columna del metodo biseccion
        it_ =[]; xi_ = []; xs_ = []; xr_ = []; fxi_ = []; fxr_ = []; fxixr_ = []; errores_ = [];        
        #PASO 2
        iteraciones = 0           
        xr_anterior = 0       
        margen_error_hallado = 1        
        while margen_error_hallado > margen_error:            
            xr = (xi + xs)/2
            xr_actual = xr            
            margen_error_hallado = abs(xr_actual - xr_anterior)           
            #almacenar los valores en arreglos
            it_.append(iteraciones + 1)
            xi_.append(xi)
            xs_.append(xs)
            xr_.append(xr)
            fxi_.append(f(xi))
            fxr_.append(f(xr))
            fxixr_.append(f(xi)*f(xr))
            errores_.append(margen_error_hallado)            
            #PASO 3
            if f(xi)*f(xr) < 0:
                xs = xr
            if f(xi)*f(xr) > 0:
                xi = xr
            xr_anterior = xr_actual
            iteraciones = iteraciones + 1            
        datos = {"i":it_, "xi":xi_, "xs":xs_, "xr":xr_, "fxi":fxi_, "fxr":fxr_, "fxixr":fxixr_,"Error":errores_}
        datosTabla = pd.DataFrame(datos)
        print(datosTabla.to_string())
        
        print("Solución: iteración ", iteraciones," y raiz = ", xr)
    else:
        print("Utiliza otro método")
    
#mostrando solución
#metodoBiseccion(0, 5, 0.00001)
metodoBiseccion(1, 1.6, 0.00001)


# In[ ]:





# In[ ]:




