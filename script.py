import os, sys, time, csv

# Arquivo CSV
nome_arquivo = 'dados.csv'

####### MENU OPTIONS #######

# Menu do CSV Reader
def menu():
    print('''
        ------------------------------
            ### CSV Reader 1.0 ###
        ------------------------------
        [1]. Listar dados
        [2]. Filtro por dominio
        [3]. Sair
        ------------------------------
    ''')

# Listar dados
def listar_dados():
    # deixa o filtro vazio
    filtro=""

    print("Listando dados...\n")

    # chama função de listar de emails passanndo o filtro
    listar_emails(filtro)

    time.sleep(5)

####### FILTROS #######

# Filtrar por dominio
def filtro_por_dominio():
    # armazena o input do usuário
    filtro = input("digite o dominio: ")

    print("Listando dados...\n")

    # chama funcão de listar emails passando o filtro
    listar_emails(filtro)

    time.sleep(5)

####### VALIDAÇÕES #######

# Valida arquivo CSV
def valida_arquivo_csv():

    # usa o os para verificar se existe o arquivo csv.
    # se existir, retorna True
    if os.path.isfile(nome_arquivo):
        return True
    
    # senão retorna False e exibe as mensagens
    else:
        print(f'''Arquivo {nome_arquivo} não encontrado\n\n'''
              f'''- Verifique se o arquivo existe \n'''
              f'''- Verifique o nome do arquivo \n\n'''
              f'''O nome do arquivo deve ser {nome_arquivo}'''
        )   
        time.sleep(2)
        return False

####### LISTAGENS #######

# Lista email por dominio
def listar_emails(filtro):

    # valida se arquivo csv existe (retorna True ou False)
    # se existir
    if valida_arquivo_csv():

        # prepara o reader
        with open(nome_arquivo, mode='r', encoding='utf8') as arquivo_csv:
            reader = csv.DictReader(arquivo_csv)
            
            # se tiver fitro, listar_emails_por_dominio
            if (filtro):
                listar_emails_por_dominio(reader, filtro)
                return
            
            # senão listar_todos_emails
            else:
                listar_todos_emails(reader)
                return
    # senão sai do programa
    else:
        sys.exit()

# Lista todos os emails
def listar_todos_emails(reader):
    for linha in reader:
        print(f"ID: {linha['id']}, Nome: {linha['nome']}")

# Lista os emails por filtro
def listar_emails_por_dominio(reader, filtro):

    # inicia o contador
    count = 0

    print(f"E-mails do dominio: '{filtro}' ")

    # varre o reader linha a linha
    for linha in reader:

        # se houver algum email com esse filtro:
        # soma no contador
        # printa a linha na tela
        if linha['email'].endswith(filtro):
            count = count + 1
            print(f"ID: {linha['id']}, Nome: {linha['nome']}")

    # se o contador estiver vazio, não encontrou nada com esse filtro
    if (count == 0):
            print(f"Domino '{filtro} não encontrado' ")
                
# Main function
def main():

    # loop para manter o menu sempre visível
    while True:
        menu()

        # menu de opçoes
        '''
        ------------------------------
            ### CSV Reader 1.0 ###
        ------------------------------
        [1]. Listar dados
        [2]. Filtro por dominio
        [3]. Sair
        ------------------------------
        '''

        opcao = input("Escolha uma opção: ")

        if (opcao == "1"):
            listar_dados()

        elif (opcao == "2"):
            filtro_por_dominio()

        elif (opcao == "3"):
            sys.exit()

        else:
            print("Opção inválida. Tenten novamente")

if __name__ == "__main__":
    main()