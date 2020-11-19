import socket
import _thread

server_ip = '192.168.225.100'
server_port = 65432

player_positions = ['0,0', '-200,-200']

def threaded_client(conn, player_id):
    while True:
        data = conn.recv(1024)
        if not data:
            print('Client Disconnected')
            break
        conn.sendall(player_positions[player_id % 2].encode())
        player_positions[player_id - 1] = data.decode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((server_ip, server_port))
    server_socket.listen()

    players = 0
    player_id = 0

    while True:
        conn, addr = server_socket.accept()
        print('Client Connected')
        players = players + 1
        player_id = player_id + 1
        _thread.start_new_thread(threaded_client, (conn, player_id))