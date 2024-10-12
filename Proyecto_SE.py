import pyodbc
import tkinter as tk
from tkinter import messagebox, ttk

class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones
        self.conclusion = conclusion

def obtener_reglas_conclusiones(cursor):
    cursor.execute('''
        SELECT R.ingreso_mensual_minimo, R.valor_propiedad_minimo, R.monto_maximo_solicitado,
               R.cantidad_maxima_deudas, R.costo_maximo_curso, R.valor_activos_negocio_minimo,
               R.costo_maximo_reformas, R.costo_maximo_viaje, C.descripcion_prestamo
        FROM Reglas R
        JOIN Reglas_Conclusiones RC ON R.id_regla = RC.id_regla
        JOIN conclusiones C ON RC.id_conclusion = C.id_conclusion
    ''')
    
    reglas = []
    for row in cursor.fetchall():
        condiciones = {}
        if row.ingreso_mensual_minimo is not None:
            condiciones['ingreso_mensual'] = ('minimo', row.ingreso_mensual_minimo)
        if row.valor_propiedad_minimo is not None:
            condiciones['valor_propiedad'] = ('minimo', row.valor_propiedad_minimo)
        if row.monto_maximo_solicitado is not None:
            condiciones['monto_solicitado'] = ('maximo', row.monto_maximo_solicitado)
        if row.cantidad_maxima_deudas is not None:
            condiciones['cantidad_deudas'] = ('maximo', row.cantidad_maxima_deudas)
        if row.costo_maximo_curso is not None:
            condiciones['costo_curso'] = ('maximo', row.costo_maximo_curso)
        if row.valor_activos_negocio_minimo is not None:
            condiciones['valor_activos_negocio'] = ('maximo', row.valor_activos_negocio_minimo)
        conclusion = row.descripcion_prestamo
        reglas.append(Regla(condiciones, conclusion))
    return reglas

def encadenamiento_hacia_adelante(hechos, reglas):
    conclusiones = set()

    for regla in reglas:
        condiciones_cumplidas = True

        for campo, (tipo_condicion, valor_condicion) in regla.condiciones.items():
            hecho_valor = hechos.get(campo)

            # Comprobar que el campo requerido no es None o cero
            if hecho_valor is None or hecho_valor == 0:
                condiciones_cumplidas = False
                print(f"Condición no cumplida: {campo} no tiene un valor proporcionado o es cero.")
                break

            # Evaluar la condición según el tipo
            if tipo_condicion == 'minimo':
                if hecho_valor < valor_condicion:
                    condiciones_cumplidas = False
                    print(f"Condición no cumplida: {campo} requiere al menos {valor_condicion}, pero el hecho es {hecho_valor}")
                    break
            elif tipo_condicion == 'maximo':
                if hecho_valor > valor_condicion:
                    condiciones_cumplidas = False
                    print(f"Condición no cumplida: {campo} requiere como máximo {valor_condicion}, pero el hecho es {hecho_valor}")
                    break

        if condiciones_cumplidas:
            print(f"Regla cumplida para {regla.conclusion}")
            conclusiones.add(regla.conclusion)
        else:
            print(f"No se cumplió la regla para {regla.conclusion}")

    return conclusiones


def enviar_datos():
    try:
        hechos = {
            'ingreso_mensual': float(ingreso_mensual_entry.get() or 0),
            'valor_propiedad': float(valor_propiedad_entry.get() or 0),
            'monto_solicitado': float(monto_solicitado_entry.get() or 0),
            'cantidad_deudas': float(cantidad_deudas_entry.get() or 0),
            'costo_curso': float(costo_curso_entry.get() or 0),
            'valor_activos_negocio': float(valor_activos_negocio_entry.get() or 0),
            'costo_reformas': float(costo_reformas_entry.get() or 0),
            'costo_viaje': float(costo_viaje_entry.get() or 0)
        }
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        return

    conclusiones = encadenamiento_hacia_adelante(hechos, reglas)

    if not conclusiones:
        messagebox.showinfo("Resultados", "No se encontraron conclusiones con los hechos ingresados")
    else:
        resultado = "\n".join(conclusiones)
        messagebox.showinfo("Resultados", f"Conclusiones posibles:\n{resultado}")

def habilitar_campos(event):
    tipo_prestamo = tipo_prestamo_combobox.get()
    
    # Habilitar o deshabilitar campos según el tipo de préstamo
    for entry in [monto_solicitado_entry, valor_propiedad_entry, ingreso_mensual_entry,
                  cantidad_deudas_entry, costo_curso_entry, valor_activos_negocio_entry,
                  costo_reformas_entry, costo_viaje_entry]:
        entry.config(state='disabled')

    if tipo_prestamo in ["Hipotecario", "Personal", "Auto"]:
        ingreso_mensual_entry.config(state='normal')
        if tipo_prestamo == "Hipotecario":
            valor_propiedad_entry.config(state='normal')
        else:
            monto_solicitado_entry.config(state='normal')

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Sistema Experto de Préstamos")
root.geometry("400x500")

tk.Label(root, text="Seleccione el Tipo de Préstamo:").grid(row=0, column=0, padx=10, pady=10)
tipo_prestamo_combobox = ttk.Combobox(root, values=["Hipotecario", "Personal", "Auto", "Estudiantil", "Consolidación de Deudas", "Reformas de Hogar", "Negocio", "Emergencia", "Vacaciones"])
tipo_prestamo_combobox.grid(row=0, column=1, padx=10, pady=10)
tipo_prestamo_combobox.bind("<<ComboboxSelected>>", habilitar_campos)

tk.Label(root, text="Ingreso Mensual:").grid(row=1, column=0)
ingreso_mensual_entry = tk.Entry(root)
ingreso_mensual_entry.grid(row=1, column=1)

tk.Label(root, text="Valor Propiedad:").grid(row=2, column=0)
valor_propiedad_entry = tk.Entry(root)
valor_propiedad_entry.grid(row=2, column=1)

tk.Label(root, text="Monto Solicitado:").grid(row=3, column=0)
monto_solicitado_entry = tk.Entry(root)
monto_solicitado_entry.grid(row=3, column=1)

tk.Label(root, text="Cantidad Deudas:").grid(row=4, column=0)
cantidad_deudas_entry = tk.Entry(root)
cantidad_deudas_entry.grid(row=4, column=1)

tk.Label(root, text="Costo Curso:").grid(row=5, column=0)
costo_curso_entry = tk.Entry(root)
costo_curso_entry.grid(row=5, column=1)

tk.Label(root, text="Valor Activos Negocio:").grid(row=6, column=0)
valor_activos_negocio_entry = tk.Entry(root)
valor_activos_negocio_entry.grid(row=6, column=1)

tk.Label(root, text="Costo Reformas:").grid(row=7, column=0)
costo_reformas_entry = tk.Entry(root)
costo_reformas_entry.grid(row=7, column=1)

tk.Label(root, text="Costo Viaje:").grid(row=8, column=0)
costo_viaje_entry = tk.Entry(root)
costo_viaje_entry.grid(row=8, column=1)

enviar_button = tk.Button(root, text="Evaluar", command=enviar_datos)
enviar_button.grid(row=9, column=0, columnspan=2, pady=10)

# Conexión a la base de datos y obtención de reglas y conclusiones
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=JOSEM\SQL2022;DATABASE=sistemaExperto;UID=sa;PWD=Gotrade18')
    cursor = conn.cursor()
    reglas = obtener_reglas_conclusiones(cursor)
except pyodbc.Error as e:
    messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
    root.quit()

root.mainloop()
