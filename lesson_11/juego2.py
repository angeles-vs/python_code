import random

def iniciar_juego():
  print('Escoge una opción:\n1- Piedra\n2- Papel\n3- Tijera')
  opciones = ['Piedra','Papel','Tijera']
  eleccion = int(input())
  eleccion = opciones[eleccion-1]
  computadora = random.choice(['Piedra','Papel','Tijera'])

  if (computadora == eleccion): print('Empate!')
  elif(eleccion == 'Piedra'):
    if(computadora == 'Tijera'): print('Has ganado')
    else: print('Has perdido')
  elif(eleccion == 'Papel'):
    if(computadora == 'Piedra'): print('Has ganado')
    else: print('Has perdido')
  elif(eleccion == 'Tijera'):
    if(computadora == 'Papel'): print('Has ganado')
    else: print('Has perdido')
  print('Has escogido',eleccion,' y la computadora ',computadora)
  if (input('Seguir jugando? s/n:') == 's'): iniciar_juego()

iniciar_juego()