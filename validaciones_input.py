


# "84732807492803774"

def validar_input_entero(numero: str) -> int:

    while not numero.isdecimal(): #isdecimal devuelve true, solamente si todo su contenido tiene numeros enteros, ya si tiene comas o letras da false
        numero = input("Numero incorrecto, ingreselo nuevamente: ")
    numero_int = int(numero)

    return numero_int