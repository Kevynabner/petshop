from conexao import conectar

# CREATE
def cadastrar_pet():
    conexao = conectar()
    cursor = conexao.cursor()

    nome_pet = input("Digite o nome do seu PET: ").lower()
    especie = input("Digite a espécie/raça do seu PET: ").lower()
    cpf_dono = input("Digite o CPF do dono: ")

    # validação de CPF
    comando = 'SELECT cpf FROM clientes WHERE cpf = %s'
    cursor.execute(comando, (cpf_dono,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("CLIENTE NÃO CADASTRADO. Cadastre o cliente primeiro.")
        cursor.close()
        conexao.close()
        return

    comando = 'INSERT INTO pets (nome, raca, cpf_dono) VALUES (%s, %s, %s)'
    cursor.execute(comando, (nome_pet, especie, cpf_dono))
    conexao.commit()

    print(f'PET {nome_pet} CADASTRADO COM SUCESSO')

    cursor.close()
    conexao.close()


# READ - listar todos os pets
def listar_pets():
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'SELECT * FROM pets'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    print("________ PETS CADASTRADOS ________\n")
    for i in resultado:
        print(f'NOME = {i[1]}')
        print(f'ESPÉCIE = {i[2]}')
        print(f'CPF-DONO = {i[3]}\n')
        print("______________________\n")

    cursor.close()
    conexao.close()


# READ - listar pets por dono
def listar_pets_dono():
    conexao = conectar()
    cursor = conexao.cursor()

    cpf_dono = input("Digite o CPF do dono: ")

    comando = 'SELECT * FROM pets WHERE cpf_dono = %s'
    cursor.execute(comando, (cpf_dono,))
    resultado = cursor.fetchall()
    
    if resultado:
        print("________ PETS DO DONO ________\n")
        for i in resultado:
            print(f'NOME = {i[1]}')
            print(f'ESPÉCIE = {i[2]}')
            print(f'CPF-DONO = {i[4]}\n')
            print("______________________\n")
    else:
        print("NENHUM PET ENCONTRADO PARA ESSE CPF.")

    cursor.close()
    conexao.close()


# READ - total de pets no sistema
def listar_pets_sistema():
    conexao = conectar()
    cursor = conexao.cursor()

    comando = 'SELECT COUNT(*) FROM pets'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    print(f"TOTAL DE PETS CADASTRADOS NO SISTEMA: {resultado[0]}")

    cursor.close()
    conexao.close()


# UPDATE
def atualizar_dono():
    conexao = conectar()
    cursor = conexao.cursor()

    dono_antigo = input("Digite o CPF do antigo dono: ")
    nome_pet = input("Digite o nome do seu PET: ").lower()
    novo_dono = input("Digite o CPF do novo DONO: ")

    comando = 'UPDATE pets SET cpf_dono = %s WHERE cpf_dono = %s AND nome = %s'
    cursor.execute(comando, (novo_dono, dono_antigo, nome_pet))
    conexao.commit()

    if cursor.rowcount > 0:
        print("DONO ATUALIZADO COM SUCESSO")
    else:
        print("PET NÃO ENCONTRADO")

    cursor.close()
    conexao.close()


# DELETE
def deletar_pets():
    conexao = conectar()
    cursor = conexao.cursor()

    cpf_dono = input("Digite o CPF do DONO: ")
    nome_pet = input("Digite o nome do PET que deseja EXCLUIR: ").lower()

    comando = 'DELETE FROM pets WHERE cpf_dono = %s AND nome = %s'
    cursor.execute(comando, (cpf_dono, nome_pet))
    conexao.commit()

    if cursor.rowcount > 0:
        print("PET DELETADO COM SUCESSO")
    else:
        print("PET NÃO ENCONTRADO")

    cursor.close()
    conexao.close()