import sqlite3

con = sqlite3.connect('storage.db')
cur = con.cursor()

def Create(nome):
    
    for tab in nome:
        sql = """
                CREATE TABLE IF NOT EXISTS '{}'(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cidade TEXT,
                nupedido INTEGER,
                item TEXT,
                valor INTEGER,
                dia INTEGER,
                mes INTEGER,
                ano INTEGER
                )
            """.format(tab)
        con.execute(sql)

def buscar_tabela():
    sql = """
            SELECT name FROM sqlite_master WHERE type='table'
          """

    cur.execute(sql)
    data = cur.fetchall()

    return data


def busca_spin(v_spin):
    sql = """
            SELECT DISTINCT nome FROM '{}'
          """.format(v_spin)
    cur.execute(sql)
    data = cur.fetchall()
    return data




def buscar_cidade(tab, nome):
    sql = """
        SELECT cidade FROM '{}'
        WHERE nome = '{}'
          """.format(tab, nome)
    cur.execute(sql)
    data = cur.fetchall()
    return data




def inserir(tab, nome, cidade, nupedido, item,valor, dia, mes, ano):
    sql = """
        INSERT INTO '{}'(nome, cidade, nupedido, item, valor, dia, mes, ano)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(tab, nome, cidade, nupedido, item , valor, dia, mes, ano)
    
    con.execute(sql)
    con.commit()

def brief(tab, nome):
    sql = """
            SELECT * FROM '{}'
            WHERE nome = '{}'
            ORDER BY id DESC
          """.format(tab, nome)
    
    cur.execute(sql)
    data = cur.fetchall()

    return data

        
        

