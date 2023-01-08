# def es_primo(numero):
#     contador = 0


#     for i in range (1, numero + 1):
#         if i == 1 or i == numero:
#              continue 
#         if numero % i == 0:
#              contador += 1
#     if contador == 0:
#         return True 
#     else:
#         return False


# def run ():
#     numero = int(input("Escribe un numero:  "))
#     if es_primo(numero):
#          print("es primo")
#     else: 
#        print("No es primo")

# if __name__ == "__main__":
#      run()

# def es_primo(numero):
#     contador = 0

#     if numero <= 0:
#        return False 


#     for i in range (1, numero +1):
#         if i == 1 or i == numero:
#              continue
#         if numero % i ==0:
#              contador += 1
#              break
#     if contador == 0:
#          return True
#     else: 
#          return False

# def run ():
#     numero = int(input("escribe un numero:  "))
#     if es_primo(numero):
#          print("es primo")
#     else: 
#        print("No es primo")
    
# if __name__ == "__main__":
#      run()


def es_primo(numero):
    

    if numero % 1 == 0 or numero % numero:
      return True
    else:
      return False 


       
def run ():
    numero = int(input("escribe un numero:  "))
    if es_primo(numero):
         print("es primo")
    else: 
       print("No es primo")
    
if __name__ == "__main__":
     run()
