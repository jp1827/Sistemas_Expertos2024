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

    def mostrar_red(self):
        for nodo in self.nodos:
            for arco in nodo.arcos:
                print(arco)


def main():
    red = RedSemantica()

    #Creación de nodos para "Animal"
    animal = red.crear_nodo("Animal")
    vida = red.crear_nodo("Vida")
    sentir = red.crear_nodo("Sentir")
    moverse = red.crear_nodo("Moverse")
    
    #Creación de nodos para "Mamifero"
    mamifero = red.crear_nodo("Mamifero")
    leche = red.crear_nodo("Leche")
    pelo = red.crear_nodo("Pelo")
    tigre = red.crear_nodo("Tigre")
    ballena = red.crear_nodo("Ballena")
    carne = red.crear_nodo("Carne")
    mar = red.crear_nodo("Mar")
    piel = red.crear_nodo("Piel")
    
    #Creación de nodos para "Ave"
    ave = red.crear_nodo("Ave")
    bien = red.crear_nodo("Bien")
    plumas = red.crear_nodo("Plumas")
    huevos = red.crear_nodo("Huevos")
    avestruz = red.crear_nodo("Avestruz")
    albatros = red.crear_nodo("Albatros")
    largas = red.crear_nodo("Largas")
    no_puede = red.crear_nodo("No_puede")
    muy_bien = red.crear_nodo("Vuela")
    
    #Creación de arcos para "Animal"
    animal.agregar_arco(vida, "tiene")
    animal.agregar_arco(sentir, "puede")
    animal.agregar_arco(moverse, "puede")
    
    #Creación de arcos para "Mamifero"
    mamifero.agregar_arco(animal, "tipo_de")
    mamifero.agregar_arco(leche, "da")
    mamifero.agregar_arco(pelo, "tiene")
    tigre.agregar_arco(animal, "tipo_de")
    tigre.agregar_arco(carne, "come")
    ballena.agregar_arco(animal, "tipo_de")
    ballena.agregar_arco(mar, "vive_en")
    ballena.agregar_arco(piel, "tiene")
    
    #Creación de arcos para "Ave"
    ave.agregar_arco(animal, "tipo_de")
    ave.agregar_arco(bien, "vuela")
    ave.agregar_arco(plumas, "tiene")
    ave.agregar_arco(huevos, "pone")
    avestruz.agregar_arco(ave, "tipo_de")
    avestruz.agregar_arco(largas, "patas")
    avestruz.agregar_arco(no_puede, "vuela")
    albatros.agregar_arco(ave, "tipo_de")
    albatros.agregar_arco(muy_bien, "vuela")
    


    red.mostrar_red()


if __name__ == "__main__":
    main()
