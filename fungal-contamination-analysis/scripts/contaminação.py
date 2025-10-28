import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 1: Contaminação do Ar
data_ar = {
    "Meio de Cultura": ["Ágar BHI", "Ágar MacConkey", "Ágar Sabouraud"],
    "Crescimento Bacteriano": ["Não Houve", "Não Houve", "Não Houve"],
    "Crescimento Fúngico": ["Não Houve", "Não Houve", "Não Houve"]
}

df_ar = pd.DataFrame(data_ar)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(8, 6))

# Barras para Crescimento Bacteriano
ax.bar(df_ar["Meio de Cultura"], df_ar["Crescimento Bacteriano"].apply(lambda x: 1 if x == "Não Houve" else 0), color='blue', label="Crescimento Bacteriano")

# Barras para Crescimento Fúngico
ax.bar(df_ar["Meio de Cultura"], df_ar["Crescimento Fúngico"].apply(lambda x: 1 if x == "Não Houve" else 0), color='green', label="Crescimento Fúngico")

ax.set_title("Crescimento de Microrganismos por Meio de Cultura (Ar)")
ax.set_xlabel("Meio de Cultura")
ax.set_ylabel("Crescimento (1 = Não Houve, 0 = Houve)")
ax.legend()

plt.tight_layout()
plt.show()