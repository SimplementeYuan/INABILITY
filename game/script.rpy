# Coloca el código de tu juego en este archivo.

# Declara los personajes:
# Principales
define vr = False
define n = Character("Narrador")
define m = Character("Moyashi", color="#509750")
define al = Character("Alessandra")
define ls = Character("Lacie")
define v = Character("Vara")
define e = Character("Eru")
define dr = Character("Draco")
# Secundarios
define in = Character("R. Ingrid")
define dl = Character("Dalia")
define des = Character(". . .")
define hs = Character("Hermanas Súcubos")
define g = Character("Guardiana de los bosques")
# Terciarios
define po = Character("Aldeano")
define pa = Character("Aldeana")
define lau = Character("Laura")
define wi = Character("William")
define na = Character("Nadia")
define mc = Character("Madre cansada")
define ol = Character("Oliver")
define b = Character("Borracho")
define aca = Character("Anciana")
define aco = Character("Anciano")
define co = Character("Cocinero")
define pa = Character("Panadera")
define jc = Character("Jefe de Cocina")
define loli = Character("Los Lilian")
define gar = Character("Garsa")
define mujer = Character("Mujer")
define Niños = Character("Niños")

#Imagenes:



#Layer image:

layeredimage Moyashi_1:

    group fondos:

        attribute neutral:
            "fondo neutral.png"

        attribute emocionada:
            "fondo feliz.png"

        attribute enfadada:
            "fondo enfadado.png"

        attribute indignada:
            "fondo indignado"

        attribute triste:
            "fondo triste"

        
    group cuerpo:

        attribute neutral:
            "cuerpo neutral moyashi.png"

        attribute emocionada:
            "cuerpo emocionado moyashi.png"

        attribute enfadada:
            "cuerpo enfadado moyashi.png"

        attribute indignada:
            "cuerpo indignado moyashi.png"

        attribute triste:
            "cuerpo triste moyashi.png"

    group ojos:

        attribute neutral:
            "ojos neutral moyashi.png"

        attribute emocionada:
            "ojos emocionado moyashi.png"

        attribute enfadada:
            "ojos enfadado moyashi.png "

        attribute indignada:
            "ojos indignado moyashi.png"

        attribute triste:
            "ojos tristes moyashi.png"

    group boca:
 
        attribute neutral:
            "boca neutral moyashi.png"

        attribute emocionada:
            "boca emocionado moyashi.png"

        attribute enfadada:
            "boca enfadada moyashi.png"

        attribute indignada:
            "boca indignado moyashi.png"

        attribute triste:
            "boca triste moyashi.png"

    group ropa:

        attribute neutral:
            "ropa neutral 1 moyashi.png"

        attribute emocionada:
            "ropa emocionado 1 moyashi.png"

        attribute indignada:
            "ropa indignado 1 moyashi.png"

        attribute triste:
            "ropa triste 1 moyashi.png"

    group peinado:

        attribute neutral:
            "peinado neutral 1 moyashi.png"

        attribute emocionada:
            "peinado emocionado 1 moyashi.png"

        attribute enfadada:
            "peinado enfadado 1 moyashi.png"

        attribute indignada:
            "peinado indignado 1 moyashi.png"

        attribute triste:
            "peinado triste 1 moyashi.png"
    
    always:
        "Circulo.png"

    


# El juego comienza aquí.

label start:

    call cap1 from capitulo_1
    call cap2 from capitulo_2
    # Finaliza el juego:
    if vr == False:
        call capitulo1N from capitulo_1_neutral
    elif vr == True:
        call capitulo_1_vara from capitulo_1_vara
    return
