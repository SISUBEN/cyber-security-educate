#control.py
import socket
import threading

host = "127.0.0.1"
 
def recv(sock, addr):
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
 
 
def send(sock, addr):
    while True:
        string = input('command > ')
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break
 
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (host, 9999)
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()
 
if __name__ == '__main__':
    print("Start to listening...")
    name = input('input the client nickname:')
    main()