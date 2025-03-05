import defs

defs.limpaTerminal()

while True:
    escolha = defs.menu()

    if escolha == '1':
        defs.cadastro()
    elif escolha == '2':
        defs.mostraDados()
    elif escolha =='3':
        defs.clientesCadastrados()
    elif escolha == '4':
        defs.relatorio()
    elif escolha == '0':
        print('\033[1;33mBom rolê e até a proxima!\033[0;0m')
        break
    else:
        defs.limpaTerminal()
        defs.criaBarra()
        print('\033[1;31mInsira uma opção válida!\033[0;0m')
        defs.criaBarra()