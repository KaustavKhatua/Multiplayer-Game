#!/usr/bin/env python3

import socket
import _thread

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

starting_positions_player1 = '0,0/200,200'
starting_positions_player2 = '200,200/0,0'

player_positions = [b'0,0', b'200,200']

def threaded_client(conn, players):
    global player_positions
    with conn:
        if players == 1:
            conn.sendall(starting_positions_player1.encode())
        else:
            conn.sendall(starting_positions_player2.encode())
        while True:
            data = conn.recv(1024)
            if not data:
                print('Client disconnected.')
                break
            conn.sendall(player_positions[players % 2])
            # decoded_data = data.decode("utf-8")
            player_positions[players - 1] = data

            # x = int(decoded_data.split(',')[0])
            # print(x)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    players = 0
    while True:
        conn, addr = s.accept()
        players = players + 1
        _thread.start_new_thread(threaded_client, (conn, players))