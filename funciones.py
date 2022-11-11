# Las funciones, yo llamo a una pizzeria y pido una pizza con gaseosa

# def nombre Funcion()
    #codigo
    #codigo
# No hace parte de la funcion
def llamado():
    print('Yo: quiero una pizza')
def pizza():
    print('El senor: La pizza viene en camino')

    print('Yo: Voy a pedir una pizza (estoy llamando)')
    llamado()
    pizza()

# Que va a aparecer?
# A). Yo: voy a pedir una pizza(Estoy llamando), Yo: quiero una pizza
# B). Yo: voy a pedir una pizza (estoy llamando)

def miPc(color, RAM, marca):
    print('Mi pc es color', color, 'tiene una RAM de ', RAM, 'Y es de la marca', marca)
miPc('Gris', '8', 'asus')

def miPerro(color, raza, esjugueton):
    print('mi perro es de color', color, 'es de raza', raza, 'es extrovertido?: ', esjugueton)

color = 'Gris'
raza = 'Schnauzer'
esjugueton = True

miPerro(color, raza, esjugueton)

# Ejercicio: crear una funcion (cualquier nombre) donde le pasen por parametro su edad, nombre y su color de piel

def yomismo(edad, nombre, piel):
  
    print('Yo tengo', edad,'y mi color de piel es: ', piel, 'y tu nombre es: ', nombre)
edad = 17
nombre = 'jhon'
piel = 'moreno'

yomismo(edad, piel, nombre)

with open('mi_fichero', 'w') as f:
    # Procesamiento del fichero
    f.write('Hola mundo\n')
f.close()


