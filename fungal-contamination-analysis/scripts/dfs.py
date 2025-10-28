import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados das amostras (retirados do "Relatório TCC Vitória.docx")
data = {
    "Amostra": ["Mesa", "Pia", "Maca"],
    "AMC": ["Sensível", "Resistente", "Sensível"],
    "CFE": ["Intermediário", "Resistente", "Intermediário"],
    "GEN": ["Sensível", "Sensível", "Sensível"],
    "TET": ["Sensível", "Resistente", "Sensível"]
}

df = pd.DataFrame(data)

# Mapear os resultados de sensibilidade para valores numéricos
mapping = {"Sensível": 2, "Intermediário": 1, "Resistente": 0}
df_mapped = df.copy()
for col in ["AMC", "CFE", "GEN", "TET"]:
    df_mapped[col] = df_mapped[col].map(mapping)

# Preparar os dados para o gráfico de barras empilhadas
df_stacked = df_mapped.set_index("Amostra").stack().reset_index()
df_stacked.columns = ["Amostra", "Antibiótico", "Resistência"]  # Correção aqui

# Criar o gráfico de barras empilhadas
plt.figure(figsize=(10, 6))

sns.barplot(
    x="Amostra",
    y="Resistência",
    hue="Antibiótico",
    data=df_stacked,
    palette="viridis"
)

plt.title("Perfil de Resistência a Antibióticos por Amostra")
plt.ylabel("Nível de Resistência (0=Resistente, 1=Intermediário, 2=Sensível)")
plt.xlabel("Amostra")
plt.legend(title="Antibiótico")
plt.tight_layout()
plt.show()