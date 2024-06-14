def cabecalho():
    print("-" * 34)
    print("*******FACULDADE CESUSC*********")
    print("CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS")
    print("NOME: Gustavo Costa Gonçalves")
    print("Discipl.: LÓGICA DE PROG. E ALGORÍTMOS")
    print("Prof. Roberto Fabiano Fernandes")
    print("Turma: ADS:11 /  Ano:2024")
    print("Avaliação: N2/N3")
    print("-" * 34)


# Função para cadastro dos Dados
def cadastrar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de apêndice (adicionar dados ao final do arquivo)
        with open("Dados.txt", "a") as arquivo:
            # Solicitar ao usuário as informações do aluno
            codigo_pet = input("Digite o código do seu pet: ")
            nome_cliente = input("Digite o seu nome: ")
            contato = input("Digite um número para contato: ")
            cep = input("Digite o seu cep: ")
            ponto_de_referencia = input("Digite um ponto de refencia: ")
            nome_pet = input("Digite o nome do seu pet: ")
            data_nascimento = input("Digite a data de nascimento do seu pet: ")
            raca = input("Digite a raça do seu pet: ")
            peso = input("Digite o peso do seu pet: ")
            cor = input("Digite a cor do seu pet: ")
            obs = input("Observações: ")

            # Formatar os dados do aluno em uma string
            cliente = f"{codigo_pet},{nome_cliente},{contato},{cep},{ponto_de_referencia},{nome_pet},{data_nascimento},{raca},{peso},{cor},{obs}\n"

            # Escrever a string formatada no arquivo 'Dados.txt'
            arquivo.write(cliente)

            # Exibir uma mensagem de sucesso
            print("Dados do cliente cadastrados com sucesso!")
    except ValueError:
        # Capturar um erro caso os valores fornecidos pelo usuário não estejam no formato esperado
        print("Valor inválido.")
    except Exception as e:
        # Capturar qualquer outro erro que possa ocorrer durante o cadastro dos dados
        print("Ocorreu um erro ao cadastrar os dados:", str(e))


# Função para Listar os dados
def listar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
        with open("Dados.txt", "r") as arquivo:
            # Ler todas as linhas do arquivo e armazená-las em uma lista
            linhas = arquivo.readlines()

            # Verificar se não há linhas (dados) no arquivo
            if not linhas:
                print("Nenhum dado de cliente cadastrado.")
            else:
                # Exibir um cabeçalho para os dados dos alunos
                print("-" * 25)
                print("Dados cadastrados: ")

                # Iterar sobre cada linha do arquivo
                for linha in linhas:
                    # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco
                    dados = linha.strip().split(",")

                    # Extrair os valores individuais de cada dado
                    codigo_pet = dados[0]
                    nome_cliente = dados[1]
                    contato = dados[2]
                    cep = dados[3]
                    ponto_de_referencia = dados[4]
                    nome_pet = dados[5]
                    data_nascimento = dados[6]
                    raca = dados[7]
                    peso = dados[8]
                    cor = dados[9]
                    obs = dados[10]
                print("Dados atualizados!")
    except FileNotFoundError:
        # Capturar o erro caso o arquivo 'Dados.txt' não seja encontrado
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        # Capturar qualquer outro erro que possa ocorrer durante a listagem dos dados
        print("Ocorreu um erro ao atualizar os seus dados:", str(e))


# Função para alterar os dados
def alterar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
        with open("Dados.txt", "r") as arquivo:
            # Ler todas as linhas do arquivo e armazená-las em uma lista
            linhas = arquivo.readlines()
        # Verificar se não há linhas (dados) no arquivo
        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return
        # Solicitar ao usuário o código do aluno que deseja alterar
        codigo_pet = input("Digite o código do pet que deseja alterar: ")
        encontrado = False

        # Abrir o arquivo 'Dados.txt' em modo de escrita ('w')
        with open("Dados.txt", "w") as arquivo:
            # Percorrer cada linha do arquivo
            for linha in linhas:
                # Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco
                dados = linha.strip().split(",")

                # Verificar se o código do aluno na linha atual corresponde ao código fornecido pelo usuário
                if dados[0] == codigo_pet:
                    # Solicitar ao usuário os novos dados para o aluno
                    novo_codigo_pet = input("Digite o novo código do seu pet: ")
                    novo_nome_cliente = input("Digite o novo nome do cliente: ")
                    novo_contato = input("Digite o novo número para contato: ")
                    novo_cep = input("Digite o seu novo cep: ")
                    novo_ponto_de_referencia = input(
                        "Digite um novo ponto de refencia "
                    )
                    novo_nome_pet = input("Digite o novo nome do pet: ")
                    nova_data_de_nascimento = input(
                        "Digite a nova data de nascimento do seu pet: "
                    )
                    nova_raca = input("Digite a nova raça do seu pet: ")
                    novo_peso = input("Digite o novo peso do seu pet: ")
                    nova_cor = input("Digite a nova cor do seu pet: ")
                    nova_obs = input("Digite uma nova observação: ")

                    # Criar uma nova linha com os novos dados do aluno
                    linha = f"{novo_codigo_pet},{novo_nome_cliente},{novo_contato},{novo_cep},{novo_ponto_de_referencia},{novo_nome_pet},{nova_data_de_nascimento},{nova_raca},{novo_peso},{nova_cor},{nova_obs}\n"
                    print("Dados do cliente alterados com sucesso!")
                    encontrado = True
                # Escrever a linha no arquivo
                arquivo.write(linha)
        # Verificar se nenhum aluno foi encontrado com o código fornecido
        if not encontrado:
            print("Nenhum pet encontrado com o código fornecido.")
    except ValueError:
        # Capturar o erro caso algum valor inválido seja inserido pelo usuário
        print("Valor inválido.")
    except Exception as e:
        # Capturar qualquer outro erro que possa ocorrer durante a alteração dos dados
        print("Ocorreu um erro ao alterar os dados:", str(e))


def excluir_dados():
    try:
        with open("Dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if not linhas:
            print("Nenhum dado de pet cadastrado.")
            return
        codigo_pet = int(input("Digite o código do pet que deseja excluir: "))
        encontrado = False

        with open("Dados.txt", "w") as arquivo:
            for linha in linhas:
                dados = linha.strip().split(",")
                if int(dados[0]) == codigo_pet:
                    encontrado = True
                    print("Dados do pet excluídos com sucesso!")
                else:
                    arquivo.write(linha)
        if not encontrado:
            print("Nenhum pet encontrado com o código fornecido.")
    except ValueError:
        print(
            "Valor inválido. Certifique-se de digitar um valor numérico para o código do aluno."
        )
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados:", str(e))
        
        

#Função Backup
def backup_dados():

    #Tentativa de criar um backup dos dados
    try:

        #Abrir dados clientes 
        with open ('Dados.txt','r') as origem:
            dados = origem.read()

            #Criar uma copia dos dados clientes
            with open ('dados_backup.txt','w') as destino:
                destino.write(dados)

        #Alerta de sucesso
        print("Backup realizado com sucesso!")
    
    #Exceção de erro arquivo não encontrado
    except FileNotFoundError:
        print("Arquivo de origem não encontrado")
     #Exceção de erro backup não realizado
    except Exception as e: 
        print("Ocorreu um erro ao realizar o backup de dados: ", str(e))


def exibir_menu():
    while True:
        print("Escolha a opção:")
        print("1 - Cadastrar Dados")
        print("2 - Listar Dados")
        print("3 - Alterar Dados")
        print("4 - Excluir Dados")
        print("5 - Backup Dados")
        print("6 - cabeçalho")
        print("0 - Sair")
        opcao = input("Digite a sua opção: ")

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            alterar_dados()
        elif opcao == "4":
            excluir_dados()
        elif opcao == "5":
            backup_dados()
        elif opcao == "6":
            cabecalho()
        elif opcao == "0":
            print("Voce está saindo do sistema...")
            break
        else:
            print("Opção inválida. Digite um número válido.")