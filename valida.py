import defs 

def Nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Erro! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome valido.')
                break
        else:
            return nome.strip(' ')
        
def Senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Erro! Entrada vazia.')
            continue
        return senha.strip(' ')
      
        
def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Erro! Entrada vazia.')
            
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido! Deve conter "@" e ".com"')

def Data():
    while True:
        data= input('Nascimento: (dd/mm/aaaa):  ')
        if data == '':
            print('Erro! Entrada vazia.')
            continue
        temp = ''.join(data.split('/'))
        if not temp.isnumeric():
            print('Insira uma data válida.')
            continue
        if data.count('/') == 2 and data != '//':
            dia, mes, ano = data.split('/')
            if 1 < int(dia) < 31 and 1 < int(mes) < 12 and 1900 < int(ano) < 2022:
                return data.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaaa') 

def Login():
    while True:
        login = input('Login: ')
        if login == '':
            print('Erro! Entrada vazia.')
            continue
        return login.strip(' ')
def tele():
    while True:
        tele = input('Telefone: ( Apenas números.): ')
        if tele == '':
            print('Erro! Entrada vazia.')
            continue
        elif not tele.isnumeric():
            print('Insira apenas números.')
            continue
        else:
            if len(tele) >= 9 and len(tele) <= 11:
                return tele
            else:
                print('O número deve ter entre 9 - 11 caracteres.')

def ender():

    
   while True:
        print('------------- <<< \033[1;32mSeu Endereço Completo!\033[0;0m >>> ----------------')
        dados = {
            'rua':  input("Rua: "),
            'numero': input("Número: "),
            'complemento': input("Complemento (se houver): "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: "),
            'cidade': input("Cidade: "),
            'estado': input("Estado: "),
            'referencia': input('Referencia: ')
        }
        return dados
  


         
        
    