class RedBayesianaPrestamos:
    def __init__(self):
        self.probabilidad_incumplimiento = {
            "Cumple": 0.85,
            "Incumple": 0.15
        }

        self.prob_historial_dado_incumplimiento = {
            "Historial": {"Bueno": {"Cumple": 0.7, "Incumple": 0.2}, "Malo": {"Cumple": 0.3, "Incumple": 0.8}},
            "Ingresos": {"Alto": {"Cumple": 0.6, "Incumple": 0.2}, "Medio": {"Cumple": 0.3, "Incumple": 0.4}, "Bajo": {"Cumple": 0.1, "Incumple": 0.4}},
            "Deuda": {"Alta": {"Cumple": 0.2, "Incumple": 0.7}, "Baja": {"Cumple": 0.8, "Incumple": 0.3}}
        }

    def inferir_probabilidad_incumplimiento(self, historial, ingresos, deuda):
        prob_cumple = self.probabilidad_incumplimiento["Cumple"]
        prob_incumple = self.probabilidad_incumplimiento["Incumple"]

        prob_historial_cumple = self.prob_historial_dado_incumplimiento["Historial"][historial]["Cumple"]
        prob_historial_incumple = self.prob_historial_dado_incumplimiento["Historial"][historial]["Incumple"]

        prob_ingresos_cumple = self.prob_historial_dado_incumplimiento["Ingresos"][ingresos]["Cumple"]
        prob_ingresos_incumple = self.prob_historial_dado_incumplimiento["Ingresos"][ingresos]["Incumple"]

        prob_deuda_cumple = self.prob_historial_dado_incumplimiento["Deuda"][deuda]["Cumple"]
        prob_deuda_incumple = self.prob_historial_dado_incumplimiento["Deuda"][deuda]["Incumple"]


        unir_prob_cumple = prob_cumple * prob_historial_cumple * prob_ingresos_cumple * prob_deuda_cumple
        unir_prob_incumple = prob_incumple * prob_historial_incumple * prob_ingresos_incumple * prob_deuda_incumple

        total_prob = unir_prob_cumple + unir_prob_incumple
        unir_prob_cumple /= total_prob
        unir_prob_incumple /= total_prob

        return unir_prob_cumple, unir_prob_incumple

    def diagnostico(self, historial, ingresos, deuda):
        prob_cumple, prob_incumple = self.inferir_probabilidad_incumplimiento(historial, ingresos, deuda)

        print(f"Probabilidad de que el cliente cumpla con el préstamo: {prob_cumple * 100:.2f}%")
        print(f"Probabilidad de que el cliente incumpla con el préstamo: {prob_incumple * 100:.2f}%")


if __name__ == "__main__":
    red = RedBayesianaPrestamos()

    historial = "Bueno"  
    ingresos = "Medio"
    deuda = "Alta" 

    print("Evaluación de riesgo de préstamo basada en características del cliente:")
    red.diagnostico(historial, ingresos, deuda)
