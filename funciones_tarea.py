# Ejercicios

# 2 - Crear una funcion sin parámetros que retorne el año actual como numero entero

# 3 - Crear una función que dado un parametro que corresponde a un nombre, salude.

# 5 - Crear una funcion con parámetros que dado un radio, calcule el area de un circulo

# 9 - Crear una función con parametros que dada una palabra y una letra, retorne 
#       la cantidad de letras coincidentes que tiene esa palabra

# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras
#       y retorne dicha cantidad como un entero.

# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego
#       calculará cual de ellas tiene mayor cantidad de letras y tendra que imprimirla en consola
#       junto con la cantidad de letras que posee

#Punto 2 
# (para comentar una selección [Ctrl+k --> Ctrl + c])
# def temporada_actual () -> int:
#     """Esta función da el año en transcurso
#     Args:
#         No es necesario adjuntar parámetros

#     Returns:
#         _type_: int
#                Retorna el año actual en forma de
#                numero entero
#     """
#     temporada = 2024
#     return temporada

# print(temporada_actual())

#punto 3

# def saludo(nombre:str)-> None: 
#     """Esta función genera un saludo con nombre
#     por consola
    
#     Args:
#     nombre(str):Nombre de la persona a saludar
    
#     return: None, no es necesario retornar algo"""
#     mensaje = f"Hola {nombre}! ¿Cómo estas?"
#     print(mensaje)

# ingresar_nombre = input("Por favor, ingrese su nombre :")
# saludo(ingresar_nombre)


#punto 5 puede retornar o no el resultado

# def calcular_area_circulo(radio:float) -> float:
#     """Esta función calcula el área de un circulo
#     colocando como parámetro la radio del mismo
    
#     Args:
#         radio(float): radio del círculo a calcular

#     Returns:
#         float: El resultado del cálculo del área circular
#     """
#     PI = 3.14
#     area_circular = PI * ((radio)**2)
#     return area_circular

# print(calcular_area_circulo(425))


#punto 9

# def coincidir_letras(palabra:str , letra:str)->int:
#     """Esta función, dado una palabra y una letra, detecta
#        la cantidad de coincidencias entre ellas y lo retorna
#       Args:
#           palabra(str): palabra a ingresar
#           letra(str): letra a ingresar
#       Returns:
#              _type_:int
#              Retorna la cantidad de coincidencia encontradas 
#     """
#     coincidencia_letras = 0

#     for elemento in range(len(palabra)):
#         palabra[elemento]

#         if(palabra[elemento]) == letra:
#             coincidencia_letras += 1
        
#     return coincidencia_letras

# palabra = input("Ingrese una palabra: ")
# letra = input("Ingrese una letra: ")
# print (coincidir_letras(palabra,letra))


#ESTA PARTE ES UN BORRADOR

# letra = "a"
# palabra = "alan"
# contador_coincidencia = 0
# palabra = list(palabra)


# for elemento in range(len(palabra)):
#     palabra[elemento]
#     #print(palabra)
#     print(f"el numero del elemento es :{elemento}")
#     print(f"el elemento es :{palabra[elemento]}")

#     if (palabra[elemento]) == letra :
#         contador_coincidencia += 1
#         print("hay coincidencia de letras")
#     else:
#         print("no hay concidencia de letras")

#     print(f"La cantidad total de coincidencias es: {contador_coincidencia}")
# print(f"coincidencia de letras final = {contador_coincidencia}")

#ESTA PARTE ES UN BORRADOR


#punto 10


# def contar_cantidad_letras(palabra:str) -> int :
#     """Esta función, dado a una palabra, cuenta su cantidad
#        total de letras y luego las retorna como entero     
#        
#    Args:
#        palabra(str): la palabra a ingresar 
#
#    Returns:
#        _type_: int
#               Retorna la cantidad total de letras de
#               la palabra
#     """
#     total_letras = 0
#     for i in range( len ( palabra ) ):
#         total_letras += 1
    
#     return total_letras

# palabra = input("Ingrese una palabra : ")

# print(contar_cantidad_letras(palabra))




#punto 11

# def mostrar_palabra_con_mas_letras():
#     """Pide 3 palabras, calcula cuál de ellas tiene la mayor cantidad
#         de letras y luego muestra por consola dicha palabra junto con la 
#         cantidad de letras que posee
#     Args:
#         No es necesario adjuntar parámetros

#     Returns:
#         _type_: None
#     """
#     palabra_uno = input("Por favor, ingrese la primer palabra: ")
#     palabra_dos = input("Por favor, ingrese la segunda palabra: ")
#     palabra_tres = input("Por favor, ingrese la tercer palabra: ")

#     if (len(palabra_uno) > len(palabra_dos)) and (len(palabra_uno) > len(palabra_tres)):
#         palabra_con_mas_letras = palabra_uno
#     elif(len(palabra_dos) > len(palabra_tres)):
#         palabra_con_mas_letras = palabra_dos
#     else:
#         palabra_con_mas_letras = palabra_tres

#     mensaje = f"la palabra con mas letras es *{palabra_con_mas_letras}* , con un total de {len(palabra_con_mas_letras)} letras"

#     print(mensaje)  


# mostrar_palabra_con_mas_letras()



#soluciones en clase

#punto 10

def contar_letras_texto(texto:str)-> int:
    contador_caracteres = 0

    for caracter in texto:
        contador_caracteres += 1
    
    return contador_caracteres


#PUNTO 11

def ingresar_palabras():

    cantidad_caracteres_mayor = None
    palabra_mas_larga = None

    for i in range(3):

        palabra = input(f"ingrese la palabra {i + 1}° palabra: ")

        if cantidad_caracteres_mayor == None or 