import valida 
import datetime
import os

#Funções

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():    #criar barras para estilos
    return print('-' * 50)

data = datetime.datetime.now()  #atualização data diaria para def relatorio()
dia = data.day
mes = data.month
ano = data.year

def menu():
    print('------------- <<< \033[1;96msk8-Life\033[0;0m >>> -------------------')
    print('| [\033[1;36m1\033[0;0m] Cadastrar Cliente                          |')
    print('| [\033[1;36m2\033[0;0m] Dados do Cliente                           |')
    print('| [\033[1;36m3\033[0;0m] Mostrar Clientes                           |')
    print('| [\033[1;36m4\033[0;0m] Gerar Relatórios                           |')
    print('| [\033[1;36m0\033[0;0m] Sair                                       |')
    print('------------- <<< \033[1;96mSistema Moderno\033[0;0m >>> ------------')
    
    x = input('\033[1;36mInsira a opção: \033[0;0m')
    print('|___________________________________________________________________|')
    
    return x

'''def de Cadastrar / Checar login existente / adicionar dados no  arquivo txt de logins'''
def cadastro():
    limpaTerminal()
    print('------------- <<< \033[1;92mCadastrar Usuário\033[0;0m >>> -------------------')
    nome = valida.Nome()  # Retorna o nome validado
    login = valida.Login()  # Retorna o login validado
    
    # -> Conferir se já existe o login cadastrado
    lerLogins = open('logins.txt', 'r')
    for linha in lerLogins.readlines():  # Ler linhas do arquivo logins.txt
        valores = linha.split('-')
        # -> Criar lista com valores da linha
        # Nome: Jeff -Login: jeffin -> ['Nome: Jeff','Login: jeffin' ...]
        if login == valores[1].split(":")[1].strip():
            # Confere se login cadastrado é igual da linha
            limpaTerminal()
            criaBarra()
            print('\033[1;36mLogin já existe!\033[0;0m')
            criaBarra()
            lerLogins.close()
            return  # return para parar a função e não cadastrar
    
    lerLogins.close()
    
    senha = valida.Senha()
    email = valida.Email()
    data = valida.Data()
    tele = valida.tele()
    ender = valida.ender()  # Retorna o endereço validado em um discionário
    
    limpaTerminal()
    criaBarra()
    print('\033[1;32mCliente cadastrado com sucesso!\033[0;0m')
    criaBarra()
    
    # Adicionar dados no banco de dados login.txt
    logins = open('logins.txt', 'a')
    logins.write(f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Data de Nascimento: {data} -Numero de celular: {tele} -Endereco: {ender}\n')
    logins.close()
    
    return
'''Logar um usuario e printar seus dados cadastrados'''
def mostraDados():
    limpaTerminal()
    print('\033[1;33mDados do Cliente\033[0;0m')
    criaBarra()
    print('\033[1;33mLogue para acessar seus dados!\033[0;0m')
    criaBarra()
    
    userlogin = input('Login: ')
    usersenha = input('Senha: ')
    valida = False  # Variavel de validação do login
    
    logins = open('logins.txt', 'r')  # Percorre cada linha do logins.txt
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin in valores[1] and usersenha in valores[2]:
            # Checa se login e senha estão em valores['Login: ---'] e valores ['Senha: ---']
            limpaTerminal()
            criaBarra()
            print('\033[1;33mLogue para acessar seus dados!\033[0;0m')
            criaBarra()
            
            for percorre in range(len(valores)):
                # for no range do tamanho da lista criada
                if valores[percorre].split(':')[0] == 'Endereco':
                    # ['Nome: Vitor', 'Login: vitim', ..., 'Endereco: {}']
                    # [['Nome', 'Vitor'],['Login', 'vitim'],...,['Endereco', '{}']]
                    dictEndereco = eval(valores[percorre].split('Endereco:')[1])
                    # ['Nome: Vitor -Login: vitim ...', '{}']
                    for chave in dictEndereco:
                        print(f'{chave}: {dictEndereco[chave]}')
                else:
                    print(valores[percorre])
                
            criaBarra()
            valida = True  # valida o login e break
            logins.close()
            break
    
    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31mErro! Login ou senha invalidos\033[0;0m')  # não achou login e senha
        criaBarra()
                            

def clientesCadastrados():
    limpaTerminal()
   
    print('\033[1;33m——— Clientes Cadastrados ———\033[0;0m')
    criaBarra()
    
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        # ler cada linha
        l = linha.split('-')
        # Divide no '-' e forma uma lista com os valores divididos
        print(f'\033[1;92m{l[0]} | {l[1]}\033[0;0m')
        # Printa primeiros indices -> Nome: nome | Login: login
    
    criaBarra()
    return

def relatorio():
    countClient = 0  # variável para contar o número de clientes
    nomess = []  # lista para armazenar nomes dos clientes

    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])  # Adiciona o primeiro valor (no caso 'Nome: nome') na lista
        countClient += 1  # conta um cliente

    limpaTerminal()
    arquivo = open('dados.txt', 'w+')  # "w+" para criar o relatorio
    arquivo.write('Relatorio de Clientes \\n')
    arquivo.write('\n')
    arquivo.write(f'A Loja Sk8-Life possui {countClient} cliente(s) \\n')
    arquivo.write('\\n')

    for i in range(len(nomess)):  # for range para percorrer os indices da lista nomess
        arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))  # printa cada indice da lista
    arquivo.write(f'Russas, {dia}/{mes}/{ano}.')  # data atualizada para o relatorio gerado
    criaBarra()
    print('\033[1;32m'"Realatorio gerado em 'dados.txt'"'\033[0;0m')
    arquivo.close()
    return

