import socket

print('\tCLIENTE')

IP = input('- Digite o IP do Servidor: ')

PORTA = int(input('- Digite a PORTA: '))

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((IP, PORTA))

def enviarReceberMensagem(nome):
    mensagem = nome.encode('utf-8')
    
    tamanhoMensagem = len(mensagem)

    tamanhoEnvio = str(tamanhoMensagem).encode('utf-8')
    tamanhoEnvio += b' ' * (64 - len(tamanhoEnvio))
    
    cliente.send(tamanhoEnvio)
    cliente.send(mensagem)

    numeroTelefonico = cliente.recv(2048).decode('utf-8')

    if numeroTelefonico == '1':
        print('\nNão existe contatos para esse nome!\n')
    elif numeroTelefonico == '0':
        print('\nSaindo da Aplicação...\n')
    else:
        print('\nContato de ' + nome.upper())
        print('-'*18)
        print('|' + numeroTelefonico + '|')
        print('-'*18 + '\n')

while True:
    nome = input('- Digite o nome de uma pessoa: ')
    enviarReceberMensagem(nome.lower())
    
    if nome.lower() == 'sair':
        exit()