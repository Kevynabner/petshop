from conexao import conectar

#CREATE 
#CADASTRAR PET
def cadastrar_cliente():
    conexao = conectar()
    nome_cliente = input("Digite o seu nome: ").lower()
    cpf_cliente = int(input("Digite o seu CPF: "))
    telefone = int(input("Digite o seu TELEFONE: "))
    email = (input("Digite o seu E-MAIL: "))
    endereco = input("Digite o seu ENDEREÇO: ") 
    
    ##validação de CPF
    cursor = conexao.cursor()
    comando = f'SELECT cpf FROM clientes WHERE cpf = "{cpf_cliente}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()
    if resultado:
       print("ERRO: CPF JÁ CADASTRADO.")
       cursor.close()
       return
       
    cursor = conexao.cursor()
    comando = f'INSERT INTO clientes (cpf, nome, telefone, email, endereco) VALUES ("{cpf_cliente}","{nome_cliente}", "{telefone}", "{email}", "{endereco}")'
    cursor.execute(comando)
    conexao.commit()

    print(f'CLIENTE {nome_cliente} CADASTRADO COM SUCESSO')

    cursor.close()
    conexao.close()

def listar_clientes():

    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM clientes'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("________CLIENTES CADASTRADOS________\n")
    for i in resultado:
        print(f'NOME = {i[1]}')
        print(f'CPF = {i[2]}')
        print("______________________\n")
    print(f'TOTAL DE USUÁRIOS CADASTRADOS = {len(resultado)}')
    cursor.close()
    conexao.close()    

def deletar_cliente():
    conexao = conectar()
    cpf_clientes = int(input("Digite o CPF do cliente: "))
    cursor = conexao.cursor()
    comando = f'DELETE FROM clientes WHERE cpf = "{cpf_clientes}"'

    cursor.execute(comando)
    conexao.commit()

    print("CLIENTE DELETADO COM SUCESSO")

    cursor.close()
    conexao.close()
        
def atualizar_endereco():
    conexao = conectar()
    cpf_cliente = input("Digite o CPF : ")
    nome_clientes = input("Digite o nome do cliente: ")
    novo_endereco = (input("Digite o ENDEREÇO novo: "))
    cursor = conexao.cursor()
    comando = f'UPDATE clientes SET endereco = "{novo_endereco}" WHERE  cpf = "{cpf_cliente}" AND nome= "{nome_clientes}"'

    cursor.execute(comando)
    conexao.commit()
    print("ENDEREÇO ATUALIZADO COM SUCESSO")

    cursor.close()
    conexao.close()        

    