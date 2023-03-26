define zona = "plaza"

screen mapa:
    if zona == "plaza":
        vbox:
            textbutton ("Mercado") action Jump("Mercado")
            textbutton ("Clases") action Jump("Clases")
            textbutton ("Taberna") action Jump("Taberna")
    
    elif zona == "Mercado":
        vbox:
            textbutton ("plaza") action Jump("plaza")
            textbutton ("Clases") action Jump("Clases")
            textbutton ("Taberna") action Jump("Taberna")
    elif zona == "Taberna":
        vbox:
            textbutton ("plaza") action Jump("plaza")
            textbutton ("Clases") action Jump("Clases")
            textbutton ("Mercado") action Jump("Mercado")
    elif zona == "Clases":
        vbox:
            textbutton ("plaza") action Jump("plaza")
            textbutton ("Taberna") action Jump("Taberna")
            textbutton ("Mercado") action Jump("Mercado")       