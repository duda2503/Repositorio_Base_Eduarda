import sqlite3

banco = sqlite3.connect('biblioteca.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS ALUNOS(nome TEXT, turma INTEGER, idade INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS AUTORES(nome TEXT, livro_famoso TEXT, ano_do_livro INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS LIVROS(nome TEXT, ano_do_livro INTEGER, genero INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS EMPRÉSTIMOS(nome_cliente TEXT,data_emprestada DATE, data_devolução DATE)")

#cursor.execute("INSERT INTO ALUNOS VALUES ('Lorrani' , 1,15)")
cursor.execute("SELECT * FROM ALUNOS WHERE idade = 16")
print(cursor.fetchall())
#cursor.execute("INSERT INTO ALUNOS VALUES ('Lorrani' , 1,16)")
#cursor.execute("UPDATE ALUNOS SET nome = 'Bia' WHERE NOME = 'lorrani' ")
#cursor.execute("DELETE FROM ALUNOS where nome = 'Lorrani' ")

banco.commit()