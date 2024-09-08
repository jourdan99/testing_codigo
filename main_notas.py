from funciones.funciones.funciones_auxiliares import mostrar_numeros_primos_hasta
from funciones.funciones.validaciones_input import validar_input_entero

#de un archivo importar la funcion tal

numero_str = input("ingrese un numero para mostrar numeros primos hasta su numero ingresado")
#Validar ese numero
#Parsearlo a entero
numero_int = validar_input_entero(numero_str)

mostrar_numeros_primos_hasta(numero_int)


#otra forma de importar

import funciones.funciones.funciones_auxiliares as funciones_auxiliares

#para llamar a la funcion que necesito
#si o si debo escribir el nombre de la funcion antes de la funcion
#ej:
funciones_auxiliares.mostrar_numeros_primos_hasta()


#ponerle un alias al modulo , tambien se puede utilizar un alias en una funcion (con esto le cambiamos los nombres)
#los alias evitamos confundir funciones que se llaman igual y que vienen de lugares distintos , las renombramos para que no entren en conflicto
# algunas funciones pueden estar desarrolladas y otras no
#lo que sucede aveces que las funciones se pisan, entonces queda como valida la ultima que pusiste
#ponerle un alias , evita que se pisen las funciones que se llaman igual


import funciones.funciones.funciones_auxiliares as aux #esto (aux) seria el alias , para hacerlo mas corto

aux.mostrar_numeros_primos_hasta()

#otra forma es importar absolutamente todo

from funciones.funciones.funciones_auxiliares import *  #el asterisco es importar todo lo de ahí sirve para llamar sin utilizar un prefijo o alias
#pero que pasa? aveces no usamos todo lo de ahí , solo necesitamos ua herramienta



#importar 3 funciones de ejemplo_3.py (del mismo modulo)

from ejemplo_3 import bienvenida,es_multiplo,validar_si_es_primo

#otra forma de importar 3 funciones

from ejemplo_3 import (
    validar_si_es_primo, es_multiplo,bienvenida,
    calcular_area_rectangulo,mostrar_numeros_primos_hasta
)


#cada vez que importemos , tenemos que ver que no haya llamadas en el modulo que estamos importando
#porque se ejecutan cosas que no queremos que lo hagan
#accede al modulo , busca la funcion y en ese interin termina ejecutando el codigo suelto a lo ultimo

#para poder "saltar esas impresiones que aparecen , podemos hacer un if"

if __name__ -- "__main__": #solamente cuando el nombre de este modulo sea main, ejecuta el codigo que eesta aca:
    #ejemplo de ejemplo_3.py
    bienvenida()
    calcular_area_rectangulo(15, 4)
    calcular_area_rectangulo(altura=4, base=15)
    print(es_multiplo(15,4))

    mostrar_numeros_primos_hasta(1100)



    