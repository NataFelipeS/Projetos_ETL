import pandas as pd

caminho_csv = r"C:\\Users\\T-Gamer\Documents\\GitHub\\Projetos_ETL\\Pipeline1\dados_originais.csv"

caminho_excel = r"C:\\Users\\T-Gamer\Documents\\GitHub\\Projetos_ETL\\Pipeline1\\exemplo.xlsx"

df = pd.read_csv(caminho_csv, sep= ",")
print(df)

df.to_excel(caminho_excel, index=False)
