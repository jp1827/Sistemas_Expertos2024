class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.arcos = []

    def agregar_arco(self, destino, etiqueta_arco):
        self.arcos.append(Arco(self, destino, etiqueta_arco))


class Arco:
    def __init__(self, origen, destino, etiqueta):
        self.origen = origen
        self.destino = destino
        self.etiqueta = etiqueta

    def __str__(self):
        return f"{self.origen.etiqueta} -- {self.etiqueta} --> {self.destino.etiqueta}"


class RedSemantica:
    def __init__(self):
        self.nodos = []

    def crear_nodo(self, etiqueta):
        nodo = Nodo(etiqueta)
        self.nodos.append(nodo)
        return nodo

    def agregar_arco(self, origen, destino, etiqueta_arco):
        origen.agregar_arco(destino, etiqueta_arco)

    def mostrar_red(self):
        for nodo in self.nodos:
            for arco in nodo.arcos:
                print(arco)

    def buscar_recomendacion(self, genero, duracion, estilo):
        recomendaciones = []
        for nodo in self.nodos:
            
            if self.es_pelicula(nodo):
                tiene_genero = any(arco.destino.etiqueta.lower() == genero.lower() and arco.etiqueta == "tiene_género" for arco in nodo.arcos)
                tiene_duracion = any(arco.destino.etiqueta.lower() == duracion.lower() and arco.etiqueta == "tiene_duración" for arco in nodo.arcos)
                tiene_estilo = any(arco.destino.etiqueta.lower() == estilo.lower() and arco.etiqueta == "tiene_estilo" for arco in nodo.arcos)
                if tiene_genero and tiene_duracion and tiene_estilo:
                    recomendaciones.append(nodo.etiqueta)
        return recomendaciones

    def es_pelicula(self, nodo):
        return any(arco.etiqueta == "tiene_género" for arco in nodo.arcos)


def construir_red_semantica():
    red = RedSemantica()


    accion = red.crear_nodo("Acción")
    drama = red.crear_nodo("Drama")
    comedia = red.crear_nodo("Comedia")
    ciencia_ficcion = red.crear_nodo("Ciencia Ficción")
    terror = red.crear_nodo("Terror")
    anime  = red.crear_nodo("Anime")


    corta = red.crear_nodo("Corta")
    larga = red.crear_nodo("Larga")


    rapido = red.crear_nodo("Rápido")
    lento = red.crear_nodo("Lento")
    reflexivo = red.crear_nodo("Reflexivo")
    emotivo = red.crear_nodo("Emotivo")
    suspenso = red.crear_nodo("Suspenso")


    pelicula1 = red.crear_nodo("Mad Max: Fury Road")
    pelicula2 = red.crear_nodo("La La Land")
    pelicula3 = red.crear_nodo("The Hangover")
    pelicula4 = red.crear_nodo("A Quiet Place")
    pelicula5 = red.crear_nodo("Terror Suspenso")
    pelicula6 = red.crear_nodo("The Shawshank Redemption")
    pelicula7 = red.crear_nodo("John Wick")
    pelicula8 = red.crear_nodo("Your name")
    pelicula9 = red.crear_nodo("The Grand Budapest Hotel")
    pelicula10 = red.crear_nodo("Hot Fuzz")


    # Película 1
    red.agregar_arco(pelicula1, accion, "tiene_género")
    red.agregar_arco(pelicula1, corta, "tiene_duración")
    red.agregar_arco(pelicula1, rapido, "tiene_estilo")

    # Película 2
    red.agregar_arco(pelicula2, drama, "tiene_género")
    red.agregar_arco(pelicula2, larga, "tiene_duración")
    red.agregar_arco(pelicula2, emotivo, "tiene_estilo")

    # Película 3
    red.agregar_arco(pelicula3, comedia, "tiene_género")
    red.agregar_arco(pelicula3, corta, "tiene_duración")
    red.agregar_arco(pelicula3, rapido, "tiene_estilo")

    # Película 4
    red.agregar_arco(pelicula4, ciencia_ficcion, "tiene_género")
    red.agregar_arco(pelicula4, larga, "tiene_duración")
    red.agregar_arco(pelicula4, reflexivo, "tiene_estilo")

    # Película 5
    red.agregar_arco(pelicula5, terror, "tiene_género")
    red.agregar_arco(pelicula5, corta, "tiene_duración")
    red.agregar_arco(pelicula5, suspenso, "tiene_estilo")
    
    # Película 6
    red.agregar_arco(pelicula6, drama, "tiene_género")
    red.agregar_arco(pelicula6, larga, "tiene_duración")
    red.agregar_arco(pelicula6, reflexivo, "tiene_estilo")
    
    # Película 7
    red.agregar_arco(pelicula7, accion, "tiene_género")
    red.agregar_arco(pelicula7, corta, "tiene_duración")
    red.agregar_arco(pelicula7, rapido, "tiene_estilo")
    
    # Película 8
    red.agregar_arco(pelicula8, anime, "tiene_género")
    red.agregar_arco(pelicula8, corta, "tiene_duración")
    red.agregar_arco(pelicula8, emotivo, "tiene_estilo")
    
    # Película 9
    red.agregar_arco(pelicula9, comedia, "tiene_género")
    red.agregar_arco(pelicula9, corta, "tiene_duración")
    red.agregar_arco(pelicula9, lento, "tiene_estilo")
    
    # Película 10
    red.agregar_arco(pelicula10, accion, "tiene_género")
    red.agregar_arco(pelicula10, corta, "tiene_duración")
    red.agregar_arco(pelicula10, suspenso, "tiene_estilo")

    return red


def main():
    red = construir_red_semantica()

    print("Bienvenido al sistema de recomendación de películas.")

    genero = input("¿Qué género te interesa? (Acción, Drama, Comedia, Ciencia Ficción, Terror, Anime): ").strip()
    duracion = input("¿Prefieres una película de duración corta o larga? (Corta, Larga): ").strip()
    estilo = input("¿Qué estilo prefieres? (Rápido, Lento, Reflexivo, Emotivo, Suspenso): ").strip()
    print("--Ingresa tus preferencias sin usar tildes, por favor--")

    recomendaciones = red.buscar_recomendacion(genero, duracion, estilo)

    if recomendaciones:
        print("\nTomando en cuenta tus preferencias, se te recomiendan las siguientes películas:")
        for pelicula in recomendaciones:
            print(f"- {pelicula}")
    else:
        print("\nLo siento, no se encontró una recomendación que coincida con tus preferencias.")


if __name__ == "__main__":
    main()
