import psycopg2 as p

def main():
    conn = None

    try:
        # conectando o banco de dados
        conexao = "host = 'localhost', database = 'banco_py', user = 'postgres', password = '451000'"
        conn = p.connect(conexao)
        cursor = conn.cursor()
        # criando tabelas
        cursor.execute("CREATE TABLE TB_Usuario(Rg INTEGER PRIMARY KEY, Nome VARCHAR(20), tel INT)")
        cursor.execute("CREATE TABLE TB_Animais(Id INTEGER PRIMARY KEY, Nome VARCHAR(20), ComidaPreferida VARCHAR(20) )")
        # inserindo valores nas tabelas
        cursor.execute("INSERT INTO TB_Usuario VALUES(12345678,'João', 33106000)")
        cursor.execute("INSERT INTO TB_Usuario VALUES(23456789,'Maria', 40028922)")

        cursor.execute("INSERT INTO TB_Animais VALUES(1,'Macaco', 'Banana')")
        cursor.execute("INSERT INTO TB_Animais VALUES(2,'Gato', 'Lasanha')")
        #fazendo consulta
        cursor.execute("SELECT * FROM TB_Usuario")

        for linha in cursor.fetchall():
            print(linha)
        #atualizar dados
        cursor.execute("UPDATE TB_Animais SET Nome = %s WHERE Id = %d", ("garfield o gato", 2))
        #deletando valores da tabela
        cursor.execute("DELETE FROM TB_Usuario WHERE Rg = %d", 23456789)
        cursor.close()
        conn.commit()

    except (Exception, p.DatabaseError) as Erro:
        print(Erro)

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
