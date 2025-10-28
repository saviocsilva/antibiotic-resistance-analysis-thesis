import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# Dados da tabela (simulando a leitura do Excel)
data = {
    "Agente etiológico": [
        "Gram Positivos", "Staphylococcus aureus", "Staphylococcus sp",
        "Gram Negativos", "Pseudomonas aeruginosa", "Klebsiella pneumoniae",
        "Acinetobacter baumannii", "Escherichia coli", "Providencia suartti", "Outras", "Total"
    ],
    "Identificação": [
        "49 (20,3)", "25 (10,3)", "24 (10)",
        "100 (41,5)", "24 (10)", "21 (8,7)",
        "21 (8,7)", "20 (8,3)", "14 (5,8)", "92 (38,2)", "241 (100)"
    ],
    "Multirresistência": [
        "15 (30,6)", "9 (36)", "6 (25)",
        "41 (41)", "7 (29,1)", "8 (38,1)",
        "10 (47,6)", "6 (30)", "10 (71,4)", "40 (41,7)", "96 (39,8)"
    ]
}

df = pd.DataFrame(data)

# Função robusta para extrair valores (garante que sempre retorna uma tupla)
def extract_values(text):
    if pd.isna(text) or text.strip() == "":
        return (0, 0.0)
    
    text = str(text).strip()
    match = re.match(r"(\d+)\s*\(([\d,]+)\)", text)
    
    if match:
        absolute = int(match.group(1))
        percentage = float(match.group(2).replace(",", "."))
        return (absolute, percentage)
    
    return (0, 0.0)

# Cria as colunas corretamente usando pd.DataFrame
df[["Identificação_N", "Identificação_%"]] = pd.DataFrame(
    df["Identificação"].apply(extract_values).tolist(),
    index=df.index
)

df[["Multirresistência_N", "Multirresistência_%"]] = pd.DataFrame(
    df["Multirresistência"].apply(extract_values).tolist(),
    index=df.index
)

# Remove a linha "Total" (opcional)
df = df[df["Agente etiológico"] != "Total"]

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(df))
largura = 0.35

# Barras
barras_total = ax.bar(x - largura/2, df["Identificação_N"], largura, 
                     color="#3498db", label="Identificação (Total)")
barras_multir = ax.bar(x + largura/2, df["Multirresistência_N"], largura, 
                     color="#e67e22", label="Multirresistência (Total)")

# Personalização
ax.set_xlabel("Agente Etiológico", fontsize=12, weight="bold")
ax.set_ylabel("Número de Isolados", fontsize=12, weight="bold")
ax.set_title(
    "Prevalência de Agentes Etiológicos e Multirresistência\nHES, 2007-2008", 
    fontsize=14, pad=20, weight="bold"
)

# Ajustes do eixo X
ax.set_xticks(x)
ax.set_xticklabels(df["Agente etiológico"], rotation=45, ha="right", fontsize=10)
ax.legend()

# Adiciona porcentagens nas barras
for i, (total, multir) in enumerate(zip(df["Identificação_%"], df["Multirresistência_%"])):
    ax.text(x[i] - largura/2, df["Identificação_N"][i] + 2, f"{total:.1f}%", 
            ha="center", va="bottom", fontsize=9)
    ax.text(x[i] + largura/2, df["Multirresistência_N"][i] + 2, f"{multir:.1f}%", 
            ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig(
    'grafico_multirresistencia.png',  # Nome do arquivo
    dpi=300,                          # Resolução (300 para qualidade alta)
    bbox_inches='tight',              # Remove bordas brancas
    facecolor='white'                 # Fundo branco
)

plt.show()