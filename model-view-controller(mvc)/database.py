import sqlite3

def _execute(query):
    db_path = "./db.mvc"

    # Conectando ao banco de dados
    connection = sqlite3.connect(db_path)

    # Criando um cursor para executar comandos no banco de dados
    cursor = connection.cursor()
    result = None

    try:
        # Executando o comando no banco de dados
        cursor.execute(query)

        # Pegar todos os dados -> Lista de tuplas
        result = cursor.fetchall()

        # Commitando as mudanças
        connection.commit()
    except Exception as err:
        print(f"Erro ao executar a query: {err}")
    
    return result

"""
result = [(1, "Playstation 5", 1234, 1), (1, "Playstation 5", 1234, 1)]
"""

