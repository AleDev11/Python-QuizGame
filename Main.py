print('Hola buenas bienvenido a mi Quiz game en Python')

playing = input('¿Quieres jugar? (si/no): ')

if playing.lower() != 'si':
    quit()

print('Comencemos')
score = 0

answer = input('¿Cuantos numeros hay entre el 1 y el 4? ')
if answer.lower() == '2':
    print('Correcto')
    score += 1
else:
    print('Incorrecto')

answer = input('¿Cual es el color del cielo? ')
if answer.lower() == 'azul':
    print('Correcto')
    score += 1
else:
    print('Incorrecto')

answer = input('¿Cual es el color del agua? ')
if answer.lower() == 'azul':
    print('Correcto')
    score += 1
else:
    print('Incorrecto')
    
print('Tu puntaje es', score)
