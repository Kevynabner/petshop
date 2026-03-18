from conexao import conectar


def servicos_disponiveis():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM servico '
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("________SERVIÇOS DISPONÍVEIS________\n")
    for i in resultado:
        print(f'{i[0]} - {i[1]} - {i[2]} ')
    cursor.close()
    conexao.close()
    registrar_servicos()


def registrar_servicos():
    conexao = conectar()
    cpf_cliente = int(input("Digite o seu CPF "))
    nome_pet = input("Digite o nome do PET: ").lower()
    opcao = int(input("Digite o Nº do serviço: "))
    
    cursor = conexao.cursor()

    comando_pet = f'SELECT id FROM pets WHERE nome = "{nome_pet}"'
    cursor.execute(comando_pet)
    resultado = cursor.fetchone()
    
    if resultado is None:
        print("PET NÃO ENCONTRADO")
        return 
    
    id_pet = resultado[0]
    
    comando_servico = f'SELECT preco FROM servico WHERE id = {opcao}'
    cursor.execute(comando_servico)
    resultado = cursor.fetchone()

    if resultado is None:
        print(f'VALOR NÃO ENCONTRADO')
        return   
    

    id_servico = opcao 
    valor = resultado[0]  
    comando = f'INSERT INTO servico_realizados (cpf_dono, pet_id, servico_id, valor) VALUES ("{cpf_cliente}", "{id_pet}", "{id_servico}", "{valor}")'
    cursor.execute(comando)
    conexao.commit()

    print("SERVIÇO REGISTRADO COM SUCESSO")

    cursor.close()
    conexao.close()


def total_servicos():

    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM servico_realizados'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("________SERVICOS REALIZADOS________\n")
    print(f'TOTAL DE SERVIÇOS REALIZADOS = {len(resultado)}\n')
    faturamento()
    
    cursor.close()
    conexao.close() 

def faturamento():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "SELECT SUM(valor) FROM servico_realizados"
    cursor.execute(comando)
    resultado = cursor.fetchone()
    print(f'TOTAL FATURAMENTO = R${resultado[0]}')
    
