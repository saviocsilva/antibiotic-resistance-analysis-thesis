import pandas as pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Dados da tabela
data = {
    "Patógeno": [
        "Escherichia coli",
        "Klebsiella pneumoniae",
        "Staphylococcus aureus",
        "Streptococcus pneumoniae",
        "Salmonella spp.",
        "Shigella spp.",
        "Neisseria gonorrhoeae"
    ],
    "Antibiótico de resistência": [
        "Cefalosporinas de terceira geração e fluoroquinolonas",
        "Cefalosporinas de terceira geração e aos carbapenêmicos",
        "Meticilina",
        "Penicilina",
        "Fluoroquinolonas",
        "Fluoroquinolonas",
        "Susceptibilidade reduzida a cefalosporinas de terceira geração"
    ]
}

# Criando o DataFrame
df = pd.DataFrame(data)



# Texto com os dados para a Word Cloud
text = ("Escherichia coli Klebsiella pneumoniae Staphylococcus aureus "
        "Streptococcus pneumoniae Salmonella spp. Shigella spp. "
        "Neisseria gonorrhoeae "
        "Cefalosporinas fluoroquinolonas carbapenêmicos meticilina "
        "penicilina susceptibilidade reduzida")

# Gerando a Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(text)

# Exibindo a Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Microrganismos e Antibióticos (Frequência)", fontsize=16)
plt.show()

