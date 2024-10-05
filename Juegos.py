import clips

env = clips.Environment()


rules = [
    """
    (defrule recomendacion-last-of-us
        (and (tipo-juego accion)
             (experiencia historia)
             (plataforma playstation))
        =>
        (assert (recomendar "The Last of Us")))
    """,
    """
    (defrule recomendacion-call-of-duty
        (and (tipo-juego shooter)
             (experiencia multijugador)
             (plataforma multiplataforma))
        =>
        (assert (recomendar "Call of Duty")))
    """,
    """
    (defrule recomendacion-zelda
        (and (tipo-juego aventura)
             (experiencia exploracion)
             (plataforma nintendo-switch))
        =>
        (assert (recomendar "Zelda: Breath of the Wild")))
    """,
    """
    (defrule recomendacion-formula1
        (and (tipo-juego carreras)
             (experiencia competitivo)
             (plataforma multiplataforma))
        =>
        (assert (recomendar "Formula 1")))
    """,
    """
    (defrule recomendacion-fifa
        (and (tipo-juego deportes)
             (experiencia competitivo)
             (plataforma multiplataforma))
        =>
        (assert (recomendar "FIFA")))
    """,
    """
    (defrule recomendacion-elden-ring
        (and (tipo-juego rpg)
             (experiencia desafiante)
             (plataforma multiplataforma))
        =>
        (assert (recomendar "Elden Ring")))
    """,
    """
    (defrule recomendacion-fortnite
        (and (tipo-juego battle-royale)
             (experiencia multijugador-masivo)
             (plataforma multiplataforma))
        =>
        (assert (recomendar "Fortnite")))
    """
]


for rule in rules:
    env.build(rule)

def obtener_hechos_usuario():
    tipo_juego = input("¿Qué tipo de juego prefieres (accion, shooter, aventura, carreras, deportes, rpg, battle-royale)? ")
    experiencia = input("¿Qué tipo de experiencia prefieres (historia, multijugador, exploracion, competitivo, desafiante, multijugador-masivo)? ")
    plataforma = input("¿Qué plataforma usas (playstation, nintendo-switch, multiplataforma)? ")

    env.assert_string(f"(tipo-juego {tipo_juego})")
    env.assert_string(f"(experiencia {experiencia})")
    env.assert_string(f"(plataforma {plataforma})")


def ejecutar_recomendacion():
    env.run()
    recomendacion_hecha = False
    for fact in env.facts():
        if 'recomendar' in str(fact):
            recomendacion_hecha = True
            print(f"Recomendación: {fact}")
    
    if not recomendacion_hecha:
        print("No se encontró una recomendación con los criterios proporcionados.")

obtener_hechos_usuario()

ejecutar_recomendacion()


