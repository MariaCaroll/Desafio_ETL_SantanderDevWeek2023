#Responsavel por fazer ETL.
import pandas as pd #pip install pandas

from BANCO.comandosSQL import insert_new_cliente, select_all_cliente, insert_new_produto, select_id_produto, select_all_produto, insert_new_alerta
from alerta import generate_new_alerta
var_listAlerta = []
#         --------- PRODUTO ------------EXTRAÇÃO ----------
#Lendo arquivo excel da aba cliente e 
var_dfProduto = pd.read_excel(f"aquivoETL.xlsx", sheet_name="produto")
var_listProduto = var_dfProduto.to_numpy()


#Itera a lista do produto para inserir no banco de dados
#Antes da inserção ele faz uma consulta com base no nome e no valor para não inserir duplicado
for item  in var_listProduto:
    var_strNomeProduto = item[0]
    var_dblValor = item[1]
    var_intPromocao = item[2]
    print(var_dblValor)
    var_intRetorno = select_all_produto(var_strNomeProduto, var_dblValor)
    if var_intRetorno == 0:
        insert_new_produto(var_strNomeProduto, var_dblValor, var_intPromocao)

    else:
        print(f"O cliente: {var_strNomeProduto} já existe no banco de dados")


#         --------- CLEINTE ------------EXTRAÇÃO ------- TRANSFORMAÇÃO
#Lendo arquivo excel da aba cliente e para cada cliente novo gerar um alerta com base no desconto
var_dfCliente = pd.read_excel(f"aquivoETL.xlsx", sheet_name="cliente")
var_listCLiente = var_dfCliente.to_numpy()

#Itera a lista do cliente para inserir no banco de dados
#Antes da inserção ele faz uma consulta com base no nome e no status para não inserir duplicado
for item  in var_listCLiente:
    var_strNomeCliente = item[0]
    var_intStatus = item[1]
    var_strProduto = item[2]
    var_intRetorno = select_all_cliente(var_strNomeCliente, var_intStatus)
    if len(var_intRetorno) == 0:
        var_listProduto = select_id_produto(var_strProduto)
        insert_new_cliente(var_strNomeCliente, var_listProduto[0][0],var_intStatus)
        var_strMensagem = generate_new_alerta(var_strNomeCliente, var_listProduto[0][1])
        print(var_strMensagem)
            
    else:
        print(f"O cliente: {var_strNomeCliente} já existe no banco de dados")