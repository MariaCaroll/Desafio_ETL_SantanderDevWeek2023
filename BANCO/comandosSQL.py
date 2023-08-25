# Responsável por fazer os comandos necessários do banco local
#Consultas, inserções
from BANCO.conexaoSQL import var_strCursor, var_strConexao

# Funções para inserir dados Cliente
def insert_new_cliente(var_strNome, var_intIdProduto, var_intStatus):
    # status 0 -- cliente pouco ativo
    # status 1 -- cliente muito ativo
    print("Adiconando cliente no banco de dados..")
    var_strComando = f"INSERT INTO tbl_cliente ( nome_cliente,status) VALUES ('{var_strNome}', {var_intIdProduto}, {var_intStatus})"
    print(var_strComando)
    var_strCursor.execute(var_strComando)
    var_strConexao.commit()

# Função para consultar no banco o se o cliente já existe.
def select_all_cliente(var_strNome, var_intStatus):
    var_intRetorno = 0
    var_strComando = f"SELECT id_cliente FROM tbl_cliente WHERE nome_cliente like '{var_strNome}' and status = {var_intStatus}"
    var_strCursor.execute(var_strComando)
    var_strResultado = var_strCursor.fetchall()
    var_strConexao.commit()
    var_intRetorno = len(var_strResultado)
    return var_intRetorno

# Funções para inserir dados produto
def insert_new_produto(var_strNome, var_dblValor, var_intPromocao):

    print("Adiconando produto no banco de dados..")
    var_strComando = f"INSERT INTO tbl_produto ( nome_produto,valor, promocao) VALUES ('{var_strNome}', {var_dblValor}, {var_intPromocao})"
    print(var_strComando)
    var_strCursor.execute(var_strComando)
    var_strConexao.commit()

# Função para consultar no banco o se o produto já existe.
def select_id_produto(var_strNome):
    var_intRetorno = 0
    var_strComando = f"SELECT id_produto, promocao FROM tbl_produto WHERE nome_produto like '{var_strNome}'"
    var_strCursor.execute(var_strComando)
    var_strResultado = var_strCursor.fetchall()
    var_strConexao.commit()
    var_intRetorno = var_strResultado
    return var_intRetorno


# Função para consultar no banco o se o produto já existe.
def select_all_produto(var_strNome, var_dblValor):
    var_intRetorno = 0
    var_strComando = f"SELECT id_produto FROM tbl_produto WHERE nome_produto like '{var_strNome}' and valor = {var_dblValor}"
    var_strCursor.execute(var_strComando)
    var_strResultado = var_strCursor.fetchall()
    var_strConexao.commit()
    var_intRetorno = len(var_strResultado)
    return var_intRetorno


# Funções para inserir dados ALERTAS
def insert_new_alerta(var_intIdCliente, var_intIdProduto, var_strTipoAlerta, var_strMensagem):

    print("Adiconando ALETA no banco de dados..")
    var_strComando = f'''INSERT INTO tbl_alerta ( id_cliente,id_produto, tipo_alerta, mensagem) 
                            VALUES ({var_intIdCliente}, {var_intIdProduto}, '{var_strTipoAlerta}', '{var_strMensagem}')'''
    print(var_strComando)
    var_strCursor.execute(var_strComando)
    var_strConexao.commit()
