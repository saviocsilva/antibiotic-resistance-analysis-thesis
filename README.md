# antibiotic-resistance-analysis-thesis
Analysis of Fungal Contamination and Antibiotic Resistance
This repository contains the code and resources for my undergraduate thesis project, focusing on the data-driven analysis of fungal contamination and the prevalence of antibiotic resistance.

1. Project Objective
The primary goal of this project was to analyze a dataset of biological samples to identify key patterns in fungal contamination. The analysis aimed to answer critical questions such as:

What are the most prevalent types of fungi identified?

Is there a correlation between contamination sources and fungal species?

What is the rate of antibiotic multi-resistance, and which species are most resistant?

This analysis provides valuable insights for public health or quality control strategies.

2. Data Sources
The primary dataset used for this analysis is tabela.xlsx, located in the /data folder. This file contains

3. Methodology
The analysis was conducted using Python and several data science libraries. The main steps of the process, detailed in the scripts within the /scripts folder, were:

Data Cleaning and Preprocessing: Loading the dataset and preparing it for analysis.

Exploratory Data Analysis (EDA): Investigating the data to uncover initial patterns and distributions. Scripts like caracteristicas.py and fungos.py were used for this stage.

Resistance Analysis: A specific analysis was performed to quantify single and multi-drug resistance patterns using the resisantibiotico.py script.

Visualization: Generating plots and graphs to visually communicate the findings. The results are stored in the /visualizations folder.

4. Key Findings & Visualizations
The analysis revealed several important findings. [Adicione 2-3 das suas principais conclusões aqui. Ex: "A prevalência de fungos do gênero X foi significativamente maior em amostras de ar."]

Example Visualization: Prevalence of Multi-Resistance
(Dica: Substitua esta imagem por um dos seus gráficos mais importantes. Para fazer isso, suba a imagem para a pasta visualizations e use o link relativo)

A detailed report of all findings can be found in the final thesis document located in the /report folder.

5. Tech Stack
Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn

How to Run
Clone this repository: git clone

Install the required libraries: pip install -r requirements.txt

Run the main analysis script located in the /scripts folder.
