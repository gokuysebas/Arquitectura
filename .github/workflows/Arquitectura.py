#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Se genera un capturador para que el usuario de un numero
cantidad = " "
cantidad = input(f"Ingresa el numero a evaluar {cantidad}: ")
cantidad = int(cantidad)
#Se genera el numero anterior al dado por el usuario
numero = cantidad-1
count = 0
#Se genera un for que haga el modulo de cada una de las posibilidades detras del numero dado por el usuario
for i in range(numero):
    #Se genera la logica para determinar si solo es divisible por el mismo
    if cantidad%numero==0 and numero >1:
        count = count+1
        numero=numero-1
    elif numero>1: 
        numero = numero-1
#Se toman los resultados y se verifica que sea un numero primo, posteriormente se imprime en pantaña
if count==0 or cantidad==2:
    print('Es primo')
else:print('No es primo')


# In[ ]:




