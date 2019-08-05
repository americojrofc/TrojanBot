import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 7777

s.bind((host, port))

s.listen(1)

print ('Aguardando Conexão')

conn, endereco = s.accept()
print ('Conexão estabelecida com: ' + endereco[0] + str(endereco[1]))


while True:
    cmd = input('Comando: ')
    conn.send(cmd.encode())
    resposta = conn.recv(204800)
    print (resposta)
