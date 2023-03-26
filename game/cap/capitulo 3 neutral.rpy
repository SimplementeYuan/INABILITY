
define rana = Character("La rana ladrona")

define camarero = Character("Camarero")

define vendedora =Character("Vendedor")

define hombre_sospechoso =Character("Hombre sospechoso")

define eru =Character("Eru")



define si_plaza =Character("si_plaza")
define tienda_de_instrumentos=Character("tienda_instrumentos")

define plaza =Character("plaza")

define barrio_de_tiendas =Character("barrio_de_tiendas")

define tienda_instrumentos =Character("tienda_instrumentos")

define ropa =Character("ropa")

label capitulo_3_neutral:

"El viaje aunque no demasiado largo, fue lo suficiente para que anocheciera. Las farolas iluminaban la ciudad con su tenue iluminación, edificios aún más grandes y llenos de luz. Moyashi cada vez que visitaba una ciudad se quedaba fascinada."

"El lugar estaba lleno de gente, había todo tipo de criaturas mágicas como elfos, gigantes, dracónidos, vampiros... sin embargo, también convivían  con ellos humanos con tranquilidad."

moya "Oye Lacie, ¿por qué todos estos seres conviven con los humanos?"

lacie "Milius es conocida por dos cosas, por la gran cantidad de artistas que residen allí y, ademas, porque está ubicada en la frontera entre Polintia y Tolando."

lacie "Lo cual provoca que las criaturas mágicas y oscuras convivan con los humanos de allí."

moya "¿Hay divisiones de territorio entre especies?"

lacie "Hay un total de 9 reinos y uno devastado. Cada uno es gobernado por un rey y este dirige a su gente."

lacie "En cada uno hay unas especies predominantes, pero puede vivir cualquier especie donde quiera y se le tratará con respeto, aunque hay alguno que tiene una mentalidad racista y territorial."

moya "En el lugar donde yo vivia la gente era así, por suerte yo no sufrí por ello."

lacie "¿Y de donde vienes?"

moya "De Lator, es un país muy bonito y próspero."

lacie "No conozco ese lugar. Que raro."

"Mientras la cantante se rompía la cabeza al intentar recordar, un intenso olor le vino a la druida, provocando que su estómago tronara en señal de hambre."

lacie "¿Moyashi quieres comer algo? Suena como si no hubieras comido en días."

moya "La verdad es que si pero, primero me gustaría dar una vuelta por la ciudad."

"(Tienes libertad de moverte donde quieras, cuando hayas terminado de investigar pulsa el boton de comer,)"

define zona ="bar"


screen mapa:

    


    if zona =="bar":
        vbox:
            textbutton ("Barrio de tiendas") action Jump ("barrio_de_tiendas")
            textbutton ("Plaza") action Jump("plaza")
            textbutton ("Comer") action Jump("comer")
        

        
    elif zona =="barrio_de_tiendas":
        vbox:
            textbutton ("Bar") action Jump ("bar")
            textbutton ("Tienda de ropa") action Jump("tienda_de_ropa")
            textbutton ("Tienda de instrumentos") action Jump("tienda_de_instrumentos")
    elif zona =="plaza":
        vbox:
            textbutton ("Bar") action Jump ("bar")
            textbutton ("barrio de tiendas") action Jump ("barrio_de_tiendas")
    
    elif zona =="tienda_de_ropa":
        vbox:
            textbutton ("Barrio de tiendas") action Jump ("barrio_de_tiendas")
            textbutton ("Bar") action Jump ("bar")

    elif zona =="tienda_de_instrumentos":
        vbox:
            textbutton ("Barrio de tiendas") action Jump ("barrio_de_tiendas")
            textbutton ("Bar") action Jump ("bar")


            


call screen mapa 

label bar:
    
    $ zona ="bar"
    scene black

    call screen mapa


   


label barrio_de_tiendas:
    $zona ="barrio_de_tiendas"

    scene tiendas

    if barrio_de_tiendas == True:
        "Queda todavía algo por ver."
        call screen mapa

    
    moya "¿Lacie que hay en esta zona?"
    
    lacie "Es un barrio de tiendas, en ellas hay negocios que ofrecen todo tipo de servicios. Podemos entrar a alguna si te apetece."
    
    $ barrio_de_tiendas = True

    call screen mapa

       

    


    

label p:
    $zona ="p"
    scene plaza
if plaza == True:
    "Cuando regresan, se ve que la chica a vuelto a discutir con el camarero. Mejor dejarlos solos"
    call screen mapa

"Al entrar en la plaza notaron algo de barullo en un bar."

"Decidieron acercarse y vieron a una chica con unas botas enormes discutiendo con un camarero en un bar"

desconocido "¡Pero sigueme! ¡Te robé, intenta impedirlo!"

camarero "Eres conocida por toda la ciudad por tus robos, aunque intente impedirlo escaparás, vete, estoy trabajando."

rana "Pe-pero... ¡Si no me persiguen no es divertido!"

"Mientras decia eso la chica hacia pucheros como si fuera un niño pequeño."

"Lo intentó un par de veces más pero, fue inútil. finalmente la chica se fue con la cabeza cabizbaja con una expresión de tristeza y decepción."

moya "Creo que ya he visto todo lo que tenia que ver hoy, mejor vayamanos a otro lado."
$ plaza = True
call screen mapa
    

label tienda_de_ropa:
    $zona ="tienda_de_ropa"
    scene tienda de ropa
    
    if ropa == True:
        vendedora "¡Ah,hola! ¡Disfruta del vestido!"
        jump ropita
    if ropa == False:
        vendedora "¿Has cambiado de opinión?"
        menu:
            "Si":
                $ ropa = True
                moya "Muchas gracias señorita"
                "Miró varias prendas junto a Lacie que la ayudó hasta que se quedó con un vestido bastante largo, se lo llevó en una bolsa de papel"
                moya "Me lo pondré despues de ir a las termas"
                lacie "Podemos ir despues de comer"
                jump ropita

            "No":
                vendedora "Si cambias de opinión, no esperes a mañana."
                jump ropita

    

    "Al entrar en la tienda una muchacha bastante bonita y bien vestida les atendió"

    "Aunque al ver a Moyashi su rostro cambio de golpe"

    vendedora "Señorita, tiene la ropa muy sucia, realmente creo que debería comprarse nueva"

    moya "No tenemos dinero, lo sentimos. No vamos a poder comprarle nada."

    vendedora "Da igual invita la casa, no me gusta ver a una mujer tan bella asÍ. le ruego que acepte alguno de mis diseños."
    
    menu:
        "Aceptarla":
            $ ropa = True
            moya "Muchas gracias señorita"
            "Miró varias prendas junto a Lacie que la ayudó hasta que se quedó con un vestido bastante largo, se lo llevó en una bolsa de papel"
            moya "Me lo pondré despues de ir a la casa de baños"
            lacie "Podemos ir despues de comer"
            jump ropita
        "No puedo aceptarla":
            moya "Lo siento pero no puedo aceptar la ropa si no puedo pagarle, pero muchas gracias"
            "La mujer insistió un poco mas pero finalemente se salieron sin ella"
            $ ropa = False
    
     
    
    label ropita:
    call screen mapa

    label tienda_de_instrumentos:
        
        $zona ="tienda_de_instrumentos"
        scene tienda de instrumentos
        if tienda_instrumentos == True:
            "No hay nada mas que ver en la tienda"
            call screen mapa

        "Al entrar de los ojos de Lacie comenzaron a salir brillitos"

        "Comenzó a mirar cada uno de los instrumentos que habia en la tienda con bastante atencion"

        moya "¿Sabes que no podemos comprar nada no?"

        lacie "Ya pero me gusta ir a las tiendas para ver lo que no me podre comprar"
        
        $ tienda_instrumentos = True
        call screen mapa


label comer:
    
    $ zona ="comer"
    scene black

    "Luego de visitar todo lo que quisieron"

    "Fueron a un bar que parecía bastante caro, un escenario bastante grande, todo muy bien decorado con unos muebles bastante rústicos."
    
    "Lo mejor era el ambiente que había en el lugar, no era demasiado ruidoso pero el único ruido que se podía escuchar eran las risas de los clientes unidos al choque de sus copas para brindar."

    "Antes de que les diera tiempo a sentarse Lacie ya estaba encima del escenario. Se sentó en una silla en el escenario y se dispuso a tocar su violín que lo tenía guardado en una mochilita."
    
    "Al verlo Moyashi decidió sentarse en una de las mesas a escucharla."

    "Tocó una melodía bastante animada, parecía que era una canción que todo el mundo era capaz de reconocer ya que todos empezaron a dar palmas siguiendo el ritmo."
    
    "Tras eso Lacie comenzó a cantar con su voz angelical. Todo el mundo estaba dando palmas y estaba muy animado, Lacie tenía un aura que de alguna forma hacía que tanto niños como grandes estuvieran más alegres."

    moya "¡Lo hicistes genial! Esta vez no fallaste ninguna nota ni nada."

    lacie "Esta canción la conozco desde que tengo uso de razón, si sabes tocarla cualquier persona de estos dos reinos te aplaudirá."

    moya "Ya veo, ¿por qué gusta tanto?"

    lacie "Hace unos años hubo una cantante muy famosa justamente en esta ciudad, su nombre artístico era Luxi. Se cuenta que por donde pasará su canto todo el lugar se llenaba de luz y de alegría. Yo sueño por llegar a ser como ella."

    moya "Bueno aquí lo has conseguido."

    lacie "Si, pero no, las canciones de ella son mágicas, cualquiera que sepa cantarla medianamente bien, provocan una reacción parecida. Canciones propias no tengo y otras no tienen el mismo efecto."

    "Un camarero se acercó a atenderlas mientras continuaban hablando."

    camarero "¿Qué desean pedir? Les damos un descuento para las bebidas."

    "Pidieron un par de zumos, y se los trajeron junto a unos pequeños platos de comida."

    "Disculpe no hemos pedido esto"

    "Son tapas vienen incluidas con la comida, son gratis no se preocupe, es una costumbre típica de Keroma."

    "Cuando la muchacha terminó de servir Lacie le comentó a su compañera."

    lacie "Es algo muy típico de aquí y como tengo falta de dinero me ayuda a mantenerme con vida."

    moya "Eso te pasa por escaparte de casa."

    lacie "Ya, por eso asumo las consecuencias de mis actos economizando."

    "Al rato de estar comiendo y charlando Moyashi cortó la conversación."

    moya "Oye me haría falta orinar."

    lacie "Hay un cuarto de baño de mujeres allí."

    moya "¿Qué es eso?"

    lacie "Oh es cierto, es un invento algo nuevo y que solo tienen las clases acomodadas. Mira, tienes que ir a la habitación de allí, habrá una especie de silla de madera con agujero en medio."
    lacie "Te sientas, haces lo que tengas que hacer. Y después de eso hay una palanca, la usas y ya."

    "Asintió y fue a hacerlo como le dijo."

    "Mientras la esperaba un señor mayor bastante ebrio se acercó a Lacie."

    "¿Donde tan bonita y tan sola?"

    lacie "No estoy sola estoy con mi amiga"

    hombre_sospechoso "Bueno moza, como ahora mismo no está aquí, podemos divertirnos un rato"

    "Ella se levantó de la silla e intentó apartarse de él, pero no paraba de acercarse a ella."
    
    "Continuaron así hasta que la chica chocó contra una pared. El hombre se acercaba a ella lentamente, el olor a alcohol se hacía cada vez más fuerte conforme se acercaba y le daba ganas de vomitar,"
    
    "colocó su mano en la pared para intimidarla mientras le miraba el pecho."

    hombre_sospechoso "Que bonita eres... me gustas mucho."

    "Le decía mientras babeaba a centímetros de ella."

    "Mientras ella estaba asustada Moony acudió a su rescate. Pero antes de poder hacerle nada le pegó una patada que la dejó en el suelo."

    "Al verlo intentó lanzarle una bola de fuego pero la golpeó en la mano desviando la esfera antes de que le golpeara."

    "Le puso las manos contra la pared para que no pudiera moverse."

    "Tranquila preciosa, vamos a pasarlo bien."

    "Todas las personas del lugar estaban viendo la situación pero nadie hizo nada. En parte por miedo y por otra porque no querían meterse en problemas."

    "Afortunadamente alguien se levantó de la silla. Y se dispuso a hablar."

    desconocido "¡No la toques!"

    "Gritó el muchacho"

    "El hombre se giró y observó al pequeño hombrecillo,  bastante bajito, delgaducho y con gafas."

    hombre_sospechoso "¿Y que me vas hacer pequeñajo?"

    "El hombre, se acercó a él y lo agarró fuerte del cuello mientras lo elevaba. Le estaba apretando muy fuerte, provocando que respirara con mucha dificultad. Intentaba resistirte pero no tenía demasiado éxito."

    "Por desgracia para el matón Lacie estaba preparando un ataque desde atrás. Con esa pierna le propinó un fuerte golpe en la entrepierna."
    
    "Provocando que soltara al chico y se callera al suelo de dolor mientras se agarraba en su lastimada intimidad."

    "Con un increíble dolor por el golpe se fue caminando del lugar lentamente."

    "Mientras tanto Lacie ayudaba a levantarse al muchacho que estaba tirado en el suelo todavía."

    lacie "¡¿Estás bien no te hizo daño?!"

    desconocido "Si, no te preocupes estoy bien, ¿te hizo algo?"

    lacie "Yo estoy perfectamente."

    desconocido "Menos mal me aterraba que hubiera podido hacerte algo, jamás me lo perdonaría."

    "Al escucharlo se sonrojo un poco y continuó hablando."

    lacie "P-pero, ¿por qué fuiste a ayudarme?"

    desconocido "No podía permitir que hicieran daño a alguien, y menos a una chica tan talentosa."

    lacie "N-No soy tan buena como dices."

    "Al notar lo nerviosa que estaba él también se puso nervioso al darse cuenta de que se comportó como un héroe para salvarla, comenzó una maniobra evasiva."

    desconocido "B-Bueno, he de irme, es tarde ya."

    "Intentó huir a toda velocidad pero Lacie le agarró la mano antes de que pudiera irse."

    lacie "A-Al menos dime tu nombre."

    eru "Me llamo Eru, soy un joven ingeniero de Karelbia."

    "Tras esas palabras desapareció, dejando a Lacie de pie completamente pasmada."

    "A su vez, Moyashi salió del baño completamente entusiasmada."

    moya "Lacie, Lacie. Tiré de palanca y de golpe salió agua que empujó el pis, ¿cómo funciona eso?, ¿es magia?"

    "Le preguntó a su compañera muy impactada, sin embargo no respondió."

    "Oye, ¿estás bien?"

    "Cuando pudo espabilarse un poco, dejaron el pago en la mesa y salieron del local en busca de un hotel, ya que era bastante tarde y tenían que descansar."

    "Por el camino Lacie le fue explicando lo que pasó mientras ella estaba ausente."

    lacie "Era un chico, delgado, con el pelo moreno despeinado, los ojos de color avellana, bastante apuesto, aunque menudos harapos llevaba."

    moya "Parece que era lindo, aunque lo importante es que te ayudó cuando nadie se atrevió a hacerlo."

    lacie "Si! Ojalá pueda verlo otro día."

    "Llegaron a un pequeño hotel de mala muerte. Lacie no tenía demasiado dinero, por lo tanto tuvieron que economizar. Se tumbaron las dos en la cama agotadas, hasta que se tuvieran que levantar otra vez."

    jump capitulo_4_neutral






    






