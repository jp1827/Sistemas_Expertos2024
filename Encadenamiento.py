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

def main():
    hechos = {"Cuenta bancaria", "Pago puntual", "Leal", "Moroso", "Cliente frequente", "Cliente regular", "Cliente ocasional"}

    reglas = [
        Regla({"Cuenta bancaria"}, "Cliente"),
        Regla({"Cuenta bancaria", "Pago puntual", "Leal", "Cliente frequente"}, "Cliente A"),
        Regla({"Cuenta bancaria", "Pago puntual", "Cliente regular"}, "Cliente B"),
        Regla({"Cuenta bancaria", "Pago puntual", "Cliente ocasional"}, "Cliente C"),
        Regla({"Cuenta bancaria", "Moroso", "Cliente ocasional"}, "Cliente D"),
    ]

    conclusiones = encadenamiento_hacia_adelante(hechos, reglas)

    print("Posibles tipos de clientes:")
    for conclusion in conclusiones:
        print(conclusion)

if __name__ == "__main__":
    main()

