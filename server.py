import socket
import threading

# specify the port
HEADER = 64
PORT = 5050
# get the server ipv4 address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE ='disconnected'
# pick the socket and bind the socket to the address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)
# connect new client to the server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("msg recieved".encode(FORMAT))
    conn.close()

# start the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[STARTING] server is starting....")
start()