import random

# seguir = True
while True:
  aleatorio = random.randrange(0, 3)
  elijePc = ""
  print("1- Piedra")
  print("2- Papel")
  print("3- Tijera")
  opcion = int(input("Elije alguno"))

  if opcion == 1:
      elijeUsuario = "Piedra"
  elif opcion == 2:
      elijeUsuario = "Papel"
  elif opcion ==3:
      elijeUsuario = "Tijera"
  print("Elejiste:", elijeUsuario) 

  if aleatorio == 0:
      elijePc = "Piedra"
  elif aleatorio == 1:
      elijePc = "Papel"
  elif aleatorio == 2:
      elijePc = "Tijera"
      
  print("La bestia elijio:", elijePc)
  print("...")

  if elijePc == "Piedra" and elijeUsuario == "Papel":
      print("Ganaste, papel coje Piedra")
  elif elijePc == "Papel" and elijeUsuario == "Tijera":
      print("Ganaste, Tijera corta Papel")
  elif elijePc == "Tijera" and elijeUsuario == "Piedra":
      print("Ganaste, piedra machaca tijera")
  if elijePc == "Papel" and elijeUsuario == "Piedra":
      print("Perdiste papel cubre piedra")
  elif elijePc == "Tijera" and elijeUsuario == "Papel":  
      print("Perdiste tijera corta papel")  
  elif elijePc == "Piedra" and elijeUsuario == "Tijera":
      print("Perdiste, Piedra machaca Tijera")
  elif elijePc == elijeUsuario:
      print("empate")

  play_again = input("Quieres jugar de nuevo?")
  if play_again.lower() != "s":
      break