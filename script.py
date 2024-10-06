import sys, time

# Arquivo CSV
nome_arquivo = 'Dados.csv'

# Menu do CSV Reader
def menu():
    print("------------------------")
    print("#### CSV Reader 1.0 ####")
    print("------------------------")
    print("1. Listar dados")
    print("2. Filtro por dominio")
    print("3. Sair")

# Listar dados
def listar_dados():
    print("Listando dados...")
    time.sleep(5)

# Filtrar por dominio
def filtro_por_dominio():
    filtro = input("digite o dominio: ")

    # listar_emails_por_dominio(filtro)
    print("Listando dados...")

    time.sleep(5)

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