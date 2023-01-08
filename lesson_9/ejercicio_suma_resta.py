def run():
    menu = """

    Bienvenido a tu calculadora mágica, ingresa el resultado correcto y recibe maravillosos premios

    Para sumar, escribe 1...
    Para restar, escribe 2...

    Elige una opción: 

    """


    opcion = int(input(menu))

    while opcion != 1 and opcion !=2:
         print("\nIngresa una opcion correctan\n")
         opcion = int(input(menu))
         continue
    numero1 = int(input("\nEscribe el primer numero: "))
    numero2 = int(input("\nEscribe el segundo numero: "))
    if opcion == 1:
       operacion(numero1, numero2, "+", "suma")
    elif opcion == 2:
        while numero1 < numero2:
            print("\nLo siento no puedes restar por ahora, el primer numero debe ser mas grande. Vuelve a intentarlo")
            numero1= int(input("\nEscribe el primer numero: "))
            numero2= int(input("\nEscribe el segundo numero: "))
            continue
        operacion(numero1, numero2, "-", "resta")
    else:
       print("\nIngresa una opcion correcta\n") 


def operacion(numero1, numero2, simbolo, opcion):
     contador = 1 
     while contador <= numero1:
         contador += 1
     print("\n{}\n". format(simbolo))
     contador = 1
     while contador <= numero2:
         contador += 1


     if simbolo == "+":
         result = numero1 + numero2
     elif simbolo == "-":
         result = numero1 - numero2

    
     numero = int(input("Escribe el resultado de la {}: ". format(opcion)))
     if (numero != result):
         numero = int(input("PERDISTE {}: ". format(opcion)))
     else:
        print("Es correcto el resutlado de la {} es {}. Felicidades!!". format(opcion, result))
     
         

     if (input('Seguir practicando? s/n:') == 's'): run()

if __name__ == "__main__":
    run()