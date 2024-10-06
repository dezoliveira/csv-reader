import sys, time, csv

# Arquivo CSV
nome_arquivo = 'Dados.csv'

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
    filtro=""

    print("Listando dados...")
    listar_emails(nome_arquivo, filtro)
    time.sleep(5)

####### FILTROS #######

# Filtrar por dominio
def filtro_por_dominio():
    filtro = input("digite o dominio: ")

    print("Listando dados...")
    listar_emails(nome_arquivo, filtro)

    time.sleep(5)

####### LISTAGENS #######

# Lista email por dominio
def listar_emails(nome_arquivo, filtro):
    with open(nome_arquivo, mode='r', encoding='utf8') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)

        if not (filtro):
            listar_todos_emails(reader)
            return
        
        if (filtro):
            listar_emails_por_dominio(reader, filtro)
            return

# Lista todos os emails
def listar_todos_emails(reader):
    for linha in reader:
        print(f"ID: {linha['id']}, Nome: {linha['nome']}")

# Lista os emails por filtro
def listar_emails_por_dominio(reader, filtro):
    count = 0
    print(f"E-mails do dominio: '{filtro}' ")

    for linha in reader:
        if linha['email'].endswith(filtro):
            count = count + 1
            print(f"ID: {linha['id']}, Nome: {linha['nome']}")

    if (count == 0):
            print(f"Domino '{filtro} não encontrado' ")
                
# Main function
def main():
    while True:
        menu()

        # ------------------------
        # #### CSV Reader 1.0 ####
        # ------------------------
        # 1. Listar dados
        # 2. Filtro por dominio
        # 3. Sair

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