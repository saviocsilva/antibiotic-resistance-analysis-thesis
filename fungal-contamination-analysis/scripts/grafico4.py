import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


# Dados da tabela
data = {
    "Ação": [
        "Síntese de enzimas",
        "Diminuição da absorção de moléculas exógenas",
        "Bombas de efluxo",
        "Alteração na conformação do local de ação",
        "Aquisição de material genético"
    ],
    "Mecanismo": [
        "Enzimas β-lactamases, inativam fármacos, tornando-os incapazes de interagir com seus receptores alvo.",
        "Limitação de afluxo de substâncias hidrofílicas, como tetraciclinas, porinas e fluoroquinolonas.",
        "Ejeção de substâncias para o meio extracelular, assegurando a proteção do material genético.",
        "Alteração no sítio de ligação do antibiótico, reduzindo sua afinidade ou impedindo interação.",
        "Transferência de genes via conjugação, plasmídeos ou transposons, difundindo resistência antimicrobiana."
    ],
    "Fonte": [
        "Oliveira, 2014",
        "Oliveira, 2014",
        "Lopes, 2009",
        "Lin et al., 2015",
        "Lin et al., 2015"
    ]
}

# Criando o DataFrame
df = pd.DataFrame(data)


# Dados fictícios para o exemplo
acoes = ["Síntese de enzimas", "Diminuição de absorção", "Bombas de efluxo", "Alteração conformacional", "Aquisição de genes"]
valores = [20, 15, 30, 25, 10]
mecanismos = ["Enzimas β-lactamases", "Absorção limitada", "Efluxo ativo", "Mudança do alvo", "Transferência genética"]

# Configurando o gráfico de barras
x = np.arange(len(acoes))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, valores, width, label='Mecanismos')

# Configuração de labels e título
ax.set_xlabel('Ações')
ax.set_ylabel('Frequência')
ax.set_title('Distribuição de Mecanismos de Resistência e Ações')
ax.set_xticks(x)
ax.set_xticklabels(acoes, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
