def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

def main():
    try:
        consumo_mensal = float(input("Informe o consumo médio mensal de dados em GB: "))
        if consumo_mensal < 0:
            raise ValueError("O consumo médio mensal não pode ser negativo.")
        plano_recomendado = recomendar_plano(consumo_mensal)
        print("O plano recomendado para o consumo médio de", consumo_mensal, "GB é:", plano_recomendado)
    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()