import sqlite3

def _execute(query, params=None):
    db_path = "./db.mvc"

    # Conectando ao banco de dados
    connection = sqlite3.connect(db_path)

    # Criando um cursor para executar comandos no banco de dados
    cursor = connection.cursor()
    result = None

    try:
        #Executando o comando no banco de dados
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # Commitando as mudanças
        connection.commit()

        # Pegar todos os dados -> Lista de tuplas
        result = cursor.fetchall()
    except Exception as err:
        print(f"Erro ao executar a query: {err}")

    connection.close()
    
    return result

"""
result = [(1, "Playstation 5", 1234, 1), (1, "Playstation 5", 1234, 1)]
"""

