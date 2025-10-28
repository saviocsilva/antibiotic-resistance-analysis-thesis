import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 2: Dados Microbiológicos
data_microbiologia = {
    "Amostra": ["Mesa", "Pia", "Maca"],
    "Coloração de gram": ["Bacilos curtos gram negativo", "Bacilos gram negativo", "Bacilos gram negativo"],
    "Catalase": ["+", "+", "+"],
    "Oxidase": ["-", "-", "-"],
    "TSI": ["-", "+", "-"],
    "SIM": ["-", "-", "-"],
    "Indol": ["-", "-", "-"],
    "Citrato": ["+", "-", "-"],
    "Vermelho de Metila": ["+", "-", "+"],
    "Vogues Proskauer": ["-", "+", "-"],
    "Urease": ["-", "+", "-"]
}

df_microbiologia = pd.DataFrame(data_microbiologia)

# Converter resultados "+"/"-" para 1/0 para plotagem
for col in ["Catalase", "Oxidase", "TSI", "SIM", "Indol", "Citrato", "Vermelho de Metila", "Vogues Proskauer", "Urease"]:
    df_microbiologia[col] = df_microbiologia[col].apply(lambda x: 1 if x == "+" else 0)

# Gráfico de barras para comparar resultados dos testes por amostra
fig, axes = plt.subplots(3, 3, figsize=(15, 15), sharex=True)
testes = ["Catalase", "Oxidase", "TSI", "SIM", "Indol", "Citrato", "Vermelho de Metila", "Vogues Proskauer", "Urease"]

for i, teste in enumerate(testes):
    row = i // 3
    col = i % 3
    axes[row, col].bar(df_microbiologia["Amostra"], df_microbiologia[teste], color='skyblue')
    axes[row, col].set_title(teste)
    axes[row, col].set_ylabel("Resultado (1=Positivo, 0=Negativo)")

plt.tight_layout()
plt.show()