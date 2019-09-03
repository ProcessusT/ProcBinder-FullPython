import socket
import sys

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0', 666))
serv.listen(5)

try:
    while True:
        (conn, address) = serv.accept()
        print ("new connection from : "+str(address)+"\n")
        while True:
            r=str( sys.stdin.readline() )
            conn.send(r.encode())
            r = conn.recv(9999)
            client_answer = str( r.decode("utf-8", errors="ignore"))
            print(str(client_answer)+"\n")
    conn.close()
    print('client disconnected')
except KeyboardInterrupt:
    conn.close()
except Exception as e:
    print(str(e))
    conn.close()