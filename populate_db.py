import sqlite3
import os

DB_FILE = 'db.sqlite3'
SQL_SCRIPT = 'sgea_script_expandido.sql'

def populate_database():
    """Conecta ao SQLite e executa o script SQL para inserir dados."""
    
    if not os.path.exists(SQL_SCRIPT):
        print(f"ERRO: Arquivo {SQL_SCRIPT} não encontrado. Certifique-se de que está na raiz do projeto.")
        return

    print(f"Conectando ao banco de dados: {DB_FILE}")
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        with open(SQL_SCRIPT, 'r', encoding='utf-8') as f:
            sql_commands = f.read()
        
        # Executa todos os comandos de uma vez
        cursor.executescript(sql_commands)
        
        # Comita as mudanças no banco
        conn.commit()
        print("Sucesso! O banco de dados foi populado com os dados de teste expandidos.")
        
    except sqlite3.OperationalError as e:
        print(f"\n--- ERRO AO EXECUTAR O SCRIPT ---")
        print(f"Ocorreu um erro SQL. Isso pode ser devido a dados já existentes (tente deletar o db.sqlite3 e rodar migrate novamente).")
        print(f"Detalhe do erro: {e}")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    populate_database()