import sqlite3



#criar database
conn = sqlite3.connect("dados_treinamento.db")
#criar cursor da database
c = conn.cursor()
#criar tabelas
c.execute("""CREATE TABLE pessoas (
        nome TEXT,
        sobrenome TEXT,
        sala_etapa_1 TEXT,
        intervalo_cafe TEXT,
        sala_etapa_2 TEXT
        )""")

c.execute("""CREATE TABLE salas (
        sala TEXT,
        capacidade INT,
        participantes TEXT
        )""")

c.execute("""CREATE TABLE esp_cafe (
        nome_cafe TEXT,
        capacidade INT,
        participantes TEXT
        )""")


#commit na db
conn.commit()
#fechar conexao
conn.close()