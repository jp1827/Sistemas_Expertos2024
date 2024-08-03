import os

class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones
        self.conclusion = conclusion

def encadenamiento_hacia_adelante(hechos, reglas):
    conclusiones = set()
    nuevo_hecho_agregado = True
    
    while nuevo_hecho_agregado:
        nuevo_hecho_agregado = False
        
        for regla in reglas:
            if regla.condiciones.issubset(hechos) and regla.conclusion not in hechos:
                hechos.add(regla.conclusion)
                conclusiones.add(regla.conclusion)
                nuevo_hecho_agregado = True
    
    return conclusiones

def Ingresar_hechos():
    hechos = set()
    print("Ingrese los hechos sobre los cientes de bancos:")
    hecho = input("").strip().lower()
    hechos.add(hecho)
    
    print("Desea ingresar otro hecho:")
    print("1 para sí")
    print("2 para no")
    opcion = input("")
    if opcion == "1":
        Ingresar_hechos()
    elif opcion == "2":
        return  hechos
    else:
        print("Ingreso de hechos ha sido finalizada por opción erronea")
        return hechos


def main():
    hechos = Ingresar_hechos()

    reglas = [
        Regla({"cuenta bancaria"}, "Cliente del banco"),
        Regla({"cuenta bancaria", "pago puntual", "leal", "cliente frequente"}, "cliente A"),
        Regla({"cuenta bancaria", "pago puntual", "cliente regular"}, "cliente B"),
        Regla({"cuenta bancaria", "pago puntual", "cliente ocasional"}, "cliente C"),
        Regla({"cuenta bancaria", "moroso", "cliente ocasional"}, "cliente D"),
    ]

    conclusiones = encadenamiento_hacia_adelante(hechos, reglas)

    if not conclusiones:
            print("No se encontraron conclusiones con los hechos ingresados")
    else:
        print("Posibles tipos de clientes:")
        for conclusion in conclusiones:
            print(conclusion)
    
        

if __name__ == "__main__":
    main()

