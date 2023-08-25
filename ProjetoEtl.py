#Responsavel por fazer ETL.
import pandas as pd #pip install pandas

from BANCO.comandosSQL import insert_new_cliente, select_id_cliente

#Lendo arquivo excel da aba cliente e 
var_dfCliente = pd.read_excel(f"aquivoETL.xlsx", sheet_name="cliente")
var_listCLiente = var_dfCliente.to_numpy()

for item  in var_listCLiente:
    var_strNomeCliente = item[0]
    var_intStatus = item[1]
    var_intRetorno = select_id_cliente(var_strNomeCliente, var_intStatus)
    if var_intRetorno == 0:
        insert_new_cliente(var_strNomeCliente, var_intStatus)
    else:
        print(f"O cliente: {var_strNomeCliente} já existe no banco de dados")