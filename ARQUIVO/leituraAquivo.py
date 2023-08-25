import pandas as pd #pip install pandas

var_dfCliente = pd.read_excel(f"ARQUIVO/aquivoETL.xlsx", sheet_name="cliente")

print(var_dfCliente)


