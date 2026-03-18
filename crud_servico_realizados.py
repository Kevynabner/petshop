''''from conexao import conectar
from crud_servicos import listar_servicos

def registrar_servico_realizado():
    conexao = conectar()
    cursor = conexao.cursor()

    servicos = listar_servicos()

    servico_id = int(input("\nDigite o código do serviço: "))
    cpf_dono = input("Digite o CPF do dono: ")
    nome_pet = input("Digite o nome do pet: ").lower()

    if servico_id not in servicos:
        print("Serviço inválido.")
        return

    cursor.execute(
        "SELECT id FROM pets WHERE nome = %s AND cpf_dono = %s",
        (nome_pet, cpf_dono)
    )
    resultado = cursor.fetchone()

    if resultado is None:
        print("Pet não encontrado para esse dono.")
        cursor.close()
        conexao.close()
        return

    pet_id = resultado[0]

    valor = servicos[servico_id]['preco']

    comando = """
    INSERT INTO servico_realizados (cpf_dono, pet_id, servico_id, valor)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(comando, (cpf_dono, pet_id, servico_id, valor))
    conexao.commit()

    print("Serviço registrado com sucesso!")

    cursor.execute("SELECT SUM(valor) FROM servico_realizados WHERE cpf_dono = %s", (cpf_dono,))
    total = cursor.fetchone()[0] or 0

    print(f"Total gasto por esse cliente: R$ {total:.2f}")


    cursor.close()
    conexao.close()