# Responsável por realizar a conexão com o sqlite
import sqlite3

try:
    print("Realizando conexão com banco de dados...")
    var_strConexao = sqlite3.connect(f"BANCO/SDW2023.db")
    var_strCursor = var_strConexao.cursor()
    print("Conexão realizada com sucesso.")
except:
    print("Erro ao conectar com o banco local.")
