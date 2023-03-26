
define elfo =Character("Elfo")




label capitulo_5:

    "Al día siguiente."

    "Lacie se echó la crema por la noche y por la mañana estaba bastante mejor. Podia moverse sin hacerse daño gracias a los dos dias de reposo, aunque las quemaduras todavia no se iban del todo."

    lacie "Como ya puedo moverme bien, por lo que podemos ir rapido a la capital a ver la reina."

    draco "¿De verdad tenemos que ir a ver a esa 'mujer'?"

    "Dijo asqueado."

    moya "¿Hay algun problema con ella?"

    draco "No... No pasa nada, no se preocupen."

    lacie "Pues si no hay nada mas que decir, ¡en marcha!"

    "Agarraron sus cosas y continuaron su travesia."

    "El viaje fue largo y arduo, pero pudieron llegar a la capital."

    "Decidieron pararse a visitar la ciudad antes de ir a comer."


define zona2 ="plaza2"


screen mapa2:

    


    if zona2 =="plaza2":
        vbox:
            textbutton ("Afueras de la ciudad") action Jump ("afueras")
            textbutton ("Herbolario") action Jump("herbolario")
            textbutton ("Comer") action Jump("comer2")
        

        
    elif zona2 =="herbolario":
        vbox:
            textbutton ("Plaza") action Jump ("plaza2")
            textbutton ("Afueras de la Ciudad") action Jump("afueras")
        
    elif zona2 =="afueras":
        vbox:
            textbutton ("Plaza") action Jump ("plaza2")
            textbutton ("Lago") action Jump ("lago")
            textbutton ("Barrio peligroso") action Jump ("barrio")
    
    elif zona2 =="lago":
        vbox:
            textbutton ("Afueras de la ciudad") action Jump ("afueras")
         

    elif zona2 =="barrio":
        vbox:
            textbutton ("Afueras de la ciudad") action Jump ("afueras")


call screen mapa2

label plaza2:
    

    $ zona2 ="plaza2"
    scene black
    call screen mapa2


label herbolario:
    $ zona2 ="herbolario"
    
    if herbolario == True:
        "No hay nada mas que ver por aquí"
        
        call screen mapa2

    "Entraron al herbolario. Estaba lleno de plantas y especias curativas que Moyashi queria revisar. En el mismo se encontraron como responsable del negocio a un elfo."

    "El mismo se veia algo joven pero al ser un elfo lo mas probable es que tenga mas edad de lo que imaginan."

    "Y en su aspecto habia algo que llamo la atencion de Moyashi"

    moya "Hola, amo su negocio me parece un lugar ciertamente agradable."

    elfo "Muchas gracias por sus bonitas palabras, de hecho..."

    "Agarró una semilla y de la misma salió un pequeño rosal. Cortó un ramo y se lo ofreció."

    moya "¿Tambien eres un druida? Que interesante todavia no habia conocido ninguno en estas tierras."

    "Aceptó el ramo y comenzó a oler el aroma."

    "Lacie aprobechó la situacion para vengarse."

    lacie "¿Te gusta? Ella tambien es druida y... está soltera y sin compromiso."

    elfo "Jajajaja, que graciosa es tu hermanita. Por desgracia tengo pareja y nos vamos a casar"

    moya "Ay que lindo. ¿Cuando es la boda?"

    elfo "La semana que viene, estamos muy emocionados."

    moya "Les deseo mucha suerte en su matrimonio."

    "Tras eso se despidieron y dejaron la tienda"

    $ herbolario = True
        
    call screen mapa2


label lago:
    $ zona2 = "lago"

    if lago == True:
        "Creo que no se nos a perdido nada por aquí"
    
    "Llegan a un lago de agua cristalina."


label afueras:
    $zona2 ="afueras"

    if afueras == True:
        "¿Adonde vamos ahora?"

        call screen mapa2

    "Al llegar a las afueras de la ciudad todo estaba mas tranquilo, podian respirar aire fresco y alejarse un poco de todo el ajetreo."

    "En la misma vieron una silueta que les resultaba familiar"

    "Era la rana ladrona y estaba sentada en un banco pensativa."

    moya "Tu eres la chica que vimos hace un par de dias peleandose con un camarero."

    rana "Siento que tuvierais que ver ese espectaculo. El plan era robarle y que saliera corriendo a por mi."

    rana "Pero el muy aburrido ni lo intentó."

    lacie "¿Por qué te llaman así?"

    rana "Me llaman así por mis botas, la suela con un sistema de muelles de titanio y puedo saltar muy alto."

label barrio:
    $ zona2 ="barrio"
    
    if barrio == True:
        "Creo que no quiero volver aquí"
        
        call screen mapa2


label comer2:

    $ zona2 ="comer2"
    

    "Entraron dentro de un pequeño restuarante con un escenario y se pararon a comer."

    "Pidieron bebidas pero después de eso Lacie no fue capaz de resistirse. Salió al escenario y se dispuso a cantar y tocar."

    "Una de las cosas que estuvo haciendo durante el viaje hasta allí fue componer una canción. Era una canción bastante animada como las de Luxi,"
    
    "pero tenía un tono dulce que la diferenciaba. La gente estaba encantada y todo el mundo disfrutaba del espectáculo."

    "Mientras tanto Eru acababa de llegar también a la ciudad, fue caminando tranquilamente hasta que vio algo que le llamó la atención."
    
    "Una mujer con armadura sentada en el suelo al lado de un bar. Siguió caminando y cuando iba a pasar por el bar pero intentó rodearla un poco ya que le daba mal rollo."

    "Sin embargo escuchó una voz que le resultaba familiar. Entró dentro del antro y vio a la chica y la escuchó cantar, sus pies se comenzaron a mover solos dando pequeños golpes siguiendo el ritmo."

    "Llegó un punto que simplemente la música le llamó y eso le atrajo más cerca del escenario provocando que la cantante lo viera y algo sonrojada le diera la mano para que subiera con él."

    "Aunque algo sorprendido por el atrevimiento de la chica y agarró su mano, la cual era muy suave y cálida, provocando un suave sonrojo. Finalmente con la ayuda de ella se subió con un pequeño saltó."

    lacie "Q-Qué te trae aquí?- Preguntó con una sonrisa nerviosa."

    eru "Te escuché mientras caminaba, tu música me pareció maravillosa, p-podemos bailar?"

    lacie "Pero, tengo que seguir tocando y para colmo no sé bailar."

    "Un hombre, que estaba observado muy interesado en el panorama, comenzó a improvisar una canción con su guitarra."

    "Eru la agarró de la mano con suavidad y un poco de temblor y comenzó a bailar junto a ella, Lacie le seguía el ritmo mientras cantaba de forma improvisada junto a la canción."
    
    "En cada paso que daba se notaba que el chico sabía lo que estaba haciendo y se sentía todo muy armónico estando los dos juntos en el escenario."

    moya "«Ese chico… Creo que debería dejarlos solos, a ver qué pasa» Pensó Moyashi mientras la veía."

    moya "¿Oye vamos a darnos una vuelta?"

    draco "Disculpe pero... Yo tengo hambre."

    ale "Podriamos aprovechar para tener el duelo que me debes. Despues comemos."

    moya "Me parece una gran idea. Venga vamos fuera."

    "Draco aceptó con desgana y dejaron a la parejita sola."

    "Eru y Lacie lo estuvieron dando todo en el escenario, la gente estaba animada y todos estaban dando palmas siguiendo el ritmo,"
    
    "cuando terminó la canción fueron a sentarse algo cansados. La camarera les invitó a comer lo que quisieras pero pidieron algo sencillo, por el momento querían descansar."

    lacie "¡Bailas genial! ¿Dónde has aprendido todo eso?"

    eru "A mi madre le ha gustado siempre bailar desde pequeña y me ha enseñado un par de cosas. Además eso no es nada, ¡esa forma de cantar no la he visto nunca!"

    lacie "Aprendí escuchando mucha música y mucha práctica . Mi estilo tampoco es destacable, sólo me baso en parte en Luxie, la mejor cantante y con un arte inigualable."

    eru "No la conozco, supongo que en Kalema no es tan famosa."

    lacie "Deberías escucharla, es asombrosa… O eso creo..."
    
    "Por un momento se le rompió la voz al recordar lo que pasó. No sabía exactamente si lo que tenía era una maldición, pero el pensar que la mujer que más admira le pudiera hacer algo, le hacía mucho daño."

    "El chico notó la angustia en la expresión de ella, por lo que intentó cambiar de tema."

    eru "¿Y qué hacéis en esta ciudad?"

    lacie "Pues estamos de viaje, tenemos que hablar con la reina. ¿Y tú?"

    eru "La reina..."

    lacie "¿Pasa algo?"

    eru "No, no es nada."

    lacie "Estoy segura de que si, dimeloooo."

    eru "No puedo es secreto."

    lacie "Malo."

    "Lacie hizo pucheros y puso carita de pena. Eru no pudo resistirse."

    eru "Tengo que infiltrarme en el castillo. Hay una informacion que necesito revisar."

    lacie "Uy que interesante ¿puedo ayudar?"

    eru "¿No teneis que ir a verla?"

    lacie "Mis compañeros si, pero puede ir uno o dos a pedirla y a distraer mientras nos infiltramos."

    eru "Pero la idea es ser sigilosos… Y si voy con más personas podríamos llamar  la atención."

    lacie "¡Pero podemos ayudarte a distraerlos mientras sigues con la misión!"

    eru "Es cierto, sin embargo…"

    "Lacie la miró a los ojos con mirada de corderito. Eru intentó resistirse, era demasiado difícil."

    eru "Lo siento pero es una misión importante."

    lacie "Porfa porfa porfaaaa."

    eru "De verdad lo siento…"

    lacie "Bueno me las apañare..."
    
    eru "Bueno me tengo que despedir. Tengo cosas que hacer."

    "El chico se fue y Lacie se quedó esperando a sus compañeros."

    "Los demas fueron a una pequeña explanada en las afueras."

    "Moyashi se quedó mirando sentada en un banco mientras sus compañeros se preparaban para el duelo."

    draco "Reglas de esgrima. El primero en tocar al otro tres veces gana. ¿Le parece bien?"

    ale "Me parece perfecto."

    "Los dos sacaron su espada y se pusieron en posicion de combate."

    "El duelo comenzó y comenzaron a chocar sus espadas."

    "La espada de Alessandra era mas ancha y le costaba mas moverla y l de draco era ligera y puzante."

    "Los movimiento de la guerrera eran bastante mas rapidos aun así y se veia mas preparada en el arte del combate. Puedo ganarle las tres rondas facilmente."

    draco "Veo que eres fuerte. Mi especialidad es el asesinato por lo que, es comprensible que pierda en un duelo."

    "Cuando terminaron volvieron todos juntos con Lacie."

    lacie "¡Tenemos que colarnos en el castillo esta noche!"

    moya "¿Para que? El palacio estara abierto por la fiesta."

    lacie "Eru tiene que buscar algo importante y tenemos que ayudarle."

    moya "No vamos a colarnos en el palacio, nos vamos a meter en problemas."

    lacie "¡Pero!"
    
    moya "Ni peros ni nada."
    
    moya "Por cierto draco necesito pediros un favor."

    draco "¿Necesitais dinero?"

    moya "No lo necesitamos pero si vamos a ir a ver a la reina tendremos que ir bien vestidos."

    "Draco le entregó a Moyashi el vestido que estaba haciendo Lacie para ella y que dejó a medias hace unos días."

    draco "Lo terminé la noche que fuisteis al concierto."

    draco "Con esto ya no deberiamos tener problema. Lacie puedo presuponer que tiene más ropa, lo que tengo algo de duda es nuestra nueva compañera."

    ale "¿Qué pasa?"

    "Decidieron ir a la ciudad en busca de una tienda de ropa. Se metieron en una tienda de moda femenina y comenzaron a buscarle ropa femenina a Alessandra."

    "La cual al descubirlo no estaba muy contenta."

    ale "¿Un vestido? ¿Es una broma no?"

    moya "Si, vamos a una fiesta organizada por la reina tenemos que ir bien arreglados."

    ale "¿Y si nos atacan? Debo estar preparada para unirme a la batalla en cualquier momento."

    moya "Solo vamos a pedir informacion. No tenemos porque pelear."

    ale "Ademas... ¿Un vestido?"

    lacie "¡Son geniales! Como pueden no gustarte, son preciosos pareceras una princesa o una dama de alto estatus."

    ale "Son incomodos, y debo estar preparada para el combate."

    moya "Pues vas a tener que ponerte uno, por que si no, es posible que ni te dejen entrar."

    












    



    






