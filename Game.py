
import random
import sys
import os

personaje = {}

def TheEnd ():
    print(personaje["nombre"],"encontro la Directasa.")
    print("Se reunen Pazos, Caliebre y Enoc alrededor del hallazgo.")
    print("Lo miran y le pegan una patada. Se la suda muy fuerte.")
    print("DEBERaS CONVENCER A ESTOS TRES PARA QUE SIGAN CON LA DIRECTASA EN...")
    print("THE QUEST FOR DIRECTASA, LA NOVELA VISUAL")
    print("Liga con Pazos, Caliebre y Enoc <3")
    raw_input()
    sys.exit()

def Molyneux ():
    vida = 50
    fuerza = 15

    ganar = False

    print("Hola Soy Moli... Muli... Mo... El tito Peter")
    print("Me vas a permitir matarte...")
    print("Tiene ",vida," puntos de vida")
    while vida > 0:
        print("")
        accion = raw_input("atacar o escapar: ")
        if accion == "atacar":
            vida = vida - personaje["fuerza"]
            if vida <= 0:
                print("Ganaste")
                print("Tu premio es 2 monedas")
                personaje["dinero"] += 2

                return True
            else:
                print("A Peter le quedan",vida,"puntos de vida")
                print("La Peter ataca")
                if personaje["dinero"] <= 0:
                    personaje["vida"] -= fuerza
                    if personaje["vida"] <= 0:
                        print("GAME OVER")
                        sys.exit()
                else:
                    personaje["dinero"] -= fuerza
            printEstado()
        else:
            print("Escapaste")
            return False

    return False

def FINALBOSS ():
    if Molyneux():
        TheEnd()
    else:
        print("No has conseguido derrotar a Peter, como vas a intentarlo con Tito Phil")
        print("Vuelve a probar de nuevo")
        raw_input()
        sys.exit()

def tienda(visitas):
    objetos = {"pocion":[3,"Este brevaje espiritual (para nada alcoholizado) te recuperara toda la salud (podria incluso darte de mas). Usalo en cualquier momento"]
        , "loteria":[7,"Comprando este objeto te dare tantas monedas como diga una ruleta que va de 1 a 15 monedas. Es muy popular"]
        , "6en1":[20,"Esta vieja reliquia podria hacer que una silla dejara de hacer ruido. Muy util en una mazmorra, desde luego"]
        , "pesas":[15, "Este objeto aumentara tu fuerza permanentemente en 1 desde ya. Por problemas de licencias no se llama Pajilleitor"]}
    print("Bienvenido a la tienda de la mazmorra")
    if visitas == 0:
        visitas = visitas +1
        print("Te preguntaras que hace una tienda en mitad de una mazmorra")
        print("Pues bien")
        print("Lo hizo un mago (si quieres saber la enternecedora historia de este tendero, compra el DLC The Quest for Directasa: The Videojocco: The Origin)")
    print("Actualmente tienes ", personaje["dinero"], "monedas" )
    comprar = raw_input("Escribe si quieres comprar (si) o si prefieres hacerle un feo al vendedor (no) ")
    while comprar == "si":
        print("Estos son los objetos que tengo a la venta, di si te interesa alguno: ")
        compra = raw_input(objetos.keys())
        print(objetos[compra.lower()][1])
        print("Esto cuesta ", objetos[compra.lower()][0], "monedas")
        seguro = raw_input("Dime si te lo llevas (si) ")
        if seguro is "si":
            if objetos[compra] > personaje["dinero"]:
                print("Claro que te lo llevas, pero a mi me tienes que dejar algo a cambio sabes")
                print("Vuelve cuando tengas mas cash")
            else:
                print("Transaccion realizada con exito")
                personaje["dinero"] -= - objetos[compra]
                if compra is "loteria":
                    personaje["dinero"] += random.randint(1,15)
                elif compra is "pesas":
                    personaje["fuerza"] += 1
                else:
                    personaje["inventario"].append(compra)
        comprar = raw_input("Escribe de nuevo si quieres comprar (si) o si prefieres hacerle un feo al vendedor (no) ")
    return visitas

def printEstado():
    print("Vida: ",personaje["vida"],"Vida Maxima: ", personaje["maxVida"], "Dinero: ",personaje["dinero"],"Fuerza: ",personaje["fuerza"], "Objetos: ", personaje["inventario"])

def batalla(monstruo):

    print('Aparece un/una ', monstruo["nombre"], ' salvaje')
    print("Tiene ",monstruo["vida"]," puntos de vida")
    while monstruo["vida"] > 0:
        print("")
        accion = raw_input("atacar o escapar: ")
        if accion == "atacar":
            monstruo["vida"] -= personaje["fuerza"]
            if monstruo["vida"] <= 0:
                print("Ganaste")
                monedas = random.randint(1,4)
                print("Tu premio es ", monedas, "monedas")
                personaje["dinero"] += monedas
                if random.randint(0, 50-personaje["Habitaciones Visitadas"]) < 10:
                    print("Ha aumentado tu vida maxima en 5 puntos")
                    personaje["vida"] += 5
                    personaje["maxVida"] += 5
            else:
                print("A ", monstruo["nombre"], " le quedan ",monstruo["vida"]," puntos de vida")
                print("La Lootbox ataca")
                print("Has recibido ", monstruo["fuerza"], " puntos de dano")
                if personaje["dinero"] <= 0:
                    personaje["vida"] -= monstruo["fuerza"]
                    if personaje["vida"] <= 0:
                        print("GAME OVER")
                        sys.exit()
                else:
                    personaje["dinero"] -= monstruo["fuerza"]



            printEstado()
        else:
            print("Escapaste")
            return

def crearHabitacion(putada):
    sala = {}
    posiblesObjetos = ["cofre", "mesa", "vasija"]

    sala["guardian"] = putada
    numObj = random.randint(0,2)
    sala["objetos"] = posiblesObjetos[numObj]

    #ESTO ES PARA CLASES MAS AVANZADAS
    """sala["objetos"] = []
    for i in range(numObj):
        sala["objetos"].append(posiblesObjetos[random.randint(0,len(posiblesObjetos))])"""

    return sala

def generarMonstruo(preferencia):
    monstruo = {}
    posiblesMonstruos = ["Duende", "Hombre Bien Vestido", "Mujer Emperifollada", "Influencer Oscuro"]
    if preferencia == 0:
        nom = random.randint(0,len(posiblesMonstruos)-1)
        monstruo["nombre"] = posiblesMonstruos[nom]
    else:
        monstruo["nombre"] = preferencia

    monstruo["vida"] = random.randint(10, 30) + personaje["Habitaciones Visitadas"]
    monstruo["fuerza"] = random.randint(5,10)
    return monstruo

def explorar(comando, visitasT):
    listaAux = ["izq", "der"]
    while personaje["Habitaciones Visitadas"] < random.randint(5,10):
        if comando == "izquierda":
            comando = "izq"
        else:
            comando = "der"
        putada = random.randint(0,1)
        if random.randint(0,9) < 2:
            visitasT = tienda(visitasT)
        else:
            if comando == listaAux[putada]:
                sala = crearHabitacion(1)
            else:
                sala = crearHabitacion(0)
            personaje["Habitaciones Visitadas"] += 1
            comando = habitacion(sala)
    if visitasT == 0:
        visitasT = tienda(visitasT)
    FINALBOSS()

def habitacion(sala):
    print("Has entrado en una nueva habitacion")
    print("La puerta por la que acabas de entrar desaparece y ves que tienes una puerta a tu izquierda y otra a tu derecha")
    if sala["guardian"] == 1:
        print("Sin embargo, no estas solo en esta habitacion")
        print("De repente una criatura se abalanza sobre ti")
        monstruo = generarMonstruo(0)
        batalla(monstruo)
        print("Ahora puedes explorar la habitacion con mas calma")
    else:
        print("Exploras la habitacion con calma")
    print("Ves que hay diversos objetos")
    print("Los que mas te llaman la atencion son los siguientes: ", sala["objetos"])
    mover = 0
    while mover == 0:
        comando = raw_input("Que quieres hacer ")
        mover, comando = gestionarOpcionGeneral(comando, sala["objetos"])
    print("Has seleccionado ir hacia la ", comando)
    print("Alla vamos pues")
    return comando

def gestionarOpcionGeneral(opcion, objetos):
    posibilidades = ["izquierda", "izq", "derecha", "der", "inv", "estado", "help"]

    while opcion.lower() not in posibilidades and opcion.lower() not in objetos:
        print("Lo siento, no has introducido un comando reconocido. Vuelve a intentarlo o escribe help para ver los comandos reconocidos")
        opcion = raw_input("Vuelve a probar ")

    if opcion == "help":
        print(posibilidades)
        return 0, opcion
    elif opcion == "inv":
        print(personaje['inventario'])
        usar = raw_input("Quieres usar algo (si) ")
        if usar == "si":
            objeto = raw_input("Que quieres usar ")
            while objeto.lower() not in personaje["inventario"]:
                print("No tienes eso objeto, vuelve a probar. Si no quieres usar nada escribe justo eso")
                objeto = raw_input("Tienes lo siguiente: ", personaje["inventario"] )
            if objeto.lower() != "nada":
                usarObjeto(objeto)
                personaje["inventario"].remove(objeto)
        return 0, opcion
    elif opcion == "estado":
        printEstado()
        return 0, opcion
    elif opcion.lower() == "cofre":
        print("Te acercas lentamente al cofre.")
        probMonstruo = random.randint(0,9)
        if probMonstruo < 2:
            print("Parece que hacerse con lo que haya dentro no sera tan facil como parecia.")
            monstruo = generarMonstruo("Loot Box")
            batalla(monstruo)
        print("Te asomas al cofre y coges lo que hay dentro. Consigues...")
        din = random.randint(5,10)
        personaje["dinero"] += din
        print(din, " monedas")
        objetos.remove(opcion)
        return 0, opcion
    elif opcion.lower() in objetos:
        print("Has interacuado con la ", opcion)
        print("Rebuscas bien y encuentras...")
        din = random.randint(1,4)
        personaje["dinero"] += din
        print(din, " monedas")
        objetos.remove(opcion)
        return 0, opcion
    else:
        return 1, opcion


def entrada ():
    print("Has entrado")
    tut = raw_input("Escribe tutorial para leer el tutorial y otra cosa para saltartelo ")
    if tut == "tutorial":
        print("Acabas de entrar en una mazmorra, formada por diferentes salas")
        print("Sin embargo esta es una mazmorra magica. Eso quiere decir que en el momento que dejes una habitacion, no podras volver a la misma sala.")
        raw_input()
        print("Dentro de cada sala puedes encontrar diferentes objetos con los que puedes interactuar y puertas, a traves de las cuales puedes ir a otras salas")

        print("Tu objetivo es internarte en lo mas profundo de la mazmorra, derrotar al mono mago y devolver la Directasa")
        print("Cada vez que entres en una sala leeras una descripcion de la misma (y puede que tengas que derrotar a un monstruo, aunque eso son detalles)")
        print("Esa descripcion te dira que objetos tiene la sala. Escribe ese objeto cuando decidas que hacer para interactuar con el mismo.")
        print("Para salir de una sala escribe derecha o izquierda. Eso te llevara a una nueva sala. Puedes usar tambien der y izq")
        print("Ademas de los comandos de objetos y salida puedes escribir 'inv' para usar un objeto de tu inventario y 'estado' para saber tu estado actual")
        raw_input()
        print("En combate solo puedes atacar o huir, no te flipes. Ya iremos anadiendo cosas")
        print("Buena suerte")
        raw_input()
        print("PD: Escribe 'help' para ver una lista de lo que puedes hacer. Ahora no, solo como comando cuando estes en una sala")
        raw_input()
    print("PDD: Si, exiten. Ahora entraras en una sala de entrenamiento. Una vez la superes, podras adentrarte en la verdadera mazmorra")
    if tut != "tutorial":
        print("PDDD: Si querias saber cual era la PD, no haberte saltado el tutorial")

    salaEjemplo()

def usarObjeto(objeto):
    if objeto == "pocion":
        personaje["vida"] = personaje["maxVida"]
    elif objeto == "pesas":
        personaje["fuerza"] += 1

def salaEjemplo():
    objetos = ["cofre", "mesa", "vasija"] #A completar
    print("Has entrado en una nueva habitacion")
    print("La puerta por la que acabas de entrar desaparece y ves que tienes una puerta a tu izquierda y otra a tu derecha")
    print("Sin embargo, no estas solo en esta habitacion")
    print("De repente una criatura se abalanza sobre ti")
    monstruo = generarMonstruo(0)
    batalla(monstruo)
    print("Ahora puedes explorar la habitacion con mas calma")
    print("Ves que hay diversos objetos")
    print("Los que mas te llaman la atencion son los siguientes: ", objetos)
    #for range(len(objetos))
    mover = 0
    while mover == 0:
        print("Ahora puedes usar los comandos que quieras: recuerda que puedes usarlos que ves con help mas los nombres de los objetos que hay en la habitacion")
        comando = raw_input("Que quieres hacer ")
        mover, comando = gestionarOpcionGeneral(comando, objetos)
    print("Si has sobrevivido a esto estas listo para todo")
    print("Has seleccionado ir hacia la ", comando)
    print("Alla vamos pues")

    explorar(comando, 0)

"""def gestionarOpcionSala(comando, objetos):
    if comando.lower() == "cofre":
        print("Te acercas lentamente al cofre.")
        probMonstruo = random.randint(0,9)
        if probMonstruo < 2:
            print("Parece que hacerse con lo que haya dentro no sera tan facil como parecia.")
            monstruo = generarMonstruo("Loot Box")
            batalla(monstruo)
        print("Te asomas al cofre y coges lo que hay dentro. Consigues...")
        din = random.randint(5,10)
        personaje["dinero"] += din
        print(din, " monedas")
    else:
        print("Has interacuado con la ", comando)
        print("Rebuscas bien y encuentras...")
        din = random.randint(1,4)
        personaje["dinero"] += din
        print(din, " monedas")
    objetos.remove(comando)"""

def inicializarPersonaje(nombre):
    if nombre == "pazos":
        personaje["nombre"] = "Pazos64"
        personaje["vida"] = 25
        personaje["dinero"] = 20
        personaje["fuerza"] = 11
        personaje["maxVida"] = 25
    elif nombre == "caliebre":
        personaje["nombre"] = "Caliebre"
        personaje["vida"] = 40
        personaje["dinero"] = 10
        personaje["fuerza"] = 10
        personaje["maxVida"] = 40
    elif nombre == "enoc":
        personaje["nombre"] = "Enoc"
        personaje["vida"] = 30
        personaje["dinero"] = 15
        personaje["fuerza"] = 12
        personaje["maxVida"] = 30
    elif nombre == "a":
        personaje["nombre"] = "a"
        personaje["vida"] = 100
        personaje["dinero"] = 1000
        personaje["fuerza"] = 50
        personaje["maxVida"] = 100
    else:
        print("Has escogido un nombre al azar, ais que te asiganremos un personaje con estadisticas malas. Si ha sido un error vuelve a empezar")
        personaje["nombre"] = nombre
        personaje["vida"] = 20
        personaje["dinero"] = 5
        personaje["fuerza"] = 7
        personaje["maxVida"] = 20
    personaje["inventario"] = ["pocion", "pocion", "pesas", "nada"]
    personaje["Habitaciones Visitadas"] = 0

#os.system('cls')
print("The Quest for Directasa, The Videojocco")
print("=======================================")
print("")
print("LA DIRECTASA LA ROBo UN MONO MAGO.")
print("La ha escondido en el fondo de una mazmorra.")
print("Quien quieres ser")
opcion = raw_input("pazos, caliebre o enoc: ")

inicializarPersonaje(opcion)

print("Quieres entrar en la mazmorra",personaje["nombre"],"")

respuesta = raw_input("(si/no) ")

if respuesta == "si":
    entrada()
else:
    print("COBARDE GALLINA NO ERES UN SER DE LUZ")
