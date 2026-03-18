from conexao import conectar
from crud_cliente import cadastrar_cliente, listar_clientes, deletar_cliente, atualizar_endereco
from crud_pet import cadastrar_pet, listar_pets_dono, atualizar_dono, deletar_pets, listar_pets_sistema
from crud_servicos import servicos_disponiveis,total_servicos
conexao = conectar


tam = 30 
opcao = {
    "1" : "CADASTRAR CLIENTE",
    "2" : "CLIENTES CADASTRADOS",
    "3" : "ATUALIZAR ENDEREÇO",
    "4" : "DELETAR CLIENTE",
    "5" : "CADASTRAR PET",
    "6" : "PETS CADASTRADOS POR DONO",
    "7" : "ATUALIZAR DONO",
    "8" : "DELETAR PET",
    "9" : "LISTAR TOTAL DE PETS",
    "10": "REGISTRAR SERVIÇOS",
    "11": "SERVIÇOS / FATURAMENTO",
    "0" : "SAIR",
}

while True:
    print(f'+{"-" * tam}+')
    print(f"|{'MENU':^{tam}}")
    print(f'+{"-" * tam}+')
    for chave, valor in opcao.items():
        print(f"|{f'{chave} - {valor}':{tam}}|")
    print(f'+{"-" * tam}+') 

    option = input("Digite sua opção: ")

    if option not in opcao:
        print("OPÇÃO INVÁLIDA")
        continue   
    elif option == "0":
        print("PROGRAMA ENCERRADO")
        break
    elif option == "1":
        cadastrar_cliente()

    elif option == "2": 
        listar_clientes()

    elif option == "3":
        atualizar_endereco()

    elif option == "4":
        deletar_cliente()
    
    elif option == "5":
        cadastrar_pet()

    elif option == "6":
        listar_pets_dono()

    elif option == "7":
        atualizar_dono()   

    elif option == "8":
        deletar_pets()         
        
    elif option == "9":
        listar_pets_sistema() 

    elif option == "10":
        servicos_disponiveis() 

    elif option == "11":
        total_servicos()