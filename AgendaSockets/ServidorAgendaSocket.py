import socket 
import threading

IP = '127.0.0.1'
PORTA = 5555

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((IP, PORTA))

def agendaTelefonica(nome):
    if nome == 'marcos':
        return '(84) 9 9644-9431'
    elif nome == 'andre':
        return '(84) 9 9914-4420'
    elif nome == 'azevedo':
        return '(84) 9 9431-9644'
    elif nome == 'assis':
        return '(84) 9 1234-4567'
    elif nome == 'sair':
        return '0'
    else:
        return '1'

def receberEnviarMensagem(conexao, endereco):
    print('\nConexão Estabelecida.\nO Cliente é: {0}'.format(endereco))

    conectado = True
    
    while conectado == True:
        tamanhoMensagem = conexao.recv(64).decode('utf-8')
        
        if tamanhoMensagem:
            tamanhoMensagem = int(tamanhoMensagem)
            mensagem = conexao.recv(tamanhoMensagem).decode('utf-8')
            
            numeroTelefonico = agendaTelefonica(mensagem)
            conexao.send((numeroTelefonico).encode('utf-8'))

            if mensagem == 'sair':
                print("{0} saiu.".format(endereco))
                conectado = False
            else:
                print("{0} buscou por '{1}'".format(endereco, mensagem))
    
    print('Finalizando Thread.\n')            
    conexao.close()

def main():
    print('\tSERVIDOR')
    
    servidor.listen()

    print('\nAVISO: O Não escreva se o servidor não tiver qualquer mensagem para responder.')
    print('\nEsperando por clientes: ')
    
    while True:
        conexao, endereco = servidor.accept()
        print('Iniciando Thread...')
        thread = threading.Thread(target = receberEnviarMensagem, args = (conexao, endereco))
        thread.start()
        print('\n{0} Thread de conexao(ões) ativa(s).'.format(threading.activeCount()-1))

main()