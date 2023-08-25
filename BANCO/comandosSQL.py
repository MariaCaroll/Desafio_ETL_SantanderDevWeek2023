# Responsável por fazer os comandos necessários do banco local
#Consultas, inserções
from BANCO.conexaoSQL import var_strCursor, var_strConexao



# Funções para inserir dados Cliente
def insert_new_cliente(var_strNome, var_intStatus):
    #status 0 -- cliente pouco ativo
    #status 1 -- cliente muito ativo
    print("Adiconando cliente no banco de dados..")
    var_strComando = f"INSERT INTO tbl_cliente ( nome_cliente,status) VALUES ('{var_strNome}', {var_intStatus})"
    print(var_strComando)
    var_strCursor.execute(var_strComando)
    var_strConexao.commit()

#Função para consultar no banco o se o cliente já existe. 
def select_id_cliente(var_strNome, var_intStatus): 
    var_intRetorno = 0
    var_strComando = f"SELECT id_cliente FROM tbl_cliente WHERE nome_cliente like '{var_strNome}' and status = {var_intStatus}"
    var_strCursor.execute(var_strComando)
    var_strResultado = var_strCursor.fetchall()
    var_strConexao.commit()
    var_intRetorno = len(var_strResultado)     
    return var_intRetorno

