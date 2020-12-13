import socket
import _thread

server_ip = '192.168.1.102'
server_port = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((server_ip, server_port))

first_player_positon = None
second_player_positon = None

# connection_addresses = {'First Player':None, 'Second Player':None}
player_positions = {}

def threaded_client(data, connection_address):
    # global first_player_positon
    # global second_player_positon

    # if connection_address == connection_addresses[0]:
    #     first_player_positon = str(data)

    global player_positions

    connection_address = connection_address

    player_positions[connection_address] = data.decode('utf-8')

    players = list(player_positions)
    other_player_index = (players.index(connection_address) + 1) % 2

    try:
        other_player = players[other_player_index]
        msg = player_positions[other_player].encode('utf-8')
    except:
        msg = '-200,-200'.encode('utf-8')
        
    sock.sendto(msg, connection_address)


while True:
    print('Waiting for client.')
    data, client_address = sock.recvfrom(1024)

    _thread.start_new_thread(threaded_client, (data, client_address))