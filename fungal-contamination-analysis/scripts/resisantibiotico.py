import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DataFrame 3: Dados de Resistência a Antibióticos
data_antibiograma = {
    "Amostra": ["Mesa", "Pia", "Maca"],
    "AMC": ["Sensível", "Resistente", "Sensível"],
    "CFE": ["Intermediário", "Resistente", "Intermediário"],
    "GEN": ["Sensível", "Sensível", "Sensível"],
    "TET": ["Sensível", "Resistente", "Sensível"]
}

df_antibiograma = pd.DataFrame(data_antibiograma)

# Converter resistência para valores numéricos para ordenação correta
resistencia_mapping = {"Resistente": 0, "Intermediário": 1, "Sensível": 2}
df_antibiograma_mapped = df_antibiograma.copy()
for col in ["AMC", "CFE", "GEN", "TET"]:
    df_antibiograma_mapped[col] = df_antibiograma_mapped[col].map(resistencia_mapping)

# Preparar os dados para o gráfico de barras agrupado
df_antibiograma_melted = df_antibiograma_mapped.melt(id_vars="Amostra", value_vars=["AMC", "CFE", "GEN", "TET"], var_name="Antibiótico", value_name="Resistência")

# Gráfico de barras agrupado
plt.figure(figsize=(12, 8))
sns.barplot(x="Amostra", y="Resistência", hue="Antibiótico", data=df_antibiograma_melted, palette="viridis")
plt.title("Perfil de Resistência a Antibióticos por Amostra")
plt.ylabel("Nível de Resistência (0=Resistente, 1=Intermediário, 2=Sensível)")
plt.xlabel("Amostra")
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.tight_layout()
plt.show()