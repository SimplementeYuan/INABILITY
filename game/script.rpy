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
define ca = Character("Camarero")
define pa = Character("Leonor")
define jc = Character("Jefe de Cocina")
define loli = Character("Los Lilian")
define gar = Character("Garsa")
define mujer = Character("Mujer")
define Niños = Character("Niños")

#Imagenes:



#Layer image:

layeredimage Moyashi:

    group fondos:

        attribute f_n:
            "fondo neutral.png"

        attribute f_f:
            "fondo feliz.png"

        attribute f_e:
            "fondo enfadado.png"

        attribute f_i:
            "fondo indignado.png"

        attribute f_t:
            "fondo triste.png"

        
    group cuerpo:

        attribute c_n:
            "cuerpo neutral moyashi.png"

        attribute c_f:
            "cuerpo emocionado moyashi.png"

        attribute c_e:
            "cuerpo enfadado moyashi.png"
            
        attribute c_i:
            "cuerpo indignado moyashi.png"

        attribute c_t:
            "cuerpo triste moyashi.png"

    group ojos:

        attribute o_n:
            "ojos neutral moyashi.png"

        attribute o_f:
            "ojos emocionado moyashi.png"

        attribute o_e:
            "ojos enfadado moyashi.png"

        attribute o_i:
            "ojos indignado moyashi.png"

        attribute o_t:
            "ojos tristes moyashi.png"

    group boca:
 
        attribute b_n:
            "boca neutral moyashi.png"

        attribute b_f:
            "boca emocionado moyashi.png"

        attribute b_e:
            "boca enfadado moyashi.png"

        attribute b_i:
            "boca indignado moyashi.png"

        attribute b_t:
            "boca triste moyashi.png"

    group ropa:

        attribute rn_1:
            "ropa neutral 1 moyashi.png"

        attribute rf_1:
            "ropa emocionado 1 moyashi.png"

        attribute re_1:
            "ropa enfadado 1 moyashi.png"

        attribute ri_1:
            "ropa indignado 1 moyashi.png"

        attribute rt_1:
            "ropa triste 1 moyashi.png"

    group peinado:

        attribute pn_1:
            "peinado neutral 1 moyashi.png"

        attribute pf_1:
            "peinado emocionado 1 moyashi.png"

        attribute pe_1:
            "peinado enfadado 1 moyashi.png"

        attribute pi_1:
            "peinado indignado 1 moyashi.png"

        attribute pt_1:
            "peinado triste 1 moyashi.png"
    
    always:
        "Circulo.png"

    


# El juego comienza aquí.

label start:

    call cap1 from capitulo1
    call cap2 from capitulo2
    # Finaliza el juego:
    if vr == False:
        call capitulo1N from capitulo1neutral
    elif vr == True:
        call capitulo1vara from final_malo_1
    return
