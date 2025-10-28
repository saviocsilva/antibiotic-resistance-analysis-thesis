import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Dados organizados em um dicionário
data = {
    "Variável": [
        "Sexo Masculino", "Sexo Feminino",
        "Idade 15 a 40", "Idade 41 a 65", "Idade > 65",
        "Procedência Pronto Atendimento", "Procedência Outros setores do Hospital",
        "Procedência Comunidade", "Procedência Outros Hospitais", "Procedência Ignorado",
        "Permanência prévia ao CTI <1 dia", "Permanência prévia ao CTI 1 a 3 dias",
        "Permanência prévia ao CTI 4 a 30 dias", "Permanência prévia ao CTI >30 dias", "Permanência prévia ao CTI Ignorado",
        "Permanência no CTI 1 a 5 dias", "Permanência no CTI 6 a 30 dias", "Permanência no CTI >30 dias", "Permanência no CTI Ignorado",
        "Classificação de gravidade Sem classificação", "Classificação de gravidade A", "Classificação de gravidade B",
        "Classificação de gravidade C", "Classificação de gravidade D", "Classificação de gravidade E",
        "Doença Cardiovascular", "Doença Gastrintestinal", "Doença Neoplasias", "Doença Respiratório", "Doença Osteomuscular",
        "Doença Geniturinário", "Doença Endócrinas", "Doença Outras", "Doença Sem classificação"
    ],
    "n": [
        137, 145, 74, 135, 73, 14, 50, 6, 0, 212, 
        25, 36, 43, 4, 174, 11, 75, 22, 174, 
        1, 3, 2, 79, 191, 6, 79, 62, 49, 13, 
        11, 10, 9, 33, 16
    ],
    "%": [
        48.6, 51.4, 26.2, 47.9, 25.9, 5, 17.7, 2.1, 0, 75.2, 
        8.9, 12.8, 15.2, 1.4, 61.7, 3.9, 26.5, 7.9, 61.7, 
        0.3, 1, 0.7, 28.2, 67.8, 2, 28.1, 21.9, 17.4, 4.6, 
        3.9, 3.5, 3.2, 11.3, 5.7
    ]
}

# Criando o DataFrame
df = pd.DataFrame(data)


# Dados para o gráfico
import matplotlib.pyplot as plt
import numpy as np

# Dados corrigidos
import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo para o gráfico
variaveis = [
    "Sexo", "Idade", "Procedência",
    "Permanência Prévia ao CTI", "Permanência no CTI",
    "Gravidade", "Doença Base"
]

# Dados organizados
dados = [
    [48.6, 51.4],             # Masculino e Feminino
    [26.2, 47.9, 25.9],       # Faixas etárias
    [5, 17.7, 2.1, 75.2],     # Procedência
    [8.9, 12.8, 15.2, 61.7],  # Permanência Prévia ao CTI
    [3.9, 26.5, 7.9, 61.7],   # Permanência no CTI
    [0.3, 1, 0.7, 28.2, 67.8, 2],  # Gravidade
    [28.1, 21.9, 17.4, 11.3, 5.7]  # Doença Base
]

# Nomes descritivos dos grupos
legendas = [
    "Masculino", "Feminino",
    "15 a 40 anos", "41 a 65 anos", "Acima de 65 anos",
    "Pronto Atendimento", "Outros Setores", "Comunidade", "Ignorado",
    "Menos de 1 dia", "1 a 3 dias", "4 a 30 dias", "Ignorado",
    "1 a 5 dias", "6 a 30 dias", "Mais de 30 dias", "Ignorado",
    "Sem Classificação", "Classificação A", "Classificação B",
    "Classificação C", "Classificação D", "Classificação E",
    "Cardiovascular", "Gastrintestinal", "Neoplasias",
    "Respiratório", "Outras Doenças"
]

# Configurações do gráfico
fig, ax = plt.subplots(figsize=(12, 7))
x = np.arange(len(variaveis))  # Posições no eixo X
largura_barra = 0.6  # Largura das barras
bottom = np.zeros(len(variaveis))  # Base inicial para empilhamento

# Cores para diferenciar os grupos
colors = plt.cm.tab10(np.linspace(0, 1, len(dados)))

# Gerando as barras empilhadas
for i, valores in enumerate(dados):
    valores = np.pad(valores, (0, len(variaveis) - len(valores)), constant_values=0)
    ax.bar(x, valores, width=largura_barra, bottom=bottom, label=legendas[i], color=colors[i])
    bottom += valores

# Personalizando o gráfico
ax.set_title("Distribuição Percentual de Internações por Variáveis Hospitalares", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(variaveis, rotation=45, ha="right")
ax.set_ylabel("Percentual (%)")
ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

# Ajustando o layout
plt.tight_layout()
plt.show()