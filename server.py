import SimpleSockets as ss
import socket
import lib

s = ss.connection('127.0.0.1',5000,'server',logging=True)

def on_connect(cs,ip,port):
    lib.log('+',f'{ip}:{port} Connected!')
def on_disconnect(cs,ip,port):
    lib.log('-',f'{ip}:{port} Disconnected!')
def on_msg(msg,cs,address):
    ip = address[0]
    port = address[1]
    lib.log('*',f'{ip}:{port}: {msg}')
    for cs in s.clients:
        cs.send(f'[JOIN] {ip}:{port}'.encode())
    
s.on_connect = on_connect
s.on_disconnect = on_disconnect
s.on_msg = on_msg

ss.stop()
