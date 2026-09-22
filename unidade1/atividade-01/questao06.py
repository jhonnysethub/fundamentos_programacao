escolha = int(input("MENU: \n1 - Cadastrar Aluno\n2 - Consultar Aluno\n3 - Alterar Aluno\n4 - Excluir Aluno\n5 - Listar Alunos\n6 - Sair\nSelecione uma das opções: "))

match escolha:
    case 1:
        print("Você selecionou Cadastrar Aluno")
    
    case 2:
        print("Você selecionou Consultar Aluno")
    
    case 3:
        print("Você selecionou Alterar Aluno")
    
    case 4:
        print("Você selecionou Excluir Aluno")
    
    case 5:
        print("Você selecionou Listar Alunos")
    
    case 6:
        print("Você selecionou Sair")
    
    case _:
        print("Opção inválida")