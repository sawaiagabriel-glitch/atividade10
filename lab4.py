# code smell
#Long Conditional
#Magic Numbers (2.0, 3.5, 10.0, 8.0, 50.0, 1.0)
#cadeia de if-elif, porque o comportamento muda conforme o tipo de transporte

class CalculadoraDeFrete:
    TARIFAS = {
        "MOTO": {"por_km": 2.0, "taxa_base": 0},
        "CARRO": {"por_km": 3.5, "taxa_base": 10.0},
        "CAMINHAO": {"por_km": 8.0, "taxa_base": 50.0},
        "BICICLETA": {"por_km": 1.0, "taxa_base": 0},
    }

    def calcular_frete(self, tipo_transporte, distancia):
        if tipo_transporte not in self.TARIFAS:
            raise ValueError("Tipo de transporte desconhecido")

        tarifa = self.TARIFAS[tipo_transporte]

        return (
            distancia * tarifa["por_km"]
            + tarifa["taxa_base"]
        )