import pandas as pd
import matplotlib.pyplot as plt
import textwrap

# DataFrame 4: Análise Fúngica (o mesmo de antes)
data_fungos = {
    "Amostra": ["Maca", "Chão", "Pia"],
    "Crescimento Fúngico": ["Houve", "Houve", "Houve"],
    "Características Macroscópicas": [
        "Colônia de cor branco leitoso com as bordas marrons, aspecto rugoso e com sulcos, forma circular, convexo e borda lisa, com cerca de 5cm de tamanho.",
        "Colônia de cor branco leitoso com as bordas marrom, aspecto aveludado, forma circular, convexo e borda irregular, com cerca de 1cm de tamanho.",
        "2 colônias de cor marrom com as bordas brancas, aspecto rugoso e com sulcos, de formato oval, convexo e com bordas irregulares, com cerca de 3cm de tamanho cada uma. E também, presença de 1 colônia de cor branco leitoso e borda marrom, com aspecto aveludado, de formato oval, convexo e bordas irregulares com cerca de 1cm."
    ],
    "Características Microscópicas": [
        "Presença de fungos filamentosos, denominados bolores, multicelulares, de forma fusiforme, com presença de células tubulares denominadas hifas, septada e micélio, pigmentados no azul de metileno e agrupados.",
        "Presença de fungos filamentosos, denominados bolores, multicelulares, de forma fusiforme, com presença de células tubulares denominadas hifas, não septada, com presença de micélio, pigmentados no azul de metileno e isolados.",
        "Presença de fungos ovais, denominados leveduras, unicelulares, pigmentados no azul de metileno e agrupados."
    ]
}

df_fungos = pd.DataFrame(data_fungos)

def create_text_table(ax, data):
    y_pos = 0.9
    line_height = 0.15
    text_kwargs = {'fontsize': 10, 'ha': 'left', 'va': 'top'}
    bold_kwargs = {'fontsize': 10, 'ha': 'left', 'va': 'top', 'fontweight': 'bold'}
    wrap_width = 70  # Ajuste conforme necessário

    ax.text(0.1, y_pos, "Atributo", **bold_kwargs, bbox={'facecolor': 'lightgrey', 'pad': 5})
    ax.text(0.4, y_pos, "Descrição", **bold_kwargs, bbox={'facecolor': 'lightgrey', 'pad': 5})
    y_pos -= line_height

    ax.text(0.1, y_pos, "Amostra:", **bold_kwargs)
    ax.text(0.4, y_pos, data['Amostra'], **text_kwargs)
    y_pos -= line_height

    ax.text(0.1, y_pos, "Crescimento:", **bold_kwargs)
    ax.text(0.4, y_pos, data['Crescimento Fúngico'], **text_kwargs)
    y_pos -= line_height

    ax.text(0.1, y_pos, "Macroscópicas:", **bold_kwargs)
    macro_lines = textwrap.wrap(data['Características Macroscópicas'], width=wrap_width)
    for line in macro_lines:
        ax.text(0.4, y_pos, line, **text_kwargs)
        y_pos -= 0.1  # Ajuste a altura da linha conforme necessário

    y_pos -= 0.05  # Espaço entre seções

    ax.text(0.1, y_pos, "Microscópicas:", **bold_kwargs)
    micro_lines = textwrap.wrap(data['Características Microscópicas'], width=wrap_width)
    for line in micro_lines:
        ax.text(0.4, y_pos, line, **text_kwargs)
        y_pos -= 0.1  # Ajuste a altura da linha conforme necessário

    ax.axis('off')
    return y_pos # Retorna a posição y final para ajustar a altura do subplot

fig, axes = plt.subplots(3, 1, figsize=(10, 15))
plt.subplots_adjust(hspace=0.5)

for i, ax in enumerate(axes):
    final_y = create_text_table(ax, df_fungos.iloc[i])
    # Ajustar os limites y do subplot se necessário
    ax.set_ylim(final_y - 0.1, 1)

plt.suptitle("Análise Detalhada de Fungos", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()